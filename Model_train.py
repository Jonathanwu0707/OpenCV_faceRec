import cv2
import cvzone


cam = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('Model_database/keras_model.h5','Model_database/labels.txt')



while True:
    ret, frame = cam.read()
    flip = cv2.flip(frame, 1)
    gray = cv2.cvtColor(flip, cv2.COLOR_BGR2GRAY )
    faceCascade = cv2.CascadeClassifier("face_Rec/face_detect.xml")
    faceRec = faceCascade.detectMultiScale(gray, 1.05, 8, minSize=(70, 70))
   
    for(x, y, w, h) in faceRec:
        prediction, index1 = myClassifier.getPrediction(flip)
        cv2.rectangle(flip, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(flip, "face",(x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0),thickness=2)

    cv2.imshow("Image", flip)
    cv2.waitKey(1)

