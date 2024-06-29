import cv2
import numpy as np

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Define the range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only desired colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the resulting frame
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', res)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
