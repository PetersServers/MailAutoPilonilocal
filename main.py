#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import itertools as it
from time import sleep
from bs4 import BeautifulSoup
import requests
import smtplib
import numpy as np


counter = it.count()


URL = 'https://karrierebibel.de/lebensweisheiten/'
result = requests.get(URL)
doc = BeautifulSoup(result.text, "html.parser")

doc.getText

sp = (doc.findAll("li"))
spruch001 = (sp[22].parent.text)
spruch002 = (sp[44].parent.text)
spruch003 = (sp[66].parent.text)
spruch004 = (sp[88].parent.text)
spruch005 = (sp[100].parent.text)

spruch = (spruch001 + spruch002 + spruch003 + spruch004 + spruch005)

def fundamental_clean(sprüche):

    spruched1 = sprüche.replace('Ã¼', 'ue')
    spruched2 = spruched1.replace('â ', ' ')
    spruched3 = spruched2.replace('â', ' ')
    spruched4 = spruched3.replace('Ã¤', 'ae')
    spruched5 = spruched4.replace('â ', ' ')
    spruched6 = spruched5.replace('Ã¶', 'oe')
    spruched7 = spruched6.replace('Ã', 'ss')
    spruched8 = spruched7.replace('(', '')
    spruched9 = spruched8.replace('', ' ')
    spruched10 = spruched9.replace('©', '')
    spruched11 = spruched10.replace('²','')
    cleaned_spruch = spruched11.replace('â', '')

    return cleaned_spruch

clean_arr = []

def filter(arr):

    for i in range(len(arr)):
        if (arr[i]).isascii():
            clean_arr.append(arr[i])
            print(f'{i} is clean')
        else:
            print(f'{i} is not clean')

    return clean_arr

#call the filter functions on selected items

cleaned_spruch = fundamental_clean(spruch)

arr = np.array(cleaned_spruch.split(")"))

cleaned_arr = filter(arr)


while True:

    N = (next(counter))
    N1 = int(N + 84)
    N2 = str(N1)
    Netter_spruch = (cleaned_arr[N1])

    sender_email = "Peterservers@yahoo.com"
    reciever_email = "christian@karlpichler.it"
    password = ("uhcurlklgwqpgqcd")
    inhalt = 'Hoi Chrisse i wolt dir lei sogen dass du echt a cooler Typ bisch, und es isch wichtig dass man die an sel errinert!!! Ob iaz mit a motivierender Lebensweisheit #timetoremember #bestermann #capitano day' + N2 + Netter_spruch
    message = 'Subject: {}\n\n{}'.format("Wichtige Erinnerung inklusive Lebensweisheit von deinem Lieblingssohn", inhalt)
    # Inhalt als header formatiert sodass i an Betreff hinzufügen konn

    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(sender_email, password)
    #print("login success")
    server.sendmail(sender_email, reciever_email, message)
    print("the email has been sent to " + reciever_email)

    sleep(86400)


    #spruch = doc.findAll("::before")
    #print(spruch)
    #print(spruch[0].parent)
    #netter_spruch = (spruch[0].parent.string)

    