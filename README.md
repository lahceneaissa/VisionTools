# VisionTools
Computer vision tools for opencv with Python 

# Crossings.py : 
Contains some function to calculate crossing points between a line and a contour in opencv

## Usage : 
get_cross_points(contours, start_point, end_point, out_dist_thresh = 1, in_dist_thresh = -1, close_point_thresh = 10) 
Where : 
Returns cross points between two points and list of contours
- start_point : starting of the line
- end_point : ending of the line
- out_dist_thresh : threshold between the point and the contour (outside)
- in_dist_thresh : threshold between the point and the contour (inside)
- close_point_thresh : distance to delete close points 

Example of usage in main.py
