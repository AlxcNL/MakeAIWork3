#!/usr/bin/env python

# IMPORTS
from data_preprocessing import ImageCropper

def main():
    imageCropper = ImageCropper("../data/guess_who.jpg")
    # imageCropper.showImage()
    imageCropper.getDimensions()
    imageCropper.split()

# MAIN
if __name__ == "__main__":
    main()