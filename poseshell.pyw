import tkinter as tk
from tkinter import ttk
import keyboard
import time
import pygetwindow as gw

def saiNew():
    keyboard.press_and_release("windows+2")
    time.sleep(0.2)
    keyboard.press_and_release("ctrl+n")
    time.sleep(0.2)
    keyboard.press_and_release("enter")

def saiSave():
    global posenum
    Saiwindow=gw.getWindowsWithTitle("SAI")[0]
    Saiwindow.activate()
    keyboard.press_and_release("ctrl+w")
    time.sleep(0.2)
    keyboard.press_and_release('enter')
    time.sleep(0.2)
    keyboard.press_and_release('tab')
    time.sleep(0.2)
    keyboard.press_and_release('ctrl+a')
    time.sleep(0.2)
    keyboard.write("C:\\Users\\14491\\Desktop\\#\\#15-18\\")
    time.sleep(0.2)
    keyboard.press_and_release('enter')
    time.sleep(0.2)
    keyboard.press_and_release('tab')
    for i in range(int(posenum)-1):
        keyboard.press_and_release('ctrl+w')
        time.sleep(0.2)
        keyboard.press_and_release("enter")
        time.sleep(0.2)
        date=time.ctime()
        date=date.replace(':',"")
        keyboard.write(date+' sketch '+str(i+1))
        keyboard.press_and_release("enter")

def go(*args):
    global posenum
    posenum=combox.get()

posenum=10
win=tk.Tk()
Button=ttk.Button(win,text='New',command=saiNew)
Button.pack()
Button2=ttk.Button(win,text='Save',command=saiSave)
Button2.pack()
combox=ttk.Combobox(win,textvariable='Num')
combox['values']=('10','20','30','40','50','60','70','80','90','100')
combox.bind('<<ComboboxSelected>>',go)
combox.pack()
Quit=ttk.Button(win,text='Quit',command=win.quit)
Quit.pack()
win.geometry('38x102+1000+100')
win.overrideredirect(True)
win.wm_attributes('-topmost',1)
win.mainloop()