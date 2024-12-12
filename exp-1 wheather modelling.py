import math

a, b, c = 0.01, -0.2, 30
x = 5
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are: {root1:.2f} and {root2:.2f}")
else:
    print("No real roots exist. The discriminant is negative.")
y = a * x**2 + b * x + c
print(f"Hard-coded Weather Model: At hour {x}, temperature = {y:.2f}°C")
