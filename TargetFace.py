import cv2
import torch
import matplotlib as plt
import numpy as np
import cv2
import yolov5
#Yukarıda kütüphaneleri ekledik.
#================================================================

#Aşağıda Güvenlik kamerası adında bir fonksiyon tanımladık ve içine olmasını istediğimiz özellkikleri yazıyoruz.
#def SecurityCamera():

#öncelikle modeli yüklüyoruz.
model = torch.hub.load('ultralytics/yolov5','yolov5m')

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('Trail',frame)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

""""


Bilgisayar yer açtıktan sonra tekrardan dene


"""