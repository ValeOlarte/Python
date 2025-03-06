import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    if not check or frame is None:
        print("¡Error al capturar el frame!")
        break

    print(check)
    print(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 
                                      scaleFactor=1.1, 
                                      minNeighbors=5)
    
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)

    cv2.imshow("Capturing", frame)
    
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
