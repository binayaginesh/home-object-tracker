import cv2
import numpy as np

def main():
   
    cap = cv2.VideoCapture(0)

    
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    while True:
       
        ret, frame = cap.read()

        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        
        res = cv2.bitwise_and(frame, frame, mask=mask)

        
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', res)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

   
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
