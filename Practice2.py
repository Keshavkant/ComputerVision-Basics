import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Foundation.jpg", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]  # this mean, h = image.shape[0] and w = image.shape[1]
cv2.imshow("Original", image)

(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {}, Gree: {}, Blue: {}".format(r, g, b))
(b,g,r) = image[20,50] # x = 50, y = 20
image[20,50] = (0,0,255)
(b, g, r) = image[20, 50]
print("Pixel at (50,20) -Red: {}, Green: {}, Blue: {}".format(r,g,b))

(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
cv2.imshow("Top left corner", tl)

tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top right corner", tr)
cv2.imshow("Bottom right corner", br)
cv2.imshow("Bottom Left Corner", bl)

image[0:cY, 0:cX] = (0, 255, 0)
cv2.waitKey(0)

cv2.imshow("Updated", image)
cv2.waitKey(0)