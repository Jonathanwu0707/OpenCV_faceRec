import cv2
from cv2 import waitKey
from cv2 import destroyAllWindows

cam = cv2.VideoCapture(0)

cv2.namedWindow("123",cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()
    img = cv2.flip(frame, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("face_Rec/face_detect.xml")
    faceRec = faceCascade.detectMultiScale(gray, 1.05, 7, minSize=(70, 70))

    for(x, y, w, h) in faceRec:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "face",(x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0),thickness=2)
    cv2.imshow("123", img)
    waitKey(1)

