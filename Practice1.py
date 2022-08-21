import argparse  #Allow the user to input t obe pqarsed without inputting the value manually
import cv2

ap = argparse.ArgumentParser() #Initialize the parser so that we can start to add custom argument
ap.add_argument("-i", "--image", required=True, help="path to input image") #add an argument
#ap.add_argument("-o", "--output", help="Path to output image")
#args = vars(ap.parse_args())
#with open(args.output, 'w') as output_file:
    #output_file.write("%s\n" % item)

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channel: {} pixels".format(c))

cv2.imshow("Keshav Doing Cool Stuffs!", image)
cv2.waitKey(0)

cv2.imwrite("Keshav doing cool stuff.jpg", image)


