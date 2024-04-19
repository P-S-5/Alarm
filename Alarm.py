from tkinter import *
import datetime
import time
# from playsound import playsound
import pygame
from threading import *
import os

win = Tk()
win.geometry("400x200")


def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, "police_siren.mp3")


def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")
            play_sound(path)
            break


win.title("Alarm Clock")
set_time = Label(win, text="Set Time", fg="#330080",
                 font=("Helvetica 15 bold")).pack(side=TOP)
hour = Label(win, text="Hour", font=("Helvetica 12")).place(x=120, y=50)
min = Label(win, text="Min", font=("Helvetica 12")).place(x=185, y=50)
sec = Label(win, text="Sec", font=("Helvetica 12")).place(x=245, y=50)

hour = StringVar(win)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23')
hour.set(hours[0])
hrs = OptionMenu(win, hour, *hours,)
hrs.configure(activebackground="#bfbfbf")
hrs.place(x=110, y=70)

minute = StringVar(win)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
minute.set(minutes[0])
mins = OptionMenu(win, minute, *minutes)
mins.configure(activebackground="#bfbfbf")
mins.place(x=172, y=70)

second = StringVar(win)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
second.set(seconds[0])
secs = OptionMenu(win, second, *seconds)
secs.configure(activebackground="#bfbfbf")
secs.place(x=234, y=70)

set_alarm = Button(win, text="Set Alarm", fg="#cc0000", activebackground="#cc0000",
                   activeforeground="#ffffff", font=("Helvetica 15 bold"), command=Threading)
set_alarm.place(x=147, y=120)

win.mainloop()

pygame.quit()
