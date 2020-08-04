import keyboard
import numpy as np
import cv2
from mss import mss
from PIL import Image
from datetime import datetime
import pandas as pd

class DataGenerator:
    mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    sct = mss()

    @classmethod
    def generate(cls):
        mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
        sct = mss()

        while True:
            ssct_img = sct.grab(mon)

            image_data = np.array(ssct_img)
            cv2.imshow('screen', np.array(image_data))

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            
            key_presses = (keyboard.is_pressed('w'), keyboard.is_pressed('a'), \
                        keyboard.is_pressed('s'), keyboard.is_pressed('d'), \
                        keyboard.is_pressed('['), keyboard.is_pressed(']'))
            
            time = str(datetime.now())
            print(str(time))
            cv2.imwrite("data/" + time + ".png", image_data)
            pd.DataFrame(key_presses).to_csv("data/" + time + ".csv")




DataGenerator().generate()