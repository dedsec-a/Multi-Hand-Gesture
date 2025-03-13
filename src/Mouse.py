import cv2
import mediapipe as mp
import pyautogui
from hand_tracking import handTracking  # Ensure hand_tracking.py has a class named handTracking

class Mouse:
    def __init__(self, smooth_factor=0.5, sensitivity=6):
        self.tracker = handTracking()
        self.smooth_factor = smooth_factor
        self.sensitivity = sensitivity
        self.screen_width, self.screen_height = pyautogui.size()

        # Initialize smoothing variables
        self.smoothed_x = None
        self.smoothed_y = None

    def get_mouse_coordinates(self, frame):
        """Processes frame and returns hand landmarks."""
        result = self.tracker.process_frame(frame)
        landmarks = self.tracker.get_landmarks(result, frame)
        return landmarks  

    def move_mouse(self, landmarks):
        """Moves the mouse smoothly based on index finger position."""
        if not landmarks:  # Check if landmarks dictionary is empty
            return

        # Extract index finger tip coordinates
        if 8 not in landmarks:  # Ensure index finger tip is detected
            return

        x, y = landmarks[8]  # Unpacking tuple (x, y)

        # Convert to screen coordinates
        x = int(x * self.screen_width)
        y = int(y * self.screen_height)

        # Initialize smoothing if first frame
        if self.smoothed_x is None or self.smoothed_y is None:
            self.smoothed_x, self.smoothed_y = x, y
        else:
            # Apply exponential smoothing
            self.smoothed_x = int(self.smooth_factor * self.smoothed_x + (1 - self.smooth_factor) * x)
            self.smoothed_y = int(self.smooth_factor * self.smoothed_y + (1 - self.smooth_factor) * y)

        # Move mouse
        pyautogui.moveTo(self.smoothed_x, self.smoothed_y)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    mouse = Mouse()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = mouse.get_mouse_coordinates(frame)
        mouse.move_mouse(landmarks)

        cv2.imshow("Mouse Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


        
          

           
     
