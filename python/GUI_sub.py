from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import pygame


class App:
    def __init__(self, _img=Image.open("./image/pancol-A.gif"), _class_id=None, _window_size=(375, 700), _color="#FBD65C"):
        """
        init
        :param _img: 모델에서 나온 이미지

        :param _window_size:
        :param _color:
        """
        self.img = None
        self._window_height = _window_size[1]
        self._window_width = _window_size[0]
        self._color = _color
        self.logo = None    # 로고
        self.img = _img     # 이미지
        self.class_id = _class_id

        self.window = Tk()
        # self.window = Toplevel()
        print("self.window = Tk()")
        # self.window = Toplevel()
        self.window.geometry(str(self._window_width) + "x" + str(self._window_height))  # 윈도우 베이스 틀 크기
        self.window.configure(bg="#FBD65C")

        self.app = Canvas(
            self.window,  # GUI 윈도우 객체 창 위에 app 올리기
            bg=self._color,  # 노란색
            height=self._window_height,
            width=self._window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.app.place(x=0, y=0)
        self.head_init()
        self.img_init()
        self.button_init()
        self.running = True

    def head_init(self):
        self.app.create_rectangle(
            0.0,
            0.0,
            375.0,
            72.0,
            fill="#513A2D",
            outline="")

        self.app.create_rectangle(
            28.0,
            12.0,
            77.0,
            56.0,
            fill="#FFFFFF",
            outline="")

        img = Image.open("./image/logo.gif")
        img = img.resize((49, 44), Image.ANTIALIAS)
        # img.show()  # 이거 입력해야 이미지 뜨는건 뭐임?
        self.logo = ImageTk.PhotoImage(img)
        self.app.create_image(
            52.0,
            36.0,
            image=self.logo
        )

        self.app.create_text(
            82.0,
            25.0,
            anchor="nw",
            text="이거모약",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        self.app.create_text(
            205.0,
            37.0,
            anchor="nw",
            text="님 환영합니다",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

    def img_init(self):
        """
        촬영된 사진 띄우기
        :return: None
        """
        self.app.create_rectangle(
            28.0,
            92.0,
            347.0,
            573.0,
            fill="#FFFFFF",
            outline="")
        # _img.show() # 이거 해야 이미지 뜨는 이유는?
        self.img = self.img.resize((319, 481), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.app.create_image(
            187.0, 332.0,
            image=self.img
        )

        self.pill_Explanation_speech_bubble()

    def pill_Explanation_speech_bubble(self, _text="판콜에이 입니다. \n감기에 걸리셨나요?"):
        """
        말풍선 + 안에 텍스트 추가
        :param _text: 말풍선 안에 넣고 싶은 문장
        :return: None
        """
        self.round_rectangle(45, 105, 330, 198, fill="#000015", outline="")  # 둥근 네모 그리기

        # 텍스트
        self.app.create_text(
            77.0,
            130.0,
            anchor="nw",
            text=_text,  # 대사
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        # 말풍선 삼각형 꼭따리
        self.app.create_polygon(
            253, 195,
            273, 215,
            293, 195,
            fill="#000000",
            outline="")

    def button_init(self):
        key1 = self.round_rectangle(16, 582, 125, 691, fill="#50392D", outline="")
        self.app.create_text(
            26.0,
            621.0,
            anchor="nw",
            text="복용법",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )
        self.app.tag_bind(key1, "<Button-1>", self.onClick_Dosage)
        # key1 = Button(self.window, text="복용법", command=self.onClick_Dosage,
        #               image=tk.PhotoImage(file="./image/복용법.png"),
        #               width=14, height=6)
        # key1.place(x=16, y=582)
        # key1.pack()

        key2 = self.round_rectangle(133, 582, 242, 691, fill="#50392D", outline="")
        self.app.create_text(
            144.0,
            621.0,
            anchor="nw",
            text="부작용",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )
        self.app.tag_bind(key2, "<Button-1>", self.onClick_side_effect)

        key3 = self.round_rectangle(250, 582, 359, 691, fill="#50392D", outline="")
        self.app.create_text(
            263.0,
            621.0,
            anchor="nw",
            text="재촬영",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )
        self.app.tag_bind(key3, "<Button-1>", self.onClick_close)

    def close_window(self):
        self.running = False
        self.app.destroy()
        print("Window closed")

    @staticmethod
    def onClick_Dosage(a):
        music_file = "./sound/pancol-A.mp3"  # mp3 or mid file
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

    @staticmethod
    def onClick_side_effect(a):
        music_file = "./sound/bearse.mp3"  # mp3 or mid file
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

    @staticmethod
    def onClick_close(a):
        app.close_window()

    def round_rectangle(self, x1, y1, x2, y2, r=25, **kwargs):
        """
        테두리가 둥근 네모 그리기
        :param x1: x1
        :param y1: y1
        :param x2: x2
        :param y2: y2
        :param r:  ??
        :param kwargs: Canvas.create_polygon()에서 사용할 수 있는 추가 파라미터
        :return: None
        """
        points = (
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1,
            x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2,
            y2 - r, x2, y2, x2 - r, y2, x2 - r, y2, x1 + r,
            y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r,
            x1, y1 + r, x1, y1 + r, x1, y1)
        return self.app.create_polygon(points, **kwargs, smooth=True)


app = App()  # 윈두우 창에다가 app 올리기

# app.window.resizable(False, False)
# app.window.mainloop()

app.window.resizable(False, False)  # 윈도우 창 사이즈 고정

while app.running:
    # print("update")
    app.window.update()
