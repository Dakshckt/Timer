import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import datetime
import threading
from threading import Thread
import time
import vlc

base = tk.Tk()
base.title("Clock")
base.geometry("350x500")

nb = Notebook(base)

player = vlc.MediaPlayer("./alarmSound.mp3")

def player_start():
    global player
    player.play()

def player_stop():
    global player
    player.stop()

def alarm(take_time):
    hour = int(take_time.hour)
    minute = int(take_time.minute)
    second = int(take_time.second)
    total_sec = int(((((hour * 60) + minute) * 60) + second))
    take_time = take_time.strftime("%H : %M : %S")

    target_second = 0
    while target_second < total_sec:
        total_sec -= 1
        time.sleep(1)
        # print(total_sec)
    
    result = listBox.get(0 , tk.END)
    for index , val in enumerate(result):
        if val == take_time:
            listBox.delete(index)

    sound = Thread(target=player_start)
    sound.start()
    if messagebox.showinfo("Info",f"{take_time}") == 'ok':
        player_stop()
    

def myFunc():
    hour = hr_entry.get()
    minute = min_entry.get()
    second = sec_entry.get()

    if hour == '':
        hour = 0
    else:
        hour = int(hour)

    if minute == '':
        minute = 0
    else:
        minute = int(minute)

    if second == '':
        second = 0
    else:
        second = int(second)
    
    time = datetime.time(hour , minute , second)
    listBox.insert(tk.END , time.strftime("%H : %M : %S"))
    new_thread = Thread(target=alarm , args=(time ,))
    new_thread.start()

    messagebox.showinfo("Info",f"Total timer are : {threading.active_count() - 1}")
    hr_entry.delete(0 , tk.END)
    min_entry.delete(0 , tk.END)
    sec_entry.delete(0 , tk.END)


frame1 = Frame(nb)
header = Label(frame1 , text="Timer Clock (set alarm)")
header.grid(row=0 , column=0 , columnspan=3 , pady=10)

hr_label = Label(frame1 , text="Hour")
hr_label.grid(row=1 , column=0 , pady=10 , padx=5)
min_label = Label(frame1 , text="Minutes")
min_label.grid(row=1 , column=1 , pady=10 , padx=5)
sec_label = Label(frame1 , text="Seconds")
sec_label.grid(row=1 , column=2 , pady=10 , padx=5)

hr_entry = Entry(frame1 , width=15)
hr_entry.grid(row=2 , column=0 , pady=10 , padx=5)
min_entry = Entry(frame1 , width=15)
min_entry.grid(row=2 , column=1 , pady=10 , padx=5)
sec_entry = Entry(frame1 , width=15)
sec_entry.grid(row=2 , column=2 , pady=10 , padx=5)

button = Button(frame1 , text="Set Timer" , command=lambda : myFunc())
button.grid(row=3 , column=2 , pady=10 , padx=5)

listBox = tk.Listbox(frame1 , width=30)
listBox.grid(row=4 , column=0 , columnspan=3 , padx=10 , pady=10)
frame1.pack(fill=tk.BOTH , expand=True)


nb.pack(fill=tk.BOTH , expand=True , padx=10 , pady=5)
nb.add(frame1 , text="Timer")

base.mainloop()

