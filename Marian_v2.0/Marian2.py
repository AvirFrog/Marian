# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:19:44 2020
Updates: Marian v2.0 15:35:50 16.04.2022

@author: AvirFrog
"""

# required libraries
import speech_recognition as sr
import pyttsx3 as tts
import time

version = "2.0"
author = "AvirFrog"

sleep_time = 5 #Waiting for me to speak

recognizer = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_text():
    with sr.Microphone() as source:
        try:
            print("Słucham...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='pl-PL')
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
        txt = get_text().lower()
        txt = txt.split()
        match txt[0]:
            case "marian":
                print(txt)
                speak("Tak")
                match txt[1]:
                    case "witaj":
                        print(txt)
                        speak("Witaj, co mogę dla Ciebie zrobić?")
                        continue
                    case "wyloguj":
                        print(txt)
                        speak("Dozobaczenia")
                        break
                    case "policz":
                        print(txt)
                        speak("Zaraz policzymy")
                        match txt[3]:
                            case "dodać":
                                print(txt)
                                speak("dodawanie")
                                n1, n2 = int(txt[2]), int(txt[4])
                                mwynik = str(n1 + n2)
                                speak(f'{str(n1)} dodać {str(n2)} jest równe {mwynik}')
                                continue
                            case "minus":
                                print(txt)
                                speak("odejmowanie")
                                n1, n2 = int(txt[2]), int(txt[4])
                                mwynik = str(n1 - n2)
                                speak(f'{str(n1)} minus {str(n2)} jest równe {mwynik}')
                                continue
                            case "na":
                                print(txt)
                                speak("dzielenie")
                                n1, n2 = int(txt[2]), int(txt[4])
                                mwynik = str(rounding_of_numbers((n1 / n2), 2))
                                speak(f'{str(n1)} podzielić {str(n2)} jest równe {mwynik}')
                                continue
                            case "x" | "razy":
                                print(txt)
                                speak("mnożenie")
                                n1, n2 = int(txt[2]), int(txt[4])
                                mwynik = str(n1 * n2)
                                speak(f'{str(n1)} razy {str(n2)} jest równe {mwynik}')
                                continue
                            case "":
                                print(txt)
                                continue
                            case _:
                                print(txt)
                                speak(f"Potrafię tylko dodawać, odejmować, dzielić i mnożyć dlatego nie wiem co to {txt[3]}")
                                continue
                    case "informacje":
                        print(txt)
                        speak(f"Informacje o bocie głosowym Marian. Wersja {version}, Autor {author}.")
                        continue
                    case "":
                        print(txt)
                        continue
            case "":
                print(txt)
                continue
    except:
        time.sleep(sleep_time)
        speak("Skoro nic nie mówisz to wyłączam się. Bywaj")
        break