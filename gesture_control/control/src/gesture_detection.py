#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)


# Function to detect hand gestures
def get_gesture(lmList, fingers, totalFingers):
    wrist_x, wrist_y = lmList[0][0], lmList[0][1]
    joint_x, joint_y = lmList[3][0], lmList[3][1]
    thumb_x, thumb_y = lmList[4][0], lmList[4][1]
    index_x, index_y = lmList[8][0], lmList[8][1]
    middle_x, middle_y = lmList[12][0], lmList[12][1]
    center_x, center_y = lmList[9][0], lmList[9][1]
    
    if totalFingers == 5:
        return "Stop"
    elif totalFingers == 0 and joint_x < wrist_x:
        return "Move Forward"
    elif totalFingers == 0 and joint_x > wrist_x:
        return "Move Backward"
    elif totalFingers == 1 and fingers[0] == 1:
        if thumb_x < joint_x and abs(thumb_y - joint_y) <= 30:
            return "Move Left"
        elif thumb_x > joint_x and abs(thumb_y - joint_y) <= 30:
            return "Move Right"
        else:
            return "Stop"
    elif totalFingers == 2 and fingers[1] * fingers[2] == 1:
        if index_x < middle_x:
            return "Turn Left"
        else:
            return "Turn Right"
    else:
        return "Stop"
    

# Function to publish gesture commands
def pub_gesture():
    pub = rospy.Publisher('/gesture', String, queue_size=10)  # publisher for gesture command (String)
    rospy.init_node('cam', anonymous=True)                    # initialize node
    rate = rospy.Rate(10)                                     # 10Hz rate

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = detector.findHands(frame)
        lmList, bbox = detector.findPosition(frame)
        gesture = "Stop"
        totalFingers = 0

        if lmList:  # Hand is detected
            fingers = detector.fingersUp()
            totalFingers = fingers.count(1)
            gesture = get_gesture(lmList, fingers, totalFingers)

        # Display
        cv2.putText(frame, f'Fingers: {totalFingers}', (20, 120), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.putText(frame, gesture, (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        pub.publish(gesture)
        rate.sleep()
  
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        pub_gesture()
    except rospy.ROSInterruptException:
        pass
