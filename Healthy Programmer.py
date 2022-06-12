# a healthy programmer
"""we have to make functions for eye , exercise , and drink water"""
import time
from datetime import datetime
def eye():
    from pygame import mixer
    mixer.init()
    mixer.music.load("Alarm Bell.mp3")
    mixer.music.play()
def exercise():
    from pygame import mixer
    mixer.init()
    mixer.music.load("Alarm Bell.mp3")
    mixer.music.play()
def water():
    from pygame import mixer
    mixer.init()
    mixer.music.load("Alarm Bell.mp3")
    mixer.music.play()
def getdate():
    import datetime
    return datetime.datetime.now() #This will print "2022-04-16 18:51:12.312057"
v=getdate()
v=str(v)

if __name__ == "__main__":
    log = 20
    while(log>1):
        time.sleep(5)
        eye()
        inp4 = input("time to do eye exercise , enter 'ey done' to stop the alarm : ")
        if inp4=="ey done":
            from pygame import mixer
            mixer.init()
            mixer.music.load("Alarm Bell.mp3")
            mixer.music.stop()
            with open("Eye.txt", "a") as f:
                s = "Time:[{}] Eye:{}\n".format(v, inp4)
                f.write(s)
            log = log-1
        else:
            print(" enter a valid input! after 5 seconds. ")
        time.sleep(5)
        exercise()
        inp5 = input("time to do physical exercise , enter 'ex done' to stop the alarm : ")
        if inp5=="ex done":
            from pygame import mixer
            mixer.init()
            mixer.music.load("Alarm Bell.mp3")
            mixer.music.stop()
            with open("Physical_Exercise.txt", "a") as f:
                s = "Time:[{}] Physical_Exercise:{}\n".format(v, inp5)
                f.write(s)
            log = log-1
        else:
            print(" enter a valid input! after 5 seconds. ")      
        time.sleep(5)
        exercise()
        inp6 = input("time to drink water , enter 'dw done' to stop the alarm : ")
        if inp6=="dw done":
            from pygame import mixer
            mixer.init()
            mixer.music.load("Alarm Bell.mp3")
            mixer.music.stop()
            with open("Water.txt", "a") as f:
                s = "Time:[{}] Eye:{}\n".format(v, inp6)
                f.write(s)
            log = log-1
        else:
            print(" enter a valid input! after 5 seconds. ")# a healthy programmer
