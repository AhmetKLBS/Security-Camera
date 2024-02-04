# Bu dosya mail gönderme işlemi yapar.
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#"encoders" change the encoding type so that changes to the document encoding.
# Simple Mail Transfer Protocol
# Basit Mail Transfer Protokolü
def sendmail():
    try:
        # Mail Mesaj Bilgisi
        post= MIMEMultipart()
        subcjet = "Test"
        message = "Bu bir test mesajıdır!"
        content = "Subject: {0}\n\n{1}".format(subcjet,message)

        # Hesap Bilgileri
        myMailAdress = "ahmetkulabas5414@gmail.com"
        apppasswd = "rtyihlajmwucapsl"
        # Yukarıdaki şifreyi https://myaccount.google.com/lesssecu... linki aracılığıyla alıyoruz.
        # Kime Gönderilecek Bilgisi
        sendTo = "ismetkulabas14@gmail.com"

        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, apppasswd)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        print("Mail Gönderme İşlemi Başarılı!")
    except Exception as e:
        print("Hata Oluştu!\n {0}".format(e))
