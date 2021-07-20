'''arashi_imageファイルにある画像をOpenCVで瞳を検出し、切り出すプログラム。
瞳の検出にはOpenCVのデフォルトの分類器(https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)を使用する。
'''

import cv2, os, re,requests, time, bs4
from urllib.request import urlretrieve
from urllib import request as req
from urllib import error,parse
from PIL import Image
import numpy as np
import glob
from multiprocessing import Pool, Queue, Process
from multiprocessing import Pool
import sys
#from util.estimator import Estimate


def main(member):
    eye_cascade_path = "haarcascade_righteye_2splits.xml"#OpenCVのデフォルトの分類器のpath
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)



    
    img_dir = "./arashi_image/"

    files = glob.glob(img_dir+member+"/*.jpg")
    print("{}の写真は{}枚です。瞳認識を始めます。".format(member, len(files)))
    error_count = 0
    for index, file in enumerate(files,1):
        img = cv2.imread(file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #minSizeを5の倍数で5から100まで変更して検出することで、瞳の検出率を高める。
        for i in range(1,20):
            minValue = i * 5
            eyes = eye_cascade.detectMultiScale(img_gray, minSize=(minValue,minValue))
            if len(eyes) == 1:
                break
        if len(eyes) != 1:
                continue
        for x,y,w,h in eyes:
                img = img[y:y+h, x:x+w]
        face_path = img_dir+member+"/eye"
        if not os.path.exists(face_path):
            os.makedirs(face_path)
        cv2.imwrite(face_path  + "/" + str(index)+".jpg", img)

if __name__ == "__main__":
    _,member = sys.argv
    main(member)