# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:19:44 2020

@author: kacper
"""

#potrzebne biblioteki
import speech_recognition as sr
import pyttsx3 as tts
from playsound import playsound

version = "1.0"
author = "Avir Frog"

'''
Ponizszy slownik ma za zadanie konwertowac "uslyszane" przez Mariana slowa do 
odpowiedniej formy. Marian niestety ma problem i czasem zamiast interpretowac
liczbe jako liczbe  interpretuje ja jako slowo, np. gdy powiem dwa dodać dwa
zamiast wykonac polecenie 2 + 2 proboje on skonkatenowac slowa dwa i dwa.
'''
liczby ={'jeden': 1, '1': 1, 'dwa': 2, '2': 2, 
         'trzy': 3, '3': 3, 'cztery': 4, '4': 4,  
         'pięć': 5, '5': 5}

r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 150)


def speak(text):
	engine.say(text)
	engine.runAndWait()


def get_Text():
	with sr.Microphone() as source:
		try:
			print("Słucham...")
			audio = r.listen(source)
			text = r.recognize_google(audio, language='pl-PL')
			if text != "":
				return text
			return 0
		except:
			return 0


def rounding_of_numbers(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


while True:
    
    try:
        txt = get_Text().lower()
        txt = txt.split()   
        if txt != 0 and txt[0] == 'marian':
            print(txt)
            speak("Tak")
            if txt != 0 and txt[1] == 'witaj':
                print(txt)
                speak("Witaj, co mogę dla Ciebie zrobić?")
                continue
            elif txt != 0 and txt[1] == 'tryb' and txt[2] == 'bojowy':
                print(txt)
                speak("Włączam tryb bojowy")
                playsound('x.mp3')
            elif txt != 0 and txt[1] == 'wyloguj':
                print(txt)
                speak("Dozobaczenia")
                break
            elif txt != 0 and txt[1] == 'policz':
                print(txt)
                speak("Zaraz policzymy")
                if txt != 0 and txt[3] == 'dodać':
                    print(txt)
                    speak("dodawanie")
                    n1 = int(txt[2])
                    n2 = int(txt[4])
                    print(n1)
                    print(n2)
                    wynik = n1 + n2
                    mwynik = str(wynik)
                    speak(f'{str(n1)} dodać {str(n2)} jest równe {mwynik}')
                    continue
                elif txt != 0 and (txt[3] == '-' or txt[3] == 'minus'):
                    print(txt)
                    speak("odejmowanie")
                    n1 = int(txt[2])
                    n2 = int(txt[4])
                    print(n1)
                    print(n2)
                    wynik = n1 - n2
                    mwynik = str(wynik)
                    print(wynik)
                    print(mwynik)
                    speak(f'{str(n1)} minus {str(n2)} jest równe {mwynik}')
                    continue
                elif txt != 0 and txt[3] == 'na':
                    print(txt)
                    speak("dzielenie")
                    n1 = int(txt[2])
                    n2 = int(txt[4])
                    print(n1)
                    print(n2)
                    wynik = rounding_of_numbers((n1 / n2), 2)
                    mwynik = str(wynik)
                    speak(f'{str(n1)} podzielić {str(n2)} jest równe {mwynik}')
                    continue
                elif txt != 0 and (txt[3] == 'x' or txt[3] == 'razy'):
                    print(txt)
                    speak("mnożenie")
                    n1 = int(txt[2])
                    n2 = int(txt[4])
                    print(n1)
                    print(n2)
                    wynik = n1 * n2
                    mwynik = str(wynik)
                    speak(f'{str(n1)} razy {str(n2)} jest równe {mwynik}')
                    continue
                else:
                    print(txt)
                    speak("Potrafię tylko dodawać, odejmować, dzielić i mnożyć dlatego nie wiem co to {txt[3]}")
                    continue
            elif txt != 0 and txt[1] == 'informacje':
                print(txt)
                speak(f"Informacje o bocie głosowym Marian. Wersja {version}, Autor {author}.")
                continue
                
            else:
                print(txt)
                continue
        else:
            print(txt)
            continue
    except:
        print(".")