import cv2
faceCap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

videoCap = cv2.VideoCapture(0)
while True :
    ret , videoData =videoCap.read()
    col = cv2.cvtColor(videoData,cv2.COLOR_BGR2GRAY)
    faces = faceCap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors= 5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(videoData,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("videoLive",videoData)
    if cv2.waitKey(10) == ord("f"):
        break
videoCap.release()    