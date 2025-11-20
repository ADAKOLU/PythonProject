import speech_recognition as sr
import pyttsx3
import openai
import requests
import time



openai.api_key = " abcdef12345"
TASKER_URL = ""
engine = pyttsx3.init()
recognizer = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_bing(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Could not connect to Google service.")
            return ""
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            message=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"openAI request failed: {e}"
def turn_on_phone():
    try:
        requests.get(TASKER_URL, timeout=5)
        speak("Command sent to your phone.")
    except Exception as e:
        speak(f"Failed to send command: {e}")
speak("Hello! I am Emmanuel. Say 'exit' to quit.")

while True:
    command = listen()
    if command == "":
        time.sleep(0.5)
        continue
    if "exit" in command.lower():
        speak("Goodbye. See you soon.")
        break
    if "turn on phone" in command.lower():
        turn_on_phone()
        continue
    response = ask_openai(command)
    print("Assistant:", response)
    speak(response)
    time.sleep(0.5)


