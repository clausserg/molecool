"""
measure.py

This module performs measurements!
"""

import numpy as np


def calculate_distance(r_a, r_b):
    """
    Calculate the distance between two points.
    
    Parameters
    ==========
    r_a, r_b : np.ndarray
    	the coordinates of each point

    Returns
    =======
    distance : float
    	The distance between the two points

    Examples
    ========

    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """
    distance_vector = (r_a - r_b)
    distance = np.linalg.norm(distance_vector)
    return distance

def calculate_angle(r_a, r_b, r_c, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    r_ab = r_b - ra
    r_bc = r_b - rc
    theta=np.arccos(np.dot(r_ab, r_bc)/(np.linalg.norm(r_ab)*np.linalg.norm(r_bc)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

