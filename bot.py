import cv2 as cv
import numpy as np
import time 
from utils.util import execution_time

template = cv.imread('utils/template.png', cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

def insert_to_moves(moves, next_point, key):
    if len(moves) != 0 and abs(moves[-1][1]-next_point) <= 50:
        return moves
    moves.append((key, next_point))
    return moves

def create_moves_array(l, r):
    """
    Merge 2 sorted list in to one list,
    """
    moves = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        l_point = l[i]
        r_point = r[j]
        if l_point > r_point:
            moves = insert_to_moves(moves, l_point, "right")
            i+=1
        else:
            moves = insert_to_moves(moves, r_point, "left")
            j+=1
    
    while i < len(l):
        l_point = l[i]
        moves = insert_to_moves(moves, l_point, "right")
        i+=1
    
    while j < len(r):
        r_point = r[j]
        moves = insert_to_moves(moves, r_point, "left")
        j+=1
    
    return moves

def do_the_thing(img):
    global template, w,h
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img_gray = cv.Canny(img_gray, 100, 200)
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.165
    loc = np.where(res >= threshold)
    left_pts = []
    right_pts = []
    for pt in zip(*loc[::-1]):
        if pt[1] > 950:
            continue
        if pt[0] < 300:
            left_pts.append(pt[1])
        else:
            right_pts.append(pt[1])

    left_pts = list(set(left_pts))
    left_pts.sort(reverse=True)
    right_pts = list(set(right_pts))
    right_pts.sort(reverse=True)
    moves = create_moves_array(left_pts, right_pts)
    return moves

class LumberjackBot:
    def __init__(self, io_provider, key_delay, screenshot_delay) -> None:
        self.io_provider = io_provider
        self.key_delay = key_delay
        self.screenshot_delay = screenshot_delay

    def play(self):
        self.io_provider.hit_key("left", self.key_delay)
        self.io_provider.hit_key("left", self.key_delay)
        
        # TODO handle the case when game ends
        while True:
            im = self.io_provider.get_screenshot()
            moves = self.get_moves(im)
            
            for m in moves:
                self.io_provider.hit_key(m[0], self.key_delay)
                self.io_provider.hit_key(m[0], self.key_delay)
            
            time.sleep(0.02)

    @execution_time("Bot.get_moves")
    def get_moves(self, screen_shot_img):
        return do_the_thing(screen_shot_img)