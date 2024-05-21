from flask import Flask
from flask import request
import pygame

app = Flask("server")
pygame.init()
sounds = [pygame.mixer.Sound('music/file1.wav'), pygame.mixer.Sound('music/file2.wav'), pygame.mixer.Sound('music/file3.wav'), pygame.mixer.Sound('music/file4.wav')]

currently_playing_sound = None

def stop_playing():
  global currently_playing_sound
  if currently_playing_sound:
    currently_playing_sound.stop()
    currently_playing_sound = None

@app.route("/call/<call_id>", methods = ['GET'])
def call(call_id):
    if request.method == 'GET':
        stop_playing()
        match call_id:
          case "0":
            currently_playing_sound = pygame.mixer.Sound('music/file1.wav')
            currently_playing_sound.play()
            print("LOG LEVEL 0: PLUSHIE SAYS: YOU ARE MY BEST FRIEND")
            return "called 0"
          case "1":
            currently_playing_sound = pygame.mixer.Sound('music/file2.wav')
            currently_playing_sound.play()
            print("LOG LEVEL 0: PLUSHIE SAYS: YOU ARE THE BEST SEAL IN THE WORLD")
            return "called 1"
          case "2":
            currently_playing_sound = pygame.mixer.Sound('music/file3.wav')
            currently_playing_sound.play()
            print("LOG LEVEL 0: PLUSHIE SAYS: I LOVE TO PLAY WITH YOU")
            return "called 2"
          case "3":
            currently_playing_sound = pygame.mixer.Sound('music/file4.wav')
            currently_playing_sound.play()
            print("LOG LEVEL 0: PLUSHIE SAYS: LETS BE FRIENDS FOREVER")
            return "called 3"
          case _:
            return call_id
    else:
      return "Method does not exist/Use GET method"
  
app.run()