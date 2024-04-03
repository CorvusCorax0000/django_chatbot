import requests
import random

def get_image():
    random_number = random.randint(0, 999)
    return f"<img src='https://picsum.photos/id/{random_number}/200/300' alt='a random image'>"

def wiki_search(message):
    word_list = message.split(" ", 3)
    subject = word_list[3]
    return f"<a href='https://en.wikipedia.org/wiki/{subject}'>Wikipedia article about {subject}</a>"

last_message = None

def reset_last_message():
    global last_message
    last_message = None

def weather(message):
    message = message.lower()
    word_list = message.split(" ", 2)
    location = word_list[2]

    base_url = "http://api.weatherapi.com/v1/forecast.json"
    api_key = "9d981aca306b4c8daaa01803240304"
    request_url = f"{base_url}?key={api_key}&q={location}&days=1&aqi=no&alerts=no"
    response = requests.request('GET', request_url)
    result = response.json()
    return f"Weather in {location.title()} is currently {int(result['current']['temp_c'])}c."

command_list = '''Gimme Image: gives a random image<br>
Tell me about SOMETHING: gives a wikipedia article about SOMETHING<br>
Weather in CITY: gives current temperature in CITY<br>
help: lists all commands I know'''

def bot_response(message):
    message = message.lower()
    global last_message
    if message == last_message:
        return "STOP REPEATING YOURSELF!"
    else:
        last_message = message
        if message == "hello":
            return "hello there human"
        elif message == "goodbye":
            return "<b>short circuit</b> executed"
        elif message == "gimme image":
            return get_image()
        elif message.startswith("tell me about"):
            return wiki_search(message)
        elif message.startswith("weather in"):
            return weather(message)
        elif message == "help":
            return command_list
        else:
            return "cannot comprehend"

