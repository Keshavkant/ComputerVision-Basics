import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="mountain.jpg", help="path to the input image")
args = vars(ap.parse_args())

added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))

added = np.uint8([300]) + np.uint8([100])
subtracted = np.uint8([100]) - np.uint8([50])
print("Wrapped of 255:  {}".format(added))
print("Wrapped of 0: {}".format(subtracted))

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)

cv2.waitKey(0)
