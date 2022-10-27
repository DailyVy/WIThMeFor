from pathlib import Path
import tkinter as tk

import PIL.Image
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import pygame
import os.path
import cv2

assets_root_path = "./assets"


class App:
    def __init__(self, _class_id=None, _img=None, _box=None, _window_size=(375, 700), _color="#FBD65C"):
        """
        App 클래스 생성 + 실행
        :param _class_id: 약 클래스 이름
        :param _window_size: 앱 크기(윈도우 크기) 변경하지 않는것을 추천
        :param _color: 앱 배경 색상
        """
        self.window = None
        self.pill_name = None
        self.color = _color
        self.window_size = _window_size
        self.cam = cv2.VideoCapture(0)
        self.header_image = None

        self.capture_img_text = None
        self.capture_img = None
        self.cap_img = None
        # self.box = _box[0]  # [x, y, w, h]
        self.box = None  # [x, y, w, h]

        self.capture_key_img = None
        self.key1_img = None
        self.key2_img = None
        self.key3_img = None

        self.window_height = _window_size[1]
        self.window_width = _window_size[0]
        self.app = None
        # self.header_init()  # 헤더 init
        # self.capture_img_init(_img=_img)  # 캡처된 이미지 init
        # self.button_init()  # 버튼 리스너 init

    def set_class_id_box(self, _class_id, _box):
        self.pill_name = _class_id[0]
        self.box = _box[0]

    def background_init(self):
        self.window = Tk()
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))  # 윈도우 베이스 틀 크기
        # self.window.geometry(f"%dx%d+%dx%d",(self.window_width, self.window_height, self.))  # 윈도우 창 열리는거 위치 고정?
        self.window.configure(bg=self.color)
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

    def gui_1(self):
        self.background_init()  # 배경 틀 설정

        img = Image.open(f"{assets_root_path}/image/capture_button.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.capture_key_img = ImageTk.PhotoImage(img)
        key = tk.Button(self.window, image=self.capture_key_img, bg=self.color)
        key.place(x=130, y=582)
        key.bind("<Button-1>", self.onClick_capture)
        self.window.resizable(False, False)  # 윈도우 크기 고정

        while self.window is not None and self.cam.isOpened():
            ret, img = self.cam.read()
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img_copy = img.copy()
            self.capture_img = img
            img_copy = cv2.resize(img_copy, dsize=(318, 390))
            img_copy = ImageTk.PhotoImage(image=PIL.Image.fromarray(img_copy))
            self.app.create_image(
                187.0, 380.0,
                image=img_copy
            )
            self.window.update()

    def gui_2(self):
        self.background_init()

        # 헤더 이미지 설정 ====================================================================================
        img = Image.open(f"{assets_root_path}/image/해더.png")
        img = img.resize((385, 70), Image.ANTIALIAS)  # 크기는 조정하지 않는것을 추천 이미 알맞게 설정되어있음
        self.header_image = ImageTk.PhotoImage(img)  # 클래스 맴버변수로 사용해야지 이미지가 나온다 참 이상하다
        self.app.create_image(
            187.0, 30.0,
            image=self.header_image
        )
        # 촬영된 이미지 띄우기 ========
        self.app.create_rectangle(
            28.0,
            92.0,
            347.0,
            573.0,
            fill="#FFFFFF",
            outline="")

        # if os.path.exists(f"{assets_root_path}/image/{self.pill_name}.png"):
        img = self.capture_img.copy()
        # else:
        #     img = Image.open(f"{assets_root_path}/image/not_find_image.png")

        # img = img.resize((319, 481), Image.ANTIALIAS) # ndarray로 넘어오기 때문에 해당 코드는 사용하지 못함 ㅋㅋ루삥뽕
        # original code
        img = cv2.resize(img, dsize=(318, 390))
        # test_code 
        # img = self.__capture_img_make_standard()
        # img = self.__capture_img_make_standard_test()
        # =========
        print(img.shape)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.capture_img = ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
        self.app.create_image(
            187.0, 380.0,
            image=self.capture_img
        )
        # 기존 187.0, 332.0c

        # 약 종류에 따른 말풍선 이미지 
        img = Image.open(f"{assets_root_path}/image/{self.pill_name}_text.png")
        img = img.resize((318, 100), Image.ANTIALIAS)
        self.capture_img_text = ImageTk.PhotoImage(img)
        self.app.create_image(
            188.0, 140.0,
            image=self.capture_img_text
        )

        # 버튼 셋팅 ==========================================================================================
        img = Image.open(f"{assets_root_path}/image/복용법.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key1_img = ImageTk.PhotoImage(img)
        key1 = tk.Button(self.window, image=self.key1_img, bg=self.color)
        key1.place(x=15, y=582)
        key1.bind("<Button-1>", self.onClick_Dosage)

        img = Image.open(f"{assets_root_path}/image/부작용.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key2_img = ImageTk.PhotoImage(img)
        key2 = tk.Button(self.window, image=self.key2_img, bg=self.color)
        key2.place(x=130, y=582)
        key2.bind("<Button-1>", self.onClick_side_effect)
        # key2.bind("<Button-1>", self.onClick_Dosage)

        img = Image.open(f"{assets_root_path}/image/재촬영.png")
        img = img.resize((105, 105), Image.ANTIALIAS)
        self.key3_img = ImageTk.PhotoImage(img)
        key3 = tk.Button(self.window, image=self.key3_img, bg=self.color)
        key3.place(x=245, y=582)
        key3.bind("<Button-1>", self.onClick_close(a=0))

        self.window.resizable(False, False)  # 윈도우 크기 고정
        self.window.mainloop()  # 시행




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

    def onClick_capture(self, a):
        """
        사진 촬영 버튼
        :param a: 리스너로 사용하기 때문에 딱히 사용하지 않는다
        :return: None
        """
        print("찰칵")
        cv2.imwrite("img/img.png", self.cam.read()[1])
        self.window.destroy()
        self.window = None


    def __capture_img_make_standard_test(self):
        """
        약 부분만 예쁘게 잘라내기(포기)
        :return:
        """
        print("[info] use __capture_img_make_standard_test()")
        standard_h = 390
        standard_w = 318
        x = self.box[0]
        y = self.box[1]
        w = self.box[2]
        h = self.box[3]
        print(f"x={x},y={y},w={w}, h={h}, x2(x+w)={x + w},y2(y+h)={y + h}")

        box_mid_h = y + (h // 2)
        box_mid_w = x + (w // 2)
        print(f"mid_h={box_mid_h}, mid_w={box_mid_w}")

        img = self.capture_img.copy()
        print(img.shape)
        # 아몰랑 알아서 짜 ㅋ  =========================================
        # ㅋㅋㄹ삥뽕

        half_h = standard_h // 2
        half_w = standard_w // 2
        top, bottom, left, right = 0, 0, 0, 0
        h_w_ratio = 1.126

        if h > standard_h and w > standard_w:
            if h > w:
                pass

            elif w < w:
                pass
            else:
                pass

        elif h > standard_h:
            pass
        elif w > standard_w:
            pass

        img = img[top:bottom, left:right, :]
        print(f"left={left}")
        print(f"right={right}")
        print(f"top={top}")
        print(f"bottom={bottom}")
        # ============================================================
        return img