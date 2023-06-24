import time
import  VideoKayıt
def zaman_kontrol(saati, saatf):
  while True:
    saat = time.strftime("%H:%M:%S")
    if saati <= saat <= saatf:
        print("Zaman geldi kontrol ediliyor.")
        VideoKayıt.VideoKayıt()
    else:
        print("zaman gelmedi")


while True:
    try:
        saat_baslangic = input("Başlangıç saati (HH:MM:SS): ")
        saat_bitis = input("Bitiş saati (HH:MM:SS): ")
        if len(saat_baslangic) != 8 or len(saat_bitis) != 8:
            raise ValueError("Hatalı saat formatı! Lütfen HH:MM:SS formatında girin.")
        break
    except ValueError as e:
        print("Hata:", e)
        print("Lütfen doğru saat formatını kullanın.")

zaman_kontrol(saat_baslangic, saat_bitis)
