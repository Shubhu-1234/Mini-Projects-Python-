# Healthy Programmer
import time
import pygame
from pygame import mixer
start_time=time.time()

def songs():
    from pygame import mixer
    mixer.init()  # Instantiate mixer
    mixer.music.load('Alarm Bell.mp3')  # Load audio file
    print("music started playing....")
    mixer.music.set_volume(0.2)  # Load audio file
    mixer.music.play(-1)  # Play the music

def getdate():
    from datetime import datetime
    now = datetime.now()
    #print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 24-hour format
    now.strftime('%Y/%m/%d %I:%M:%S %p')  # 12-hour format
    return now.strftime('%d/%m/%Y %I:%M:%S %p')   #This will print "16/06/2022 08:50:57 PM"
v=getdate()
v=str(v)

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    if elapsed_time > 5:
        songs()
        print("Enter Done to stop the song")
        x = str(input())
        if x == "Done":
            mixer.music.stop()
            print("music is stopped....")
            with open("Water.txt", "a") as f:
                s = f"Time:[{v}] You have drank Water\n"
                f.write(s)
            break

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    if elapsed_time > 15:
        songs()
        print("Enter Done to stop the song")
        x = str(input())
        if x == "Done":
            mixer.music.stop()
            print("music is stopped....")
            with open("Eye.txt", "a") as f:
                s = f"Time:[{v}] You have performed Eye Exercise.\n"
                f.write(s)
            break

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    if elapsed_time > 25:
        songs()
        print("Enter Done to stop the song")
        x = str(input())
        if x == "Done":
            mixer.music.stop()
            print("music is stopped....")
            with open("Physical_Exercise.txt", "a") as f:
                s = f"Time:[{v}] You have done Physical Exercise\n"
                f.write(s)
            break
