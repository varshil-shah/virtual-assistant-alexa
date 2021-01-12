# Personal Assistant using python

## Objective:
Automate all the boring stuffs that we use in our daily life.

***

## Use case:
You can save your time by using such automations and make your work easy

***

## Installation:
For installing complete project -
`https://github.com/Varshil-Shah/Personal-Assistant.git`

For installing all modules -
`pip install -r requirements.txt`

**Note**

If there is an error while installing pyaudio,use the following in terminal.

``` shell
1. pip install pipwin
2. pipwin install pyaudio
```
***

## Features:
1. You can get the information about every stuffs present on internet using wikipedia module.
`Command: Programming wikipedia `.

2. You can call google and ask your query and other stuffs.
`Command: Open google`.
3. You can call youtube and ask your query to get solutions/entertainment etc.
`Command: Open youtube`.
4. You can get solutions for your errors on stackoverflow
`Command: Open stackover flow`
5. You can play random music.
`Command: Play a random music`

6. You can get the present time.
`Command: Tell me current time`
7. You can send messages on whatsApp.
`Command: Send a whatsApp message`.

8. You can open any software, for this project we can open vs code editor.
`Command: Open vscode`.

9. You can send emails.
`Command: Send a email`.

10. You can take screenshots.
`Command: Take a screenshot`.

11. You can find your geo-location.
`Command: What is my location`.

12. You can add alarm.
`Command: Add alarm`.

***

### Usage note:
1. **For wikipedia:**
    You can ask your query and at last you have to speak wikipedia, you can find the solution for your query.

2. **For random musics:**
    You have to add your music directory path, I have mentioned the path name in the program, it will be easire for you to search.
3. **WhatsApp Message**
    1. In `options.add_argument` you have to change the username,according to your name in the PC.
    2. You have to add all the names and names of that person in your whatsApp,
     ``` python
    dic = {'name':'name in whatsApp'}`.
    ```
4. **VS code**
    You have to change username in path variable and set the name present in your PC.
5. **Email**
    1. You have to make your gmail id less secure.
    2. In `email_and_password.py` file you have to enter correct email id and password of that email id.
    3. You have to add names and email id in a dictonary.
    ``` python 
    dic = {'name of the person':'Email address of the person'}
    ```
6. **Screenshot**
    1. You have to say `Please take a screenshot`.
    2. You have to give file name.
    3. You have to provide folder name to save your images.
7. **Location**
    You have to ask your geo-location, assistant will speak and print your location.
    
8. **Alarm**
    1. You have to tell hour in 24hr format.
    2. You have to tell minute.
***

## About the creator:
### Varshil Shah

Feel free to mail me at my email address [varshilshah1004@gmail.com](mailto:varshilshah1004@gmail.com "Varshil Shah") for any queries.

>Work hard + smart

