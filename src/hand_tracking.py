import cv2
import mediapipe as mp

class handTracking:
    """ Hand Trackin Class which Detects the Hand and then Gives the LandMarks as output"""
    def __init__(self, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detection_confidence, 
            min_tracking_confidence=tracking_confidence
        )

    def process_frame(self, frame):
        """Processes the frame and returns detected hand landmarks."""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results

    def get_landmarks(self, result, frame):
        """
        Extracts hand landmarks and returns them as a dictionary.
        """
        landmarks_dict = {}
        if result.multi_hand_landmarks:  # ✅ Fixed Typo Here
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                for idx, landmark in enumerate(hand_landmarks.landmark):
                    landmarks_dict[idx] = (landmark.x, landmark.y)  # Store as (x, y) tuple

        return landmarks_dict
