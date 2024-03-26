import cv2
import mediapipe as mp
import time
import pyautogui

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

screenWidth, screenHeight = pyautogui.size()
cap.set(3, 640)  
cap.set(4, 480)  

pTime = 0

CLICK_THRESHOLD = 0.05
HOLD_THRESHOLD = 0.05
DOUBLE_CLICK_THRESHOLD = 0.05
RIGHT_CLICK_THRESHOLD = 0.05

isHolding = False

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            landmarks = [(lm.x, lm.y, lm.z) for lm in handLms.landmark]
            if len(landmarks) > 4:
                index_tip = landmarks[8]
                thumb_tip = landmarks[4]
                middle_tip = landmarks[12]
                ring_tip = landmarks[16]
                pinky_tip = landmarks[20]

                mouseX, mouseY = int(index_tip[0] * screenWidth), int(index_tip[1] * screenHeight)
                mouseX = min(max(mouseX, 0), screenWidth - 1)
                mouseY = min(max(mouseY, 0), screenHeight - 1)
                pyautogui.moveTo(mouseX, mouseY)

                distances = {
                    "thumb_index": ((index_tip[0] - thumb_tip[0])**2 + (index_tip[1] - thumb_tip[1])**2 + (index_tip[2] - thumb_tip[2])**2)**0.5,
                    "thumb_middle": ((middle_tip[0] - thumb_tip[0])**2 + (middle_tip[1] - thumb_tip[1])**2 + (middle_tip[2] - thumb_tip[2])**2)**0.5,
                    "thumb_ring": ((ring_tip[0] - thumb_tip[0])**2 + (ring_tip[1] - thumb_tip[1])**2 + (ring_tip[2] - thumb_tip[2])**2)**0.5,
                    "thumb_pinky": ((pinky_tip[0] - thumb_tip[0])**2 + (pinky_tip[1] - thumb_tip[1])**2 + (pinky_tip[2] - thumb_tip[2])**2)**0.5,
                }

                
                circle_colors = [(255, 0, 255) for _ in range(5)] 


                for key, distance in distances.items():
                    if distance < CLICK_THRESHOLD:
                        if key == "thumb_index":
                            pyautogui.click()
                            circle_colors[1] = (0, 255, 0) # Yeşil
                        elif key == "thumb_middle":
                            if not isHolding:
                                pyautogui.mouseDown()
                                isHolding = True
                            circle_colors[2] = (255, 255, 0) # Sarı
                        elif key == "thumb_ring":
                            pyautogui.click(clicks=2, interval=0.2)
                            circle_colors[3] = (0, 0, 255) # Mavi
                        elif key == "thumb_pinky":
                            pyautogui.rightClick()
                            circle_colors[4] = (0, 255, 255) # Cyan

                if isHolding and all(distance >= HOLD_THRESHOLD for distance in distances.values()):
                    pyautogui.mouseUp()
                    isHolding = False

                for i, landmark in enumerate([thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip]):
                    pos_x = int(landmark[0] * img.shape[1])
                    pos_y = int(landmark[1] * img.shape[0])
                    cv2.circle(img, (pos_x, pos_y), 10, circle_colors[i], cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
