import torch
import matplotlib as plt
import numpy as np
import cv2
import MailGonderme
import time
import TargetTime
dete=time.localtime()
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')
TargetTime=int(input("Hedef Zamanının Başlangıcını Giriniz: "))
TargetTimeEnd=int(input("Hedef Zamanının Bitişini Giriniz: "))
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame)
    cv2.imshow('Trail', np.squeeze(results.render()))
#Tespit edildikten sonra belirli nesneyi tespit etmek istediğimizde aşağıdaki kod satırlarını eklememiz gerekiyor.
#Eğer insan yerine başka bir nesneyi tespit etmek istiyorsak o nesnenin çerçeve üzerindeki ismini yazmamız gerekiyor.
#Biz insan tespit etmek istediğimizden 'person' yazdık başka bir nesneyi tespit etmek istiyorsak bu
#ifadeyi değiştirmemiz yeterli.
    if 'person' in results.pandas().xyxy[0]['name'].tolist():
        if TargetTime<=date<=TargetTimeEnd:
            pass


        #print("İnsan tespit edildi!")
#----------------------------------------------------------------------------------------------------------------------
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
