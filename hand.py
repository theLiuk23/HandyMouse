import mediapipe as mp
import cv2




class Hand:
    def __init__(self):
        self.hands = mp.solutions.hands        


    def get_landmarks(self, frame) -> list[tuple[float]] | None:
        with self.hands.Hands(max_num_hands=1, model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame)
            return results.multi_hand_landmarks


    def get_index(self, frame) -> tuple[float]:
        hands = self.get_landmarks(frame)
        if hands:
            for landmark in hands[0].landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
            return hands[0].landmark[8]