
from triangle import classify_triangle


def test_customer_requirements():
    # A customer enters three side lengths.
    # Check whether the program identifies invalid glass pieces.
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"

    # Check the shape of valid glass pieces.
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"

    # Check whether right-angle glass pieces are identified.
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * (2 ** 0.5)) == "Right Isosceles"
