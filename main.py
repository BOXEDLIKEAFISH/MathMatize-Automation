from PIL import ImageGrab   # take screenshots of the page
from pyautogui import click    # automated clicking
import random   # select random button to press
from time import sleep # sleep function
from tkinter import *
import threading

running = False
grey =  '#E1E1E1'   #colour and font variables
lightgrey = '#3F4E4F'
textfont = ('helvetica', 20, 'bold')

buttonColours = [(67, 160, 71), (229, 57, 53), (30, 136, 229), (253, 216, 53), (142, 36, 170)] # mathmatize poll button colours
                # green           red            blue            yellow          purple

buttonX = [700, 840, 970, 1110, 1250]   # x values for every corresponding button
buttonY = 250   # same y value for every button
submitXY = (970, 360)   # submit button location

buttonLocations = (630, 185, 1320, 310) # rectangle where all the buttons are
submittedPrompt = (910, 384, 1030, 386)

def findcolour() -> bool:
    for x in range(display.width):  # check all x
        for y in range(display.height): # check all y
            if display.getpixel((x, y)) in buttonColours:   # if buttons are on screen
                return True
    return False


def submitPoll() -> None:
    click(buttonX[random.randint(0, 4)], buttonY)   # select a random button A-E
    sleep(2)    # delay 2 sec
    click(submitXY) # click submit button


def pause():
    while True:
        submitted = False
        display = ImageGrab.grab(bbox = submittedPrompt)
        for x in range(display.width):
            for y in range(display.height):
                if display.getpixel((x, y)) == (103, 82, 91):
                    submitted = True
        if not submitted:
            return
        sleep(8)
        

def startprogram():
    while True:
        global display
        while running:
            display = ImageGrab.grab(bbox = buttonLocations)    # take screenshot of display
            if findcolour():    # if buttons are on scren
                submitPoll()    # submit answer
                pause()
            sleep(10)


def toggle():
    global running
    running = not running

    if startstop.config('relief')[-1] == 'sunken':
        startstop.config(relief="raised", text = 'Start')
        runningmessage.set('Status: Stopped')
    else:
        startstop.config(relief="sunken", text = 'Stop')
        runningmessage.set('Status: Running')


def tkinterwindow():
    global startstop
    global runningmessage
    window = Tk()
    window.title("MathMatize Bot")
    window.geometry("300x100")
    window.iconbitmap('logo.ico')

    runningmessage = StringVar()
    runningmessage.set('Status: Stopped')

    label = Label(window, textvariable=runningmessage, font=textfont, fg = 'black', width=24, height=1, anchor="w", justify="left").pack()

    startstop = Button(window, text = 'Start', height = 4, width = 30, font = 35, bg = grey, fg = 'black', activebackground = lightgrey, activeforeground = 'white', command = toggle)
    startstop.pack()

    window.mainloop()

thread1 = threading.Thread(target = startprogram)
thread2 = threading.Thread(target = tkinterwindow)
thread1.start()
thread2.start()
#85/178