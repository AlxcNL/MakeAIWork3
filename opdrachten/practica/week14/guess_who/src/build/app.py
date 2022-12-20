#!/usr/bin/env python

# IMPORTS
from image_cropper import ImageCropper
import logging
from os import path
from pathlib import PurePath
from nosql_adapter import MongoAdapter

imgDir = PurePath("../../data/pics")
mongoClient = MongoAdapter("guess_who", "persons")
logging.basicConfig(level="DEBUG")


def extractPortraits(imageCropper):
    # Represent guess_who.jpg as a grid
    nrOfRows = 3
    nrOfCols = 8
    rows = range(nrOfRows)
    cols = range(nrOfCols)

    # Add empty rows
    personGrid = [["" for col in cols] for row in rows]

    # TODO Exercise 1: Add all names to the grid

    personGrid[0][0] = "Alex"
    personGrid[0][1] = "Alfred"
    personGrid[2][7] = "Tom"

    logging.debug(personGrid)

    # Example with Alex
    portraitName = personGrid[0][0]
    logging.debug(f"portraitName : {portraitName}")

    rowOffset, colOffset = 0, 0
    portraitImg = imageCropper.crop(rowOffset, nrOfRows, colOffset, nrOfCols)
    portraitImgPath = path.join(imgDir, f"{portraitName.lower()}.jpg")

    logging.debug(f"portraitImgPath : {portraitImgPath}")
    imageCropper.saveImage(portraitImg, portraitImgPath)

    # Example with Alfred
    portraitName = personGrid[0][1]
    logging.debug(f"portraitName : {portraitName}")

    rowPortOffset, colPortOffset = 0, 1
    portraitImg = imageCropper.crop(rowPortOffset, nrOfRows, colPortOffset, nrOfCols)
    portraitImgPath = path.join(imgDir, f"{portraitName.lower()}.jpg")

    logging.debug(f"portraitImgPath : {portraitImgPath}")
    imageCropper.saveImage(portraitImg, portraitImgPath)

    # Example with Tom

    portraitName = personGrid[2][7]
    logging.debug(f"portraitName : {portraitName}")

    rowPortOffset, colPortOffset = 2, 7
    portraitImg = imageCropper.crop(rowPortOffset, nrOfRows, colPortOffset, nrOfCols)
    portraitImgPath = path.join(imgDir, f"{portraitName.lower()}.jpg")

    logging.debug(f"portraitImgPath : {portraitImgPath}")
    # imageCropper.saveImage(portraitImg, portraitImgPath)
    # imageCropper.storeImage(portraitImg, portraitName)


def main():
    imgPath = path.join(imgDir, "guess_who.jpg")

    logging.debug(imgPath)
    imageCropper = ImageCropper(imgPath)
    imageCropper.getDimensions()

    extractPortraits(imageCropper)

    # Excercise 2

    properties = dict()
    properties["Alex"] = ["Moustache", "Brown Hair"]
    properties["Alfred"] = ["Blue Eyes", "Moustach"]
    properties["Tom"] = ["Bold", "Glasses", "Blue Eyes", "Brown Hair"]

    alex = {"name": "Alex", "properties": properties["Alex"]}
    alfred = {"name": "Alfred", "properties": properties["Alfred"]}
    tom = {"name": "Tom", "properties": properties["Tom"]}

    mongoClient.deleteCollection()

    mongoClient.insertOne(alex)
    mongoClient.insertOne(alfred)
    mongoClient.insertOne(tom)


# MAIN
if __name__ == "__main__":
    main()
