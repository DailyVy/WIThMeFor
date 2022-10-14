import gui

if __name__ == '__main__':
    pill_name = ["bearse", "brufen", "drbearse", "festalPlus", "pancol-A", "panpyrinT", "tyrenol"]
    for name in pill_name:
        app = gui.App(name)
        app = None
        # app = gui.App(_class_id=name, _img=capture_droid_cam_image)
