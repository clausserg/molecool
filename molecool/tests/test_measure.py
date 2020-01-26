"""
Unit test for the measure.py module
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np
import pytest

def test_calculate_distance():

    """Test that the calculate_distance() functions returns correctly"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert calculated_distance == expected_distance


def test_calculate_distance_typeerorr():
    
    r_a = [0, 0, 0]
    r_b = [0, 1, 0]

    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r_a, r_b)


def test_calculate_angle():

    """Test that the calculate_angle() function returns correctly"""

    r_a = np.array([0, 0, -1])
    r_b = np.array([0, 0, 0])
    r_c = np.array([0, 1, 0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r_a, r_b, r_c, degrees=True)

    assert calculated_angle == expected_angle

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
])

def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert pytest.approx(calculated_angle) == expected_angle







