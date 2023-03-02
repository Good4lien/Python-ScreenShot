import os
from PIL import ImageGrab
from datetime import datetime
from pynput import keyboard

def on_press(key):
    if key.__str__()=='Key.print_screen' or key.__str__()=='Key.ctrl_l':
        date = datetime.now().__str__().split(' ')
        time = date[1].replace(':', "'").replace(".", "-")
        path = 'screens/%s/' % date[0]
        name = path + time
        print(name)

        if not ('screens' in os.listdir(path=".")):
            os.mkdir('screens')

        if not (date[0] in os.listdir(path='screens')):
            os.mkdir(path)

        img = ImageGrab.grab()
        img.save("%s.jpg" % name, "JPEG")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
