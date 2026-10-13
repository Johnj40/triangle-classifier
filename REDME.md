
# Triangle Classifier

## Project Description
This project is a Python program that classifies triangles based on their three side lengths. It checks whether the triangle is valid and determines whether it is equilateral, isosceles, or scalene. It also identifies right triangles.

## How to Run the Tests
1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required package:

   python3 -m pip install -r requirements.txt

4. Run the tests:

   python3 -m pytest -v

## Equivalence Classes
The program tests the following categories:

- Invalid triangles: zero or negative sides, or sides that violate the triangle inequality.
- Equilateral triangles: all three sides are equal.
- Isosceles triangles: exactly two sides are equal.
- Scalene triangles: all three sides are different.
- Right triangles: side lengths satisfy the Pythagorean theorem.

## Boundary Cases
The program checks important boundary cases:

- A side length of zero.
- Negative side lengths.
- A degenerate triangle such as (1, 2, 3).
- A right triangle such as (3, 4, 5).
- A right isosceles triangle such as (5, 5, 5 * sqrt(2)).

## Testing Results
The project includes seven unit tests and one acceptance test. All eight tests passed using pytest.



## Copilot Review Log

### Suggestion 1
- Suggested code: Equilateral test
- Decision: Edited 
- Reason: Copilot sugested equilateral with a lower case e.

### Suggestion 2
- Suggested code: Scalene test
- Decision: Edited 
- Reason: Copilot sugested (3, 4, 5) for scalene. I changed it to (4, 5, 6) because the other one is a right triangle 

## AI-Use Disclosure
- AI tools used: ChatGPT
- What I used them for: Helped me understand the intruction and my code. Plus helped me decide what Copolot sugested. 
- What I personally verified: I ran the test and vertfied that everything was right. 
