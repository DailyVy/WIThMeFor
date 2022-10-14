from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import pygame

def onClick_side_effect(a):
    """
    부작용 소리를 출력하게 해주는 클릭 리스너
    :param a: 리스너로 사용하기 때문에 딱히 사용하지 않는다
    :return: None
    """
    music_file = f"./assets/sound/bearse_side_effect.mp3"
    freq = 16000  # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
    bitsize = -16  # signed 16 bit. support 8,-8,16,-16
    channels = 1  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get right sound)
    # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.quit()


window = Tk()
app = Canvas(
    window,  # GUI 윈도우 객체 창 위에 app 올리기
    height=500,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
app.place(x=0, y=0)

key1 = tk.Button(window)
key1.place(x=0, y=0)
key1.bind("<Button-1>", onClick_side_effect)

window.resizable(False, False)  # 윈도우 크기 고정
window.mainloop()  # 시행