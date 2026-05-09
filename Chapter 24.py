import pyttsx3

engine = pyttsx3.init()

engine.say('Hello world!')
engine.runAndWait()
# pyttsx3.init()
# Creates the speech engine object

# engine.say()
# Adds text to the speech queue

# engine.runAndWait()
# Runs the speech engine and waits until speaking is finished
import pyttsx3

engine = pyttsx3.init()

engine.say('Hello.')
engine.say('Welcome to Python.')
engine.say('This is text to speech.')

engine.runAndWait()

# Changing Speech Rate

import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)

engine.setProperty('rate', 125)

engine.say('This speech is slower.')
engine.runAndWait()

# Common Rates

# 200 = default on many systems
# Lower numbers = slower speech
# Higher numbers = faster speech

# Changing Volume

import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volume', 0.5)

engine.say('This volume is quieter.')
engine.runAndWait()

# Volume Range

# 0.0 = silent
# 1.0 = maximum volume

# Getting Available Voices

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
    print(voice.name)
    print(voice.languages)

# Changing Voice

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.say('This uses a different voice.')
engine.runAndWait()

# Voice Notes

# voices[0] is often male
# voices[1] is often female
# Available voices depend on your operating system

# Saving Speech to a File

import pyttsx3

engine = pyttsx3.init()

engine.save_to_file(
    'Hello from Python.',
    'speech.wav'
)

engine.runAndWait()

# save_to_file()

# Converts text into an audio file
# Common formats include .wav

# Installing Whisper

# Install with pip:
# pip install openai-whisper

# Whisper Requirements

# ffmpeg must also be installed

# Basic Speech Recognition Example

import whisper

model = whisper.load_model('base')

result = model.transcribe('speech.wav')

print(result['text'])

# Explanation

# whisper.load_model()
# Loads the AI speech recognition model

# model.transcribe()
# Converts spoken audio into text

# result['text']
# Contains the transcription

# Whisper Model Sizes

# tiny
# base
# small
# medium
# large

# Model Notes

# Smaller models:
# Faster
# Less accurate

# Larger models:
# Slower
# More accurate

# Transcribing MP3 Files

import whisper

model = whisper.load_model('base')

result = model.transcribe('audio.mp3')

print(result['text'])

# Supported Audio Formats

# mp3
# wav
# m4a
# mp4

# Practical Uses

# Audiobooks
# Accessibility tools
# Voice assistants
# Automatic subtitles
# Voice notes transcription
# Reading text files aloud

# Example - Reading a Text File Aloud

import pyttsx3

engine = pyttsx3.init()

with open('story.txt') as file:
    text = file.read()

engine.say(text)

engine.runAndWait()

# Example - Simple Voice Assistant

import pyttsx3

engine = pyttsx3.init()

command = input('Enter text: ')

engine.say(command)

engine.runAndWait()
