import cv2 as cv
import numpy as np
import video2numpy
import time
import tensorflow as tf

def VideoCamera():
    VideoCam=cv.VideoCapture(1)
    if VideoCam.isOpened():
        print("Kameraya Bağlanılıyor...")
    #Aşağıda while döngüsüne kadar olan iki satırda video görüntüsünün en boy oranını belirtik.
        VideoCam.set(cv.CAP_PROP_FRAME_WIDTH,640)
        VideoCam.set(cv.CAP_PROP_FRAME_HEIGHT,480)

        def change_pixel_size_720p():
            VideoCam.set(cv.CAP_PROP_FRAME_WIDTH,1366)
            VideoCam.set(cv.CAP_PROP_FRAME_HEIGHT,720)

        def change_pixel_size_4K():
            VideoCam.set(3,1920)
            VideoCam.set(4,1080)

        def user_settin_pixel_size(width, height):
            VideoCam.set(3,width)
            VideoCam.set(4,height)
        #user_settin_pixel_size(600,600) #Bu komut satırında kullanıcı kamera boyutunu ayarlıyor eğer boyutu ayarlamak istemezse
        #bu satırı yorum satırı yapabilir.
        while True:
            ret,VideoImg=VideoCam.read()
            if ret:
                kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])

                image_sharp = cv.filter2D(src=VideoImg, ddepth=-1, kernel=kernel)
                cv.imshow("Security Camera", image_sharp)
                #changegray=cv.cvtColor(VideoImg,cv.COLOR_BGR2GRAY)     # change gray   color to    gray color_BGR2GRAY (COLOR_BGR2GRAY kameradaki görüntüyü griye çeviriyor)
            # Daha yüksek fps ve daha düşük bir yer kaplaması açısından RGB renk skalası yerine gri renk skalası tercih edilmiştir.
#******************Bu ara kısma HDR görüntüye dönüştürme komutu ekle****************************************************






            #*********************************************************
            else:
                print("Hata: Çerçeve Oluşutulurken Hata Oluştu")
            if cv.waitKey(1) & 0xFF == ord('q'):    #waitKey(1) iken bir değer bekliyor. waitKey(0) iken sonsuz oluyor.
                break
    else:
        print("Hata: Kameraya Bağlanılamadı")
    VideoCam.release()  #Okunan değişkenin bellekte kapladığı alanı serbest bırak gibi bir anlama geliyor.

    cv.destroyWindow("Security Camera")

#Bu satır ile yazdığımız fonksiyonu çalıştırıyoruz.
VideoCamera()