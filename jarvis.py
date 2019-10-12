import pyttsx3
import webbrowser
import smptlib
import random
import speech_recognition as sr
import os
import sys

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voices', voices[len(voices) - 1].id)


def speak(audio):
	print('Computer: ' + audio)
	engine.say(audio)
	engine.runAndWayt()


def greet_me():
	currentHour = int(datetimer.datetime.now().hour)
	if currentHour >= 0 and currentHour < 12:
		speak('Good Morning!')

	if currentHour >= 12 and currentHour < 18:
		speak('Good Afternoon!')

	if currentHour >= 18 and currentHour != 0:
		speak('Good Evening!')


def my_command():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		recognizer.pause_threshold = 1
		audio = recognizer.listen(source)
	try:
		query = recognizer.recognize_google(audio, language = 'en-in')
		print('User' + query + '\n')
	except sr.UnknownValueError:
		speak('Sorry sir! I didn\'t get that! Try typing the command!')
		query = str(input('Command: '))
	return query


if __name__ == '__main__':
	while True:
		greet_me()
		speak('Hello Sir, I am your digital assistant Jarvis!')
		speak('How may I help you?')

		query = my_command()
		query = query.lower()

		if 'open youtube' in query:
			speak('okay')
			webbrowser.open('www.youtube.com')
		elif 'open google' in query:
			speak('okay')
			webbrowser.open('www.google.com')
		elif 'open gmail' in query:
			speak('okay')
			webbrowser.open('www.gmail.com')
		elif 'bye' in query or 'abort' in query or 'stop' in query:
			speak('Okay')
			speak('Bye Sir, have a good day.')
			sys.exit()
		elif 'hello' in query:
			speak('Hello Sir')
		speak('Next command! Sir!')














