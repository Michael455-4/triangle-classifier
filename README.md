
# Triangle Classifier

## Project Description

This project is a Python program that classifies triangles based on three side lengths.

The program determines whether a triangle is valid and classifies it as Equilateral, Isosceles, or Scalene. It also identifies right triangles using the Pythagorean theorem.

The project includes unit tests written with the assistance of GitHub Copilot and an acceptance test based on a stained-glass studio's customer requirements.

## How to Run the Tests

1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required dependency:

   python3 -m pip install -r requirements.txt

4. Run all tests:

   python3 -m pytest -v

## Why an Equilateral Triangle Cannot Be Right

An equilateral triangle has three equal angles of 60 degrees. Since a right triangle must have one 90-degree angle, an equilateral triangle cannot also be a right triangle.


## Equivalence Classes and Boundary Cases

Equivalence classes are groups of inputs that should produce the same type of result.

### Equivalence Classes

| Input | Expected Result | Reason |
|---|---|---|
| (0, 4, 5) | Invalid | A side cannot be zero. |
| (-3, 4, 5) | Invalid | A side cannot be negative. |
| (1, 2, 3) | Invalid | The sum of two sides equals the third. |
| (2, 3, 10) | Invalid | The sum of two sides is less than the third. |
| (5, 5, 5) | Equilateral | All three sides are equal. |
| (5, 5, 3) | Isosceles | Exactly two sides are equal. |
| (4, 5, 6) | Scalene | All three sides are different. |
| (3, 4, 5) | Right Scalene | The sides satisfy the Pythagorean theorem. |
| (1, 1, math.sqrt(2)) | Right Isosceles | Two sides are equal and the triangle has a right angle. |

### Boundary Cases

The triangle inequality requires the sum of any two sides to be greater than the third side.

- (1, 2, 3) is invalid because 1 + 2 = 3.
- (2, 3, 10) is invalid because 2 + 3 < 10.
- (0, 4, 5) is invalid because one side equals zero.
- (-3, 4, 5) is invalid because one side is negative.

The right-triangle test uses math.isclose() instead of == to handle floating-point rounding errors.


## Acceptance Criteria

The following acceptance criteria are based on the stained-glass studio's customer requirements.

1. When a customer enters three side lengths that cannot form a valid triangle, the program must return "Invalid" without crashing.

2. When a customer enters three valid side lengths, the program must return the correct triangle classification: "Equilateral", "Isosceles", or "Scalene".

3. When a customer enters three side lengths that form a right triangle, the program must return a classification beginning with "Right " to indicate that reinforced corners are required.

The acceptance test in test_acceptance.py checks all three criteria using invalid, equilateral, and right scalene triangle examples.

## AI-Use Disclosure

Tools used: GitHub Copilot and ChatGPT (OpenAI).

GitHub Copilot was used to suggest unit tests in test_triangle.py. I reviewed the suggestions against the assignment requirements before accepting them.

ChatGPT was used for guidance on project setup, implementing the triangle classifier, understanding the testing requirements, and preparing the README.

The acceptance test was written without GitHub Copilot, following the assignment instructions.

I verified the program by running pytest. All 9 unit tests and the acceptance test passed, for a total of 10 passing tests.




## Copilot Review Log

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| test_zero_length_side | Yes | Kept | Correctly checks that a zero-length side is invalid. |
| test_degenerate_triangle | Yes | Kept | Correctly checks the boundary where 1 + 2 = 3. |
| test_equilateral_triangle | Yes | Kept | Correctly checks three equal positive sides. |
| test_isosceles_triangle | Yes | Kept | Correctly checks sides (5, 5, 3). |
| test_scalene_triangle | Yes | Kept | Correctly checks sides (4, 5, 6). |
| test_right_scalene_triangle | Yes | Kept | Correctly checks the 3-4-5 right triangle. |
| test_right_isosceles_triangle | Yes | Kept | Correctly checks a non-integer hypotenuse using math.sqrt(2). |
| test_negative_side_length | Yes | Kept | Correctly checks that a negative side is invalid. |
| test_invalid_degenerate_triangle_copilot_review | Yes | Edited | Copilot incorrectly treated (2, 3, 5) as a valid Scalene triangle. I corrected both assertions because 2 + 3 = 5, which violates the triangle inequality. |

