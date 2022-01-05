import time
import mss
import mss.tools
import numpy as np
from io_provider.io_provider import IoProvider
from utils.util import execution_time

from pynput.keyboard import Key, Controller


class FastProvider(IoProvider):
    """
    Combining 2 different packages, both of them faster than py_autogui package 
    """

    def __init__(self) -> None:
        super().__init__()
        self.keyboard = Controller()

    @execution_time("FastProvider.get_screenshot")
    def get_screenshot(self):
        """ 
        Method returns the screen shot of given region, returns np array
        """
        with mss.mss() as sct:
            region = {'top': 150, 'left': 870, 'width': 350, 'height': 500}
            sct_img = sct.grab(region)
            return np.array(sct_img)

    @execution_time("FastProvider.hit_key")
    def hit_key(self, key, sleep_time):
        start_time = time.time()
        if key == "left":
            self.keyboard.press(Key.left)
            self.keyboard.release(Key.left)
        else:
            self.keyboard.press(Key.right)
            self.keyboard.release(Key.right)
        time.sleep(sleep_time)
        print("BUTTON HIT new api --- %s seconds ---" %
              (time.time() - start_time))
