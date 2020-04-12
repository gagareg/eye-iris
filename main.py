import cv2
import numpy as np
from PIL import Image, ImageDraw

image = Image.open("input.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]

resize_img = Image.open("input.jpg")
resize_img = resize_img.resize((width, height), Image.ANTIALIAS)

image = resize_img
pix = image.load()

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = (a + b + c) // 3
        draw.point((i, j), (S, S, S))

image.save("input-gray.jpg", "JPEG")
del draw

img = cv2.imread("input-gray.jpg", 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 75, param1=75, param2=30, minRadius=130, maxRadius=150)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)  # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)  # draw the center of the circle

cv2.imwrite("output.jpg", cimg)  # save img
cv2.destroyAllWindows()
