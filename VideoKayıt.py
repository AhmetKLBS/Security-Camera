import cv2
def VideoKayıt():
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
        cv2.imshow('goruntu', goruntu)  # Görüntüyü gösterme

        frame_sayaci += 1  # Kare sayacını artırma

        # Belirlenen süre dolana kadar veya 't' tuşuna basılana kadar kaydı devam ettirme
        if cv2.waitKey(10) & 0xFF == ord('r') or (cv2.getTickCount() - baslangic_zamani) / cv2.getTickFrequency() >= kayit_suresi:
            break

    kamera.release()  # Kamerayı serbest bırak
    kayit.release()# Kaydı durdur
    cv2.destroyAllWindows()  # Açılan pencereleri kapat