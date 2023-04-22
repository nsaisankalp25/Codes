import cv2
from datetime import datetime
import pyautogui
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while True:
    _,frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.1, 5)   
    num = 0
    for (x,y, width, height) in faces:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 255, 0), 4)
        take = pyautogui.screenshot().save(f'C:\\Users\\Vinod-2018\\Desktop\\TOTAL SAI THINGS\\sai stuff\\Sai Programming\\spam_pics\\{num}.png')
        now2 = datetime.now()
        date_time2 = now2.strftime("%m/%d/%Y, %H:%M:%S")
        print(date_time2)
        with open('isthere.txt', 'a') as store:
            num += 1
            store.write(f"Face deteced at time: {date_time}\n")
            store.close()
            
    cv2.imshow("Testing Cam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
