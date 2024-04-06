import cv2
import random
import numpy as np
import argparse

# Initialize a global list to store points
clicked_points = []

# add an argument parser to get the image path
parser = argparse.ArgumentParser()
parser.add_argument('image_path', type=str, help='Path to the image')
args = parser.parse_args()
image_path = args.image_path

# Create an empty (white) image instead of reading from a path

# image = np.ones((height, width, 3), np.uint8) * 255  # White background
# image_path = './images/0777_1.png'  # Replace with your image path
image = cv2.imread(image_path)
height, width, _ = image.shape
print(f"Image Width: {width}, Image Height: {height}")
# Function to be called every time the mouse events happen
def mouse_click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Point added: (x={x}, y={y})")
        cv2.circle(image, (x, y), 2, (0, 0, 0), -1)  # Change circle color to black
        cv2.imshow('Image', image)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_click_event)

cv2.imshow('Image', image)
cv2.waitKey(0)  # Change to 0 to wait indefinitely until a key is pressed

# Draw the final circle in black on a new white background image
final_image = np.ones((height, width, 3), np.uint8) * 255  # White background
# add the polygon points to the image in black
cv2.fillPoly(final_image, [np.array(clicked_points)], (0, 0, 0))
cv2.imshow('Mask image', final_image) # Show the final masked image
cv2.imwrite('final_image.png', final_image)  # Save the image to the current directory
# cv2.waitKey(0)

cv2.destroyAllWindows()