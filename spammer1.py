import PySimpleGUI as sg
import pyautogui as ag
from time import sleep
from math import pi


def main():
    spamm = Spammerbot()
    spamm.start()


def spam():
    numero_base = 1

    sleep(5)
    f = open("Rick Astley", 'r')
    while numero_base != pi:
        f.seek(0)
        numero_base += 1
        for word in f:
            ag.typewrite(word)
            ag.press('enter')


class Spammerbot:

    def start(self):
        # layout
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Spammer bot')],
            [sg.Button('Start')],
        ]
        # windows
        window = sg.Window('SpammerBot', layout=layout, size=(150, 70), element_justification='c')
        # receive values
        while True:
            events, values = window.read()
            if events == sg.WINDOW_CLOSED:
                break
            if events == 'Start':
                spam()


if __name__ == '__main__':
    main()

