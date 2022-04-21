import cv2
import matplotlib.pyplot as plt
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img) # we are taking zeros because(0-black, 255-White)
    mask_color = 255 
    cv2.fillPoly(mask, vertices, mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

