from screeninfo import get_monitors
import pyautogui



class Mouse:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.screen = self.get_screen_size()
        self.SENSIBILITY = 5


    def move(self, x, y):
        print(x, y)
        pyautogui.moveTo(x * self.screen[0] * self.SENSIBILITY, y * self.screen[1] * self.SENSIBILITY)



    def get_screen_size(self):
        w, h = 0, 0

        for monitor in get_monitors():
            w += monitor.width
            h = monitor.height

        return (w, h)
            