import cv2
import numpy as np
from pathlib import Path, PurePath
from time import sleep

class ImageCropper():

    def __init__(self, imgPath):
        self.imgPath = imgPath
        self.img = cv2.imread(imgPath)
        self.rows, self.cols, _ = self.img.shape

    def showImage(self):
        cv2.imshow(self.imgPath, self.img)
        
        print("Press 0 to close image")
        cv2.waitKey(0)

    def getDimensions(self):
        print( f"rows : {self.rows}\ncolumns : {self.cols}" )

    def crop(self, vertCrop, horCrop):
        height = self.rows //vertCrop
        width = self.cols // horCrop
        cutImg = self.img[0:height, 0:width]        

        self.saveImage( cutImg, f"../data/cropped_img_{height}_{width}.jpg" )

        print("Press 0 to close image.")
        cv2.imshow("cut", cutImg)

        sleepTime = 5
        cv2.waitKey(sleepTime * 1000)

        print( f"All windows will be closed after {sleepTime} seconds" )
        # sleep(sleepTime)
        cv2.destroyAllWindows()

        # return cutImg

    def saveImage(self, imgToStore, storePath):
        cv2.imwrite(storePath, imgToStore)


    def split(self):
        self.crop(3, 8)
