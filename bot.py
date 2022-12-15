import pyscreeze
import numpy as np
from numpy import array
import scipy.ndimage
from PIL import Image
from screeninfo import get_monitors
from skimage import measure
import time
import pyautogui

def getBlobs():
    im = pyscreeze.screenshot(region=(1180,500, 200, 75))

    data = np.zeros( (75, 200, 3), dtype=np.uint8)

    highestx = 0
    highesty = 0
    highestcolor = 0

    for i in range(75):
        for j in range(200):
            pixel = im.getpixel((j, i))
            #data[i, j] = [pixel[0], pixel[1], pixel[2]]
            grayscale = (pixel[0] + pixel[1] + pixel[2])/3
            data[i, j] = [grayscale, grayscale, grayscale]

            if grayscale > highestcolor:
                highestcolor = grayscale
                highestx = i
                highesty = j

    whitepixels = 0

    for i in range(75):
        for j in range(200):
            pixel = im.getpixel((j, i))
            grayscale = (pixel[0] + pixel[1] + pixel[2])/3
            
            if grayscale == highestcolor:
                whitepixels += 1
                data[i, j] = [255, 255, 255]
            else:
                data[i, j] = [0, 0, 0]

    image = Image.fromarray(data)

    arr = array(image)

    n = measure.label(arr)

    return [n.max(), n.mean()]

def checkBattle():
    pixel = pyscreeze.pixel(100, 130)

    if pixel[0] == 51 and pixel[1] == 255 and pixel[2] == 51:
        time.sleep(1.5)
        pyautogui.click(x=1900, y=1300)
        time.sleep(5)

while True:
    info = getBlobs()
    checkBattle()
    print(info[0])
    print(info[1])

    if info[1] < 0.0001:
        pyautogui.click(button='right')
        time.sleep(0.2)

    if info[0] == 6 or info[0] == 4:
        pyautogui.click(button='right')

    

    time.sleep(0.5)