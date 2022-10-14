from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import pygame
import os.path

assets_root_path = "./assets"


class App:
    def __init__(self, _class_id=None, _img=None, _window_size=(375, 700), _color="#FBD65C"):
        """
        App 클래스 생성 + 실행
        :param _class_id: 약 클래스 이름
        :param _window_size: 앱 크기(윈도우 크기) 변경하지 않는것을 추천
        :param _color: 앱 배경 색상
        """

        self.pill_name = _class_id  #
        self.color = _color

        self.header_image = None

        self.capture_img_text = None
        self.capture_img = None

        self.key1_img = None
        self.key2_img = None
        self.key3_img = None

        self.window = Tk()
        self.window_height = _window_size[1]
        self.window_width = _window_size[0]
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))  # 윈도우 베이스 틀 크기
        self.window.configure(bg=_color)

        self.app = Canvas(
            self.window,  # GUI 윈도우 객체 창 위에 app 올리기
            bg=self.color,  # 노란색
            height=self.window_height,
            width=self.window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.app.place(x=0, y=0)

        self.header_init()          # 헤더 init
        self.capture_img_init(_img=_img)     # 캡처된 이미지 init
        self.button_init()          # 버튼 리스너 init
        
        # 실행
        self.window.resizable(False, False) # 윈도우 크기 고정
        self.window.mainloop()  # 시행

    # def head_init(self):
    #     self.app.create_rectangle(
    #         0.0,
    #         0.0,
    #         375.0,
    #         72.0,
    #         fill="#513A2D",
    #         outline="")
    #
    #     self.app.create_rectangle(
    #         28.0,
    #         12.0,
    #         77.0,
    #         56.0,
    #         fill="#FFFFFF",
    #         outline="")
    #
    #     img = Image.open("./image/logo.gif")
    #     img = img.resize((49, 44), Image.ANTIALIAS)
    #     # img.show()  # 이거 입력해야 이미지 뜨는건 뭐임?
    #     self.logo = ImageTk.PhotoImage(img)
    #     self.app.create_image(
    #         52.0,
    #         36.0,
    #         image=self.logo
    #     )
    #
    #     self.app.create_text(
    #         82.0,
    #         25.0,
    #         anchor="nw",
    #         text="이거모약",
    #         fill="#FFFFFF",
    #         font=("Inter", 30 * -1)
    #     )
    #
    #     self.app.create_text(
    #         205.0,
    #         37.0,
    #         anchor="nw",
    #         text="님 환영합니다",
    #         fill="#FFFFFF",
    #         font=("Inter", 16 * -1)
    #     )

    def header_init(self, _img=None):
        """
        위에 헤더부분 설정
        :return: 
        """
        img = Image.open(f"{assets_root_path}/image/해더.png")
        img = img.resize((385, 70), Image.ANTIALIAS)  # 크기는 조정하지 않는것을 추천 이미 알맞게 설정되어있음
        self.header_image = ImageTk.PhotoImage(img)  # 클래스 맴버변수로 사용해야지 이미지가 나온다 참 이상하다
        self.app.create_image(
            187.0, 30.0,
            image=self.header_image
        )

    def capture_img_init(self, _img=None):
        """
        촬영된 사진 띄우기
        :return: None
        """
        # 촬영된 이미지 띄우기 ============================================================
        self.app.create_rectangle(
            28.0,
            92.0,
            347.0,
            573.0,
            fill="#FFFFFF",
            outline="")

        if os.path.exists(f"{assets_root_path}/image/{self.pill_name}.png"):
            img = Image.open(f"{assets_root_path}/image/{self.pill_name}.png")
        else:
            img = Image.open(f"{assets_root_path}/image/not_find_image.png")
        img = img.resize((319, 481), Image.ANTIALIAS)
        self.capture_img = ImageTk.PhotoImage(img)
        self.app.create_image(
            187.0, 332.0,
            image=self.capture_img
        )

        # 약 종류에 따른 말풍선 이미지 =========================================================================
        # TODO: 투명도 설정을 못함 이미지 자체를 투명도를 조정해서 저장 해야 할 것으로 보임
        img = Image.open(f"{assets_root_path}/image/{self.pill_name}_text.png")
        img = img.resize((300, 120), Image.ANTIALIAS)
        self.capture_img_text = ImageTk.PhotoImage(img)
        self.app.create_image(
            185.0, 160.0,
            image=self.capture_img_text
        )

    # def pill_Explanation_speech_bubble(self, _text="판콜에이 입니다. \n감기에 걸리셨나요?"):
    #     """
    #     말풍선 + 안에 텍스트 추가
    #     :param _text: 말풍선 안에 넣고 싶은 문장
    #     :return: None
    #     """
    #     self.round_rectangle(45, 105, 330, 198, fill="#000015", outline="")  # 둥근 네모 그리기
    #
    #     # 텍스트
    #     self.app.create_text(
    #         77.0,
    #         130.0,
    #         anchor="nw",
    #         text=_text,  # 대사
    #         fill="#FFFFFF",
    #         font=("Inter", 20 * -1)
    #     )
    #
    #     # 말풍선 삼각형 꼭따리
    #     self.app.create_polygon(
    #         253, 195,
    #         273, 215,
    #         293, 195,
    #         fill="#000000",
    #         outline="")

    def button_init(self):
        """
        버튼 이미지와 리스너 설정
        :return: None
        """
        # key1(복용법 버튼) ====================================================================================
        # key1 = self.round_rectangle(16, 582, 125, 691, fill="#50392D", outline="")
        # self.app.create_text(
        #     26.0,
        #     621.0,
        #     anchor="nw",
        #     text="복용법",
        #     fill="#FFFFFF",
        #     font=("Inter", 30 * -1)
        # )
        # self.app.tag_bind(key1, "<Button-1>", self.onClick_Dosage)

        img = Image.open(f"{assets_root_path}/image/복용법.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key1_img = ImageTk.PhotoImage(img)
        key1 = tk.Button(self.window, image=self.key1_img, bg=self.color)
        key1.place(x=15, y=582)
        key1.bind("<Button-1>", self.onClick_Dosage)

        # key2(부작용 버튼) ====================================================================================
        # key2 = self.round_rectangle(133, 582, 242, 691, fill="#50392D", outline="")
        # self.app.create_text(
        #     144.0,
        #     621.0,
        #     anchor="nw",
        #     text="부작용",
        #     fill="#FFFFFF",
        #     font=("Inter", 30 * -1)
        # )
        # self.app.tag_bind(key2, "<Button-1>", self.onClick_side_effect)

        img = Image.open(f"{assets_root_path}/image/부작용.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key2_img = ImageTk.PhotoImage(img)
        key2 = tk.Button(self.window, image=self.key2_img, bg=self.color)
        key2.place(x=130, y=582)
        key2.bind("<Button-1>", self.onClick_side_effect)
        # key2.bind("<Button-1>", self.onClick_Dosage)

        # key3(재촬영 버튼) ====================================================================================
        # key3 = self.round_rectangle(250, 582, 359, 691, fill="#50392D", outline="")
        # self.app.create_text(
        #     263.0,
        #     621.0,
        #     anchor="nw",
        #     text="재촬영",
        #     fill="#FFFFFF",
        #     font=("Inter", 30 * -1)
        # )
        # self.app.tag_bind(key3, "<Button-1>", self.onClick_close)

        img = Image.open(f"{assets_root_path}/image/재촬영.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key3_img = ImageTk.PhotoImage(img)
        key3 = tk.Button(self.window, image=self.key3_img, bg=self.color)
        key3.place(x=245, y=582)
        key3.bind("<Button-1>", self.onClick_close)

    def onClick_Dosage(self, a):
        """
        복용법 소리를 출력하기 위한 클릭 리스너
        :param a: 리스너로 사용하기 때문에 딱히 사용하지 않는다
        :return: None
        """
        music_file = f"{assets_root_path}/sound/{self.pill_name}.mp3"  # mp3 or mid file
        print(music_file)
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

    def onClick_side_effect(self, a):
        """
        부작용 소리를 출력하게 해주는 클릭 리스너
        :param a: 리스너로 사용하기 때문에 딱히 사용하지 않는다
        :return: None
        """
        music_file = f"{assets_root_path}/sound/{self.pill_name}_side_effect.mp3"
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

    def onClick_close(self, a):
        """
        윈도우 창 닫기
        :param a: 리스너로 사용하기 때문에 딱히 사용하지 않는다
        :return: None
        """
        self.window.destroy()
        self.window = None

    # def round_rectangle(self, x1, y1, x2, y2, r=25, **kwargs):
    #     """
    #     테두리가 둥근 네모 그리기
    #     :param x1: x1
    #     :param y1: y1
    #     :param x2: x2
    #     :param y2: y2
    #     :param r:  ??
    #     :param kwargs: Canvas.create_polygon()에서 사용할 수 있는 추가 파라미터
    #     :return: None
    #     """
    #     points = (
    #         x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1,
    #         x2, y1, x2, y1 + r, x2, y1 + r, x2, y2 - r, x2,
    #         y2 - r, x2, y2, x2 - r, y2, x2 - r, y2, x1 + r,
    #         y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r,
    #         x1, y1 + r, x1, y1 + r, x1, y1)
    #     return self.app.create_polygon(points, **kwargs, smooth=True)
