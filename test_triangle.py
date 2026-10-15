import math
from triangle import classify_triangle, is_valid_triangle
# Test that a triangle with a zero-length side is invalid
def test_zero_length_side():
    assert not is_valid_triangle(0, 5, 7)
    assert classify_triangle(0, 5, 7) == "Invalid"



# Test a degenerate triangle where the sum of two sides equals the third
def test_degenerate_triangle():
    assert not is_valid_triangle(1, 2, 3)
    assert classify_triangle(1, 2, 3) == "Invalid"


    # Test that three equal positive sides form an equilateral triangle
def test_equilateral_triangle():
    assert is_valid_triangle(5, 5, 5)
    assert classify_triangle(5, 5, 5) == "Equilateral"


# Test that exactly two equal sides form an isosceles triangle
def test_isosceles_triangle():
    assert is_valid_triangle(5, 5, 3)
    assert classify_triangle(5, 5, 3) == "Isosceles"


    # Test that three different valid side lengths form a scalene triangle
def test_scalene_triangle():
    assert is_valid_triangle(4, 5, 6)
    assert classify_triangle(4, 5, 6) == "Scalene"


    # Test that sides 3, 4, and 5 form a right scalene triangle
def test_right_scalene_triangle():
    assert is_valid_triangle(3, 4, 5)
    assert classify_triangle(3, 4, 5) == "Right Scalene"


# Test a right isosceles triangle with non-integer hypotenuse using math.sqrt(2)
def test_right_isosceles_triangle():
    side_length = 1
    hypotenuse_length = math.sqrt(2)
    assert is_valid_triangle(side_length, side_length, hypotenuse_length)
    assert classify_triangle(side_length, side_length, hypotenuse_length) == "Right Isosceles"


    # Test that a triangle with a negative side length is invalid
def test_negative_side_length():
    assert not is_valid_triangle(-3, 4, 5)
    assert classify_triangle(-3, 4, 5) == "Invalid"


# Test that sides 2, 3, and 5 form an invalid degenerate triangle
def test_invalid_degenerate_triangle_copilot_review():
    assert not is_valid_triangle(2, 3, 5)
    assert classify_triangle(2, 3, 5) == "Invalid"


