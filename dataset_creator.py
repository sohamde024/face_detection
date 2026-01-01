import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertorupdate(Id, Name, age):
    conn= sqlite3.connect('database.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1

    if isRecordExist == 1:
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE ID=?",(Name,Id))
        conn.execute("UPDATE STUDENTS SET AGE=? WHERE ID=?", (age, Id))

    else:
        conn.execute("INSERT INTO STUDENTS (Id,Name,age) values (?,?,?)",(Id, Name, age))

    conn.commit()
    conn.close()

Id= input("Enter Student ID: ")
Name= input("Enter Student Name: ")
age= input("Enter Student Age: ")

insertorupdate(Id, Name, age)

samNum = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        samNum = samNum + 1
        cv2.imwrite("dataset/user."+str(Id)+"."+str(samNum)+".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if samNum>20:
        break

cam.release()
cv2.destroyAllWindows()