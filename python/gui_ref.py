# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()


# 사각형 박스 테두리 라운딩해주는 함수
def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    points = (
    x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2, y2 - r, x2, y2,
    x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)


# 버튼 클릭 이벤트 핸들러
def onClick(a):
    # music_file = "C:/Users/AI-00/PycharmProjects/Tkinter-Designer-master/sound/pancolA.mp3"  # mp3 or mid file
    music_file = "./sound/pancolA.mp3"  # mp3 or mid file
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


window.geometry("375x700")
window.configure(bg="#FBD65C")

canvas = Canvas(
    window,
    bg="#FBD65C",
    height=700,
    width=375,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    28.0,
    92.0,
    347.0,
    573.0,
    fill="#FFFFFF",
    outline="")
img = (Image.open("./image/pancol-A.gif"))
img = img.resize((319, 481), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
canvas.create_image(
    187.0,
    332.0,
    image=img
)

# canvas.create_rectangle(
#     45.0,
#     105.0,
#     330.0,
#     198.0,
#     fill="#000000",
#     outline="")
# window.attributes('-alpha', 0.6)
round_rectangle(45, 105, 330, 198, fill="#000015", outline="")

canvas.create_text(
    77.0,
    130.0,
    anchor="nw",
    text="판콜에이 입니다. \n감기에 걸리셨나요?",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_polygon(
    253, 195,
    273, 215,
    293, 195,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    375.0,
    72.0,
    fill="#513A2D",
    outline="")

canvas.create_rectangle(
    28.0,
    12.0,
    77.0,
    56.0,
    fill="#FFFFFF",
    outline="")

img2 = (Image.open("./image/logo.gif"))
img2 = img2.resize((49, 44), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
canvas.create_image(
    52.0,
    36.0,
    image=img2
)

# canvas.create_rectangle(
#     16.0,
#     582.0,
#     125.0,
#     691.0,
#     fill="#50392D",
#     outline="")
key = round_rectangle(16, 582, 125, 691, fill="#50392D", outline="")
canvas.tag_bind(key, "<Button-1>", onClick)
canvas.pack()
# btn = Button(window, text="복용법", command=onClick, width=14, height=6)
# btn.place(x=16, y=582)

# canvas.create_rectangle(
#     250.0,
#     582.0,
#     359.0,
#     691.0,
#     fill="#50392D",
#     outline="")
round_rectangle(250, 582, 359, 691, fill="#50392D", outline="")

# canvas.create_rectangle(
#     133.0,
#     582.0,
#     242.0,
#     691.0,
#     fill="#50392D",
#     outline="")
round_rectangle(133, 582, 242, 691, fill="#50392D", outline="")

canvas.create_text(
    26.0,
    621.0,
    anchor="nw",
    text="복용법",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

canvas.create_text(
    82.0,
    25.0,
    anchor="nw",
    text="이거모약",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

canvas.create_text(
    205.0,
    37.0,
    anchor="nw",
    text="님 환영합니다",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    263.0,
    621.0,
    anchor="nw",
    text="재촬영",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

canvas.create_text(
    144.0,
    621.0,
    anchor="nw",
    text="부작용",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

window.resizable(False, False)
window.mainloop()
