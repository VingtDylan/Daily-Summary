from PIL import Image
import cv2
import os
import glob
import numpy as np

PATH = r'Drosophila'
image = glob.glob(os.path.join(PATH, '*.png')) + \
        glob.glob(os.path.join(PATH, '*.jpg'))


for idx, path in enumerate(image): 
    img = Image.open(path)
    img = np.array(img).astype(np.uint8)
    # print(path)
    img = np.stack((img,)*3, axis=-1)
    img = img[500:800, 1800:2200,:]
    cv2.imwrite(PATH + '/trans/' + str(idx) + '.png', img) 