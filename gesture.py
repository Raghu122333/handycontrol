import cv2 as cv
import mediapipe as mp
import pyautogui

cap=cv.VideoCapture(0)
my_hand=mp.solutions.hands.Hands()
draw=mp.solutions.drawing_utils
prev=None
while True:
    ret,frame=cap.read()
    rgb_image=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output=my_hand.process(rgb_image)
    hands=output.multi_hand_landmarks
    gesture="no hands"
    if hands:
        for hand in hands:
            draw.draw_landmarks(frame,hand,mp.solutions.hands.HAND_CONNECTIONS)
            lm=hand.landmark
            fingers=[]
            if lm[4].x>lm[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

            if lm[8].y<lm[6].y:
                fingers.append(1)
            else:
                fingers.append(0)

            if lm[12].y<lm[10].y:
                fingers.append(1)
            else:
                fingers.append(0)

            print(fingers)

            if lm[16].y<lm[14].y:
                fingers.append(1)
            else:
                fingers.append(0)

            if lm[20].y<lm[18].y:
                fingers.append(1)
            else:
                fingers.append(0)

            if fingers==[1,1,1,1,1]:
                gesture="palm"

            elif fingers==[0,0,0,0,0]:
                gesture="fist"

            elif fingers==[0,1,1,0,0]:
                gesture="peace"

            elif fingers==[1,0,0,0,0]:
                gesture="thumbs up"
            elif fingers==[0,1,1,1,1]:
                gesture="four"
            elif fingers==[0,1,0,0,0]:
                gesture="point"
            elif fingers==[0,0,1,1,1]:
                gesture="ok"
            else:
                gesture="unknown"

            if gesture!=prev:
                if gesture=="fist":
                    pyautogui.press('space')
                elif gesture=="palm":
                    pyautogui.typewrite("prasad tech in telugu", interval=0.1)
                elif gesture=="four":
                    pyautogui.press('enter')
                elif gesture=="peace":
                    pyautogui.press('down')
                elif gesture=="point":
                    pyautogui.moveRel(50,0)
                elif gesture=="ok":
                    pyautogui.scroll(200)

            prev=gesture
    cv.putText(frame,gesture,(20,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv.imshow('frame',frame)

    if cv.waitKey(1) & 0xff==ord('b'):
        break

cap.release()
cv.destroyAllWindows()