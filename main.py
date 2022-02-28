import time
from playsound import playsound

def pomtimer(name,length):
    print(name,' starting')
    start =time.time()
    timeleft=10
    prevsec=1
    period=length
    while timeleft>0:
        time.sleep(0.1)
        timeleft = round(start+period-time.time())
        if timeleft!=prevsec:
            timothy=divmod(timeleft,60)
            print(name,'-   ',timothy[0],':',timothy[1])
            prevsec = timeleft
            if name == 'Break' and timeleft ==40:
                playsound('/home/yellowboots/Documents/birdsong.mp3')
    playsound('/home/yellowboots/Documents/rooster-call-sound.mp3')


def custom():
    print('how many Pomodoros do you want to do?')
    total = int(input())
    playsound('/home/yellowboots/Documents/rooster-call-sound.mp3')
    for i in range(total):
        pomtimer('Pomodoro', 25 * 60)
        if i == total -1:
            break
        if(divmod(i+1,4)[1]==0):
            pomtimer('Break', 15 * 60)
        else:
            pomtimer('Break', 5 * 60)

def base_six():
    print('do you want full or half Pomodoros? (f/h)')
    response = input()
    if response == 'f':
        response = 40
    else:
        response = 20
    print('how many Pomodoros do you want to do?')
    total = int(input())
    playsound('/home/yellowboots/Documents/rooster-call-sound.mp3')
    for i in range(total):
        pomtimer('Pomodoro', response * 50)
        if i == total - 1:
            break
        if (divmod(i + 1, 4)[1] == 0):
            pomtimer('Break', response * 30)
        else:
            pomtimer('Break', response * 10)

#custom()
base_six()