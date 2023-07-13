import time
import cv2
import torch
import numpy as np
from memory_profiler import profile
@profile(func=None, stream=None, precision=1, backend='psutil')
def HedefZaman(saati, saatf):
  while True:
    saat = time.strftime("%H:%M")

    if saati <= saat <= saatf:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4v algoritmasını tanımlama
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, force_reload=True)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model.to(device)
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            results = model(frame)
            cv2.imshow('Trail', np.squeeze(results.render()))
            if 'person' in results.pandas().xyxy[0]['name'].tolist():
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # XVID algoritmasını tanımlama
                kayit1 = cv2.VideoWriter('kanıt.mp4', fourcc, 10.0, (640, 480))
            else:
                kayit = cv2.VideoWriter('kayit.mp4', fourcc, 10.0, (640, 480))
                kayit.pause()

    else:
        print("Zaman henüz gelmedi")
        time.sleep(2)



while True:
    try:
        saat_baslangic = input("Başlangıç saati (HH:MM): ")
        saat_bitis = input("Bitiş saati (HH:MM): ")
        HedefZaman(saat_baslangic, saat_bitis)
        if len(saat_baslangic) != 5 or len(saat_bitis) != 5:
            raise ValueError("Hatalı saat formatı! Lütfen HH:MM formatında girin.")
        break
    except ValueError as e:
        print("Hata:", e)
        print("Lütfen doğru saat formatını kullanın.")
    except KeyboardInterrupt:
        print("Program Ctrl+C ile sonlandırıldı.")

HedefZaman(saat_baslangic, saat_bitis)
