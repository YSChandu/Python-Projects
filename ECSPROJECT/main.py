from gpiozero import MCP3208
from time import sleep
import time
import urllib.request
import RPi.GPIO as GPIO
from gtts import gTTS
import os
import speech_recognition as sr
from pygame import mixer

language = 'en'
mixer.init()
recognizer = sr.Recognizer()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buz = 26

GPIO.setup(buz, GPIO.OUT)


def play_voice(message):
    myobj = gTTS(text=message, lang=language, slow=False)
    myobj.save("message.mp3")
    time.sleep(1)
    os.system("omxplayer message.mp3")


s1 = MCP3208(channel=0, device=0)
s2 = MCP3208(channel=1, device=0)
s3 = MCP3208(channel=2, device=0)
s4 = MCP3208(channel=3, device=0)
s5 = MCP3208(channel=4, device=0)

print('Initializing.. Sensors..')

s1val = (s1.value * 5) * 1000
s2val = (s2.value * 5) * 1000
s3val = (s3.value * 5) * 1000
s4val = (s4.value * 5) * 1000
s5val = (s5.value * 5) * 1000
time.sleep(1)
s1int = (s1.value * 5) * 1000
s2int = (s2.value * 5) * 1000
s3int = (s3.value * 5) * 1000
s4int = (s4.value * 5) * 1000
s5int = (s5.value * 5) * 1000
print('Reading Sensor Info')

label1 = 'I_NEED_WATER'
label2 = 'I_NEED_FOOD'
label3 = 'I_NEED_MEDICINE'
label4 = 'I_NEED_TO_GO_OUT'
label5 = 'I_NEED_HELP'
prv = 0
while True:
    s1val = (s1.value * 5) * 1000
    s2val = (s2.value * 5) * 1000
    s3val = (s3.value * 5) * 1000
    s4val = (s4.value * 5) * 1000
    s5val = (s5.value * 5) * 1000

    # print("S1:" +str(round(s1val,2)) + "  S2:" +str(round(s2val,2)) + "  S3:" +str(round(s3val,2)) + "  S4:" +str(round(s4val,2)) + "  S5:" +str(round(s5val,2)) )
    if ((s1val - s1int) > 300 and (s2val - s2int) > 300):

        with sr.Microphone() as source:
            print("Start Talking")
            audio_text = recognizer.listen(source)
            print("Time over, thank you")
            try:
                # using google speech recognition
                voicemsg = recognizer.recognize_google(audio_text)
                print("Text: " + str(voicemsg))
                wp = urllib.request.urlopen(
                    "https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=voice_msg:" + str(voicemsg))
                time.sleep(2)
            except:
                print("Sorry, I did not get that")


    elif ((s1val - s1int) > 300):
        print(label1)
        myobj = gTTS(text='I NEED WATER pl', lang=language, slow=False)
        myobj.save("1.mp3")
        time.sleep(2)
        os.system("omxplayer 1.mp3")
        time.sleep(4)
        wp = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=" + label1)



    elif ((s2val - s2int) > 300):
        print(label2)
        myobj = gTTS(text='I NEED FOOD pl', lang=language, slow=False)
        myobj.save("2.mp3")
        time.sleep(2)
        os.system("omxplayer 2.mp3")
        time.sleep(4)
        wp = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=" + label2)



    elif ((s3val - s3int) > 300):
        print(label3)
        myobj = gTTS(text='I NEED MEDICINE pl', lang=language, slow=False)
        myobj.save("3.mp3")
        time.sleep(2)
        os.system("omxplayer 3.mp3")
        time.sleep(4)
        wp = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=" + label3)


    elif ((s4val - s4int) > 300):
        print(label4)
        myobj = gTTS(text='I NEED TO GO OUT pl', lang=language, slow=False)
        myobj.save("4.mp3")
        time.sleep(2)
        os.system("omxplayer 4.mp3")
        time.sleep(4)
        wp = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=" + label4)


    elif ((s5val - s5int) > 300):
        print(label5)
        myobj = gTTS(text='I NEED HELP pl', lang=language, slow=False)
        myobj.save("5.mp3")
        time.sleep(2)
        os.system("omxplayer 5.mp3")
        time.sleep(4)
        wp = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=A6N32PE55CSD15FA&field1=" + label5)

    r_link = 'https://api.thingspeak.com/channels/208732/fields/1/last?api_key=SRNPOCHVDBR7UDOY'
    f = urllib.request.urlopen(r_link)
    rcv = (f.readline()).decode()
    if (prv != rcv):
        prv = rcv
        print('INFO: ' + str(rcv))
        myobj = gTTS(text=rcv, lang=language, slow=False)
        myobj.save("rcv.mp3")
        time.sleep(1)
        os.system("omxplayer rcv.mp3")

