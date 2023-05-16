import cv2
import numpy as np
import math

def get_points_between(start_point, end_point):
    points_list = []
    
    # Extract coordinates from the start and end points
    x1, y1 = start_point
    x2, y2 = end_point
    
    # Compute differences and absolute differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy
    
    # Start with the first point
    x, y = x1, y1
    
    # Append the start point to the list
    points_list.append((x, y))
    
    while x != x2 or y != y2:
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        points_list.append((x, y))
    
    return points_list


def remove_close_points(points, threshold):
    '''
    Removes close points from the points list compared to a threshold
    '''
    
    remaining_points = []
    for i in range(len(points)):
        current_point = points[i]
        keep_point = True
        
        for j in range(i+1, len(points)):
            other_point = points[j]
            
            distance = math.sqrt((current_point[0] - other_point[0])**2 + (current_point[1] - other_point[1])**2)
            
            if distance < threshold:
                keep_point = False
                break
        
        if keep_point:
            remaining_points.append(current_point)
    
    return remaining_points


def get_cross_points(contours, start_point, end_point, out_dist_thresh = 1, in_dist_thresh = -1, close_point_thresh = 10) :
    '''
    Returns cross points between two points and list of contours

    start_point : starting of the line
    end_point : ending of the line
    out_dist_thresh : threshold between the point and the contour (outside)
    in_dist_thresh : threshold between the point and the contour (inside)
    close_point_thresh : distance to delete close points   
    '''
    
    points_between = get_points_between(start_point, end_point)
    cross_points = []
    for contour in contours :
        for point in points_between :
            res = cv2.pointPolygonTest(contours[0], point, True)
            if  (res < out_dist_thresh) and (res > in_dist_thresh) :
                cross_points.append(point)
    cross_points = remove_close_points(cross_points, close_point_thresh)
    
    return cross_points



    
