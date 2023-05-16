import crossings as cross
import cv2

# Load your image
image = cv2.imread("bison.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or any other necessary preprocessing
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours (USE CHAIN_APPROX_NONE)
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw contours on the image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

#Define the start and end points
start_point = (0, 0)
end_point = (2000, 2000)

# Drawing the line (optional)
cv2.line(image, start_point, end_point, (255,0,0), 2)

# Getting crossing points
crossing_points = cross.get_cross_points(contours, start_point, end_point)

for point in crossing_points :
    cv2.circle(image, point, 10, (255,0,0), 1)


cv2.imwrite("results/result.png", image)
