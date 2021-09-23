import cv2
'''
video = cv2.VideoCapture(0)

while True:
    shamim, img = video.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (19, 19), 0)
    cv2.imshow("Video", gray)


    if cv2.waitKey(1) & 0xFF == ord('s'):
       break

'''

#---------------------------------------------------------------------------------------------

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    shamim, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 6)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,225,128), 4)
        cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
       break
