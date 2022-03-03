import requests
import json
from win32com.client import Dispatch

def speak(content):
    response = requests.get(content)
    data = json.loads(response.content)
    spell = Dispatch("SAPI.SpVoice")
    spell.Speak("Hello sir, i am your assistant!.. I am here to inform you, Some latest current affair headlines.")
    for i in range(10):
        News = data['articles'][i]['title']
        spell.Speak(f"News {i+1} : {News}")         
        print(f"News {i+1} : {News}")
    spell.Speak("Thank You")
    print("Thank You.")

if __name__ == "__main__":
    content = "https://newsapi.org/v2/top-headlines?country=in&apiKey=0bd1559abce147959d349168af980702"
    speak(content)