import pyttsx3
import pyaudio
import wikipedia
import datetime
import os
import random
import webbrowser
import speech_recognition as sr
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email_and_password import *
from time import sleep
from playsound import playsound
import requests
import pyautogui

# creating a dictonary
# you can add more peoples using comma in both dictonary
Email_dic = {'Name of the person': 'Email address of that person'}
whatsApp_dic = {'Name of the person': 'Name of that person in whatsApp'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 178)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon')
    else:
        speak('Good evening')

    speak('I am alexa, please tell me how may I help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            print('Sorry, say that again please')
            return "None"
        return query


def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(senderEmail, passW)
    server.sendmail(senderEmail, to, content)
    server.close()


def whatsApp(to, content):
    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-data-dir=C:\\Users\\<Username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')
    chrome_browser = webdriver.Chrome(
        executable_path='CHROME DRIVER PATH', options=options)
    chrome_browser.get('https://web.whatsapp.com')
    sleep(15)
    try:
        user = chrome_browser.find_element_by_xpath(
            '//span[@title="{}"]'.format(whatsApp_dic[to]))
        user.click()

        message_box = chrome_browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(content)
        chrome_browser.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

        speak('Message send successfully')
        chrome_browser.close()
    except Exception as e:
        print(e)
        speak('Failed to send whatsapp message')
        chrome_browser.close()


if __name__ == '__main__':
    wishMe()
    ask = True
    while ask:
        query = takeCommand().lower()

        # logic
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            ask = True
        elif 'google' in query:
            speak('What do you want to search on google')
            search = takeCommand()
            driver = webdriver.Chrome()
            driver.get('https://www.google.com')
            driver.maximize_window()
            try:
                speak('Searching on google')
                inputElements = driver.find_element_by_css_selector(
                    'input[name=q]')
                inputElements.send_keys(search)

                # press Enter key,
                speak(f"Showing all reults for {search}")
                inputElements.send_keys(Keys.ENTER)
                ask = True
            except Exception as e:
                # print(e)
                speak('Unable to search on google')
                ask = False

        elif 'youtube' in query:
            speak('What do you want to search on youtube')
            search = takeCommand()
            driver = webdriver.Chrome()
            driver.get('https://www.youtube.com')
            driver.maximize_window()
            try:
                speak('Searching on youtube')
                inputElements = driver.find_element_by_css_selector(
                    'input[name=search_query]')
                inputElements.send_keys(search)
                inputElements.send_keys(Keys.ENTER)
                speak(f"showing all the results for {search}")
                ask = True
            except Exception as e:
                print(e)
                speak('Unable to search on youtube')
                ask = False
        elif 'stackoverflow' in query:
            speak('Searching for stackover flow')
            webbrowser.open('www.stackoverflow.com')
            ask = Trueelif 'music' in query:
            speak('Playing music')
            try:
                music_dir = 'Music directory path here'
                songs = os.listdir(music_dir)
                speak('I will play a random song for you')
                done = True
                while done:
                    playingSong = random.choice(songs);
                    print(playingSong)
                    speak('Would you like to play the above printed song - Yes or No')
                    yesOrNo = takeCommand().lower()
                    if 'yes' in yesOrNo:
                        playsound(f"{music_dir}\\{playingSong}")
                        done = False
                    else:
                        speak('I will play one more random song for you')
                        done = True
            except Exception as e:
                print(e)
                speak('There was an error while playing music, please try again to play music')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            ask = True
        elif 'whatsapp' in query:
            speak('To whom you want to send message')
            to = takeCommand().lower()
            if to in whatsApp_dic:
                speak(f'{to} found')
                speak('Please tell what message you want to send')
                content = takeCommand()
                whatsApp(to, content)
                ask = True
            else:
                speak(f'{to} not found')
                ask = False
        elif 'vs code' in query:
            path = "C:\\Users\\<Username>\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            ask = True
        elif 'email' in query:
            try:
                speak('To whom you want to send email')
                to = takeCommand().lower()
                if to in Email_dic:
                    speak('What should I add in message')
                    content = takeCommand()
                    sendMail(Email_dic[to], content)
                    speak('Email has been sent successfully')
                    ask = True
                else:
                    speak(f'{to} not found')
                    ask = False
            except Exception as e:
                print(e)
                speak('Something went wrong will sending mail')
                ask = False
        elif 'screenshot' in query:
            try:
                speak('Please tell the file name')
                filename = takeCommand()
                pyautogui.screenshot(
                    f"D:\Python\VS code Python\AI\images\{filename}.png")
                speak('Screenshot has been taken and store in images folder')
                ask = True
            except Exception as e:
                speak('Unable to take screenshot')
                ask = False
        elif 'alarm' in query:
            speak('Hey user please tell hour in 24 hour format')
            speak('Please tell me hour')
            hour = int(takeCommand())
            # hour = int(input('Enter the hour in 24 hour format: '))
            speak('Please tell me minute')
            minute = int(takeCommand())
            # minute = int(input('Enter the minute: '))
            speak('You alarm has been added')
            hasOccured = True
            if type(hour) == int and type(minute) == int:
                while (hasOccured):
                    if hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute:
                        playsound('alert_signal.mp3')
                        hasOccured = False
                        break
                    else:
                        hasOccured = True
            else:
                speak('Alarm not add successfully')
        elif 'location' in query:
            try:
                res = requests.get('https://ipinfo.io/')
                # converting str to json
                data = res.json()
                city = data['city']
                speak(f"You are at {city}")
                location = data['loc'].split(',')
                latitude = location[0]
                longitude = location[1]
                speak(f"latitude {latitude} and logitude {longitude}")
                print(f"You are at {city}")
                print(f"latitude: {latitude} and logitude {longitude}")
                ask = True
            except Exception as e:
                print(e)
                speak('Unable to detect your location')
                ask = False
        elif 'thank you' in query:
            speak('I am here to help,please let me know if you need anything else')
            ask = False
