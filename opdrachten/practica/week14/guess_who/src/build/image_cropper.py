import cv2
import logging
import math
from pathlib import Path
from nosql_adapter import MongoAdapter

logging.basicConfig(level="DEBUG")


class ImageCropper:
    def __init__(self, imgPath):
        self.imgName = Path(imgPath).name
        self.img = cv2.imread(imgPath)
        self.imgRows, self.imgCols, _ = self.img.shape

    def renderImage(self, imgToRender, imgTitle):
        print("Press 0 to close image.")
        cv2.imshow(str(imgTitle), imgToRender)

        sleepTime = 5
        cv2.waitKey(sleepTime * 1000)

        print(f"All windows will be closed after {sleepTime} seconds")
        cv2.destroyAllWindows()

    def showImage(self):
        self.renderImage(self.img, self.imgName)

    def getDimensions(self):
        print(f"rows : {self.imgRows}\ncolumns : {self.imgCols}")

    def crop(self, rowCellOffset, nrOfRows, colCellOffset, nrOfCols):
        height = math.ceil(self.imgRows / nrOfRows)
        width = math.ceil(self.imgCols / nrOfCols)

        logging.debug(f"height : {height}")
        logging.debug(f"width : {width}")

        rowOffset = rowCellOffset * height
        correction = 0.99 - colCellOffset * 0.001
        logging.debug(f"correction : {correction}")
        colOffset = math.floor((colCellOffset * width) * correction)

        logging.debug(f"rowOffset : {rowOffset}")
        logging.debug(f"colOffset : {colOffset}")

        cutImg = self.img[rowOffset : rowOffset + height, colOffset : colOffset + width]

        return cutImg

    def saveImage(self, imgToStore, storePath):
        cv2.imwrite(storePath, imgToStore)

    def storeImage(self, imgDict):
        MongoAdapter.insertOne(imgDict)

        # self.doc = self.col.find_one()
        # print("\nfind_one() result:", self.doc)

        # database_names = mongo.list_database_names()
        # print("\ndatabases:", database_names)

        # mongo.save_file(imgName, imgToStore)
        # mongo.db.perons.insert({"name": imgName.title()})
