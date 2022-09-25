import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import ArduinoKodlari

r=sr.Recognizer()

class SesliAsistan:

    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr")
        dosya = str(random.randint(0, 10000000000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def mikrofon(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum..")
            listen=r.listen(kaynak)
            ses=""
            try:
                ses=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("ne dediğinizi anlayamadım")
            return ses

    def ses_karslik(self,gelen_Ses):
        if(gelen_Ses in "merhaba"):
            self.seslendirme("size de merhabalar")
        elif(gelen_Ses in "nasılsın"):
            self.seslendirme("iyiyim sizler nasılsınız")
        elif(gelen_Ses in "led'i yak"):
            try:
                self.seslendirme("led'inizi hemen yakıyorum")
                ArduinoKodlari.led_islemleri(1)
            except:
                self.seslendirme("bir hata meydana geldi. lütfen daha sonra tekrar deneyiniz")

        elif(gelen_Ses in "led'i söndür"):
            try:
                self.seslendirme("led'inizi hemen söndürüyorum")
                ArduinoKodlari.led_islemleri(0)
            except:
                self.seslendirme("bir hata meydana geldi. lütfen daha sonra tekrar deneyiniz")


    def uyanma_fonksiyonu(self,gelen_Ses):
        if(gelen_Ses in "hey siri"):
            self.seslendirme("dinliyorum...")
            ses=self.mikrofon()
            if(ses!=""):
                print(ses)
                self.ses_karslik(ses)



asistan = SesliAsistan()

while True:
    gelen_Ses=asistan.mikrofon().lower()
    if(gelen_Ses!=""):
        print(gelen_Ses)
        asistan.uyanma_fonksiyonu(gelen_Ses)

