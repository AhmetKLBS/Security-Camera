import torch
import numpy as np
import cv2
import TargetTime
import  os
import time



def main():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m')
    saati = input("Hedef Zamanının Başlangıcını Giriniz: ")
    saatf = input("Hedef Zamanının Bitişini Giriniz: ")
    saat = time.strftime("%H:%M")
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        results = model(frame)
        cv2.imshow('Trail', np.squeeze(results.render()))
    #Tespit edildikten sonra belirli nesneyi tespit etmek istediğimizde aşağıdaki kod satırlarını eklememiz gerekiyor.
    #Eğer insan yerine başka bir nesneyi tespit etmek istiyorsak o nesnenin çerçeve üzerindeki ismini yazmamız gerekiyor.
    #Biz insan tespit etmek istediğimizden 'person' yazdık başka bir nesneyi tespit etmek istiyorsak bu
    #ifadeyi değiştirmemiz yeterli.
        if saati <= saat <= saatf:
            TargetTime.zaman_kontrol(saati, saatf)
            if 'person' in results.pandas().xyxy[0]['name'].tolist():
                kamera = cv2.VideoCapture(0)  # Kamerayı çağırma
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # XVID algoritmasını tanımlama
                kayit = cv2.VideoWriter('kayit.mp4', fourcc, 20.0, (640, 480))
                # fourcc ile saniyede 20 resim alarak 640x480 boyutlarında bir mp4 dosyası oluşturur

                frame_sayaci = 0  # Kare sayacı başlangıç değeri
                kayit_suresi = 360  # Kayıt süresi (saniye)
                baslangic_zamani = cv2.getTickCount()  # Başlangıç zamanını kaydetme

                while True:
                    ret, goruntu = kamera.read()  # Kamera okumayı başlatma
                    kayit.write(goruntu)  # Video yazmayı başlatma
                    frame_sayaci += 1  # Kare sayacını artırma
            else:
                os.wait()
    #----------------------------------------------------------------------------------------------------------------------
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    if __name__ == "__main__":
        main()
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
