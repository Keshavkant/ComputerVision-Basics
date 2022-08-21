import argparse
import imutils  #For resizing
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Army.jpg", help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

