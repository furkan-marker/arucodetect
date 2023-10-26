
import numpy as np
import cv2 
import cv2.aruco as aruco
cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dictionary_1 = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    
    
    parameters = cv2.aruco.DetectorParameters() 
    detector = cv2.aruco.ArucoDetector(dictionary_1,parameters)
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)
    
    
    frame = aruco.drawDetectedMarkers(frame, markerCorners)
    cv2.imshow('Display', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    
cap.release()
cv2.destroyAllWindows()

