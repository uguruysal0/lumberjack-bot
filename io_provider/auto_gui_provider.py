from io_provider import IoProvider
import pyautogui
import time
import numpy as np
from utils.util import execution_time

class AutoGuiProvider(IoProvider):

    @execution_time("AutoGuiProvider.get_screenshot")
    def get_screenshot(self):
        # TODO, find the region coordinates for pyautogui provider 
        im = pyautogui.screenshot(region=(0,0, 300, 400))
        return np.array(im)

    @execution_time("AutoGuiProvider.hit_key")
    def hit_key(self, key, sleep_time):
        pyautogui.keyDown(key)
        time.sleep(sleep_time)
        pyautogui.keyUp(key)

