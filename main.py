import cv2
import mediapipe
from hand import Hand
from mouse import Mouse
import sys, time


webcam = cv2.VideoCapture(0)
hand = Hand()
mouse = Mouse()
FPS = 60


start = time.time()
end = 0
while True:
    _, frame = webcam.read()
    frame.flags.writeable = False
    cv2.imshow('MediaPipe Hands', frame)

    if cv2.waitKey(1) == ord('q'):
        break

    index = hand.get_index(cv2.flip(frame, 1))
    if not index:
        continue

    # coordinates = (int(index.x * frame.shape[1]), int(index.y * frame.shape[0]))
    # cv2.circle(frame, coordinates, 2, (0, 255, 0))
    mouse.move(index.x, index.y)

    end = time.time()
    print(f'FPS: {1/(end - start)}')
    start = end
    
    



webcam.release()
cv2.destroyAllWindows()
sys.exit(0)