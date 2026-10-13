from triangle import classify_triangle
import math
# Test that a triangle with three equal sides is equilateral
def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

    # Test that a triangle with exactly two equal sides is isosceles
def test_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"

    # Test that a triangle with three different sides is scalene
def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"


# Test that a triangle with a negative side is invalid
def test_invalid():
    assert classify_triangle(-1, 2, 3) == "Invalid"
    assert classify_triangle(1, -2, 3) == "Invalid"
    assert classify_triangle(1, 2, -3) == "Invalid"

    # Test that a triangle with sides 1, 2, 3 is invalid because it is degenerate
def test_degenerate():
    assert classify_triangle(1, 2, 3) == "Invalid"


    # Test that a triangle with sides 3, 4, 5 is classified as Right Scalene
def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


    # Test a right triangle with sides 5, 5, and 5 * sqrt(2) using floating-point tolerance
def test_right_isosceles():
    assert classify_triangle(5, 5, 5 * (2 ** 0.5)) == "Right Isosceles"