# Write your solution here
# Let's take the square root of math-module in use
# (-b ± sqrt(b²-4ac))/(2a).

from math import sqrt

a: float = float(input("Value of a: "))
b: float = float(input("Value of b: "))
c: float = float(input("Value of c: "))

x: float = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
y: float = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)

print(f"The roots are {x} and {y}")