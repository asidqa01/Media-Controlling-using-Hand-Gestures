# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:28:17 2022

@author: ibrahim
"""

import cv2
import time
import HandTrackingModule as hm
import pyautogui as p
  
cap = cv2.VideoCapture(0)
 
pTime = 0
cTime = 0



detector = hm.handDetector()
tipIds = [4,8,12,16,20]

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)
   
   
    
    
    
    LmList = detector.findPosition(img,draw=False)
    #print(LmList)

    if len(LmList) != 0:    
        fingers = []
        if LmList[tipIds[0]][1] > LmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1,5):

            if LmList[tipIds[id]][2] < LmList[tipIds[id] - 2][2]:
               fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        
        
        if totalFingers == 0:
            cv2.putText(img, " ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255),2)
           
        elif totalFingers == 1:
            
            cv2.putText(img, "Play/Pause", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255), 2)
            cv2.waitKey(10)
            p.press("space")
            
        elif totalFingers == 2:
            p.press("volumeup")    
            cv2.putText(img, "Volume UP", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255), 2)
        
        elif totalFingers == 3:
            p.hotkey("volumedown")        
            cv2.putText(img, "Volume Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255), 2)
        
        elif totalFingers == 4:
            p.press("right")    
            cv2.putText(img, "Forward", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255), 2)
            
        elif totalFingers == 5:
                p.press("left")    
                cv2.putText(img, "Backward", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.2,(0,0,255), 2)
        
        else:
            pass
           
  
        
       
        


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (510, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    cv2.imshow("video",img)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break