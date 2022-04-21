import cv2
import matplotlib.pyplot as plt
import numpy as np

'''Since we are considering only one lane, we need to consider that one region
with our required lane. '''

def region_of_interest(img, vertices):
    mask = np.zeros_like(img) # we are taking zeros because(0-black, 255-White)
    mask_color = 255 
    cv2.fillPoly(mask, vertices, mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

'''We have a points from cv2.HoughLinesP. We need to draw lines by using those points on a blank image.
After that we need to blend it to the original image.
So, for blending we used cv2.addweighted()'''

def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 0.2, 0.0)
    return img

'''Piplene to process the given image'''
def process(image):
    
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
        (0, height),
        (width/2, height/1.7),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100,200)
    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=40, maxLineGap=25)
    image_lines = drow_the_lines(image, lines)
    return image_lines



# img = cv2.imread(r'resources\test_images\solidWhiteCurve.jpg')
# image_lines = process(img)
# cv2.imshow('lane1',image_lines)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(r'resources\test_videos\solidYellowLeft.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('trail',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()