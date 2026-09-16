# geometric_lib
Python library for calculating areas and perimeters(circumferences)
of various plane shapes

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = abc

# Functions
## circle.py
- area(r) - returns the area of a circle with r radius
`area(6)` returns ~113.097
- perimeter(r) - returns the circumference of a circle with r radius
`perimeter(6)` returns ~37.699

## rectangle.py
- area(a, b) - returns the area of a rectangle with sides of a and b
`area(2, 3)` returns 6
- perimeter(a, b) - returns the perimeter of a rectangle with sides of a and b
`perimeter(2, 3)` returns 10

## square.py
- area(a) - returns the area of a square with a side of a
`area(4)` returns 16
- perimeter(a) - returns the perimeter of a square with a side of a
`perimeter(2)` returns 8

## triangle.py
- area(a, h) - returns the area of a 90deg triangle with sides of a and h
`area(5, 6)` returns 15
- perimeter(a, b, c) - returns the perimeter of a triangle with sides of a, b and c
`perimeter(1, 2, 3)` returns 6

# Commit history
- main
8ba9aeb3cea847b63a91ac378a2a6db758682460 - Circle and square added
d078c8d9ee6155f3cb0e577d28d337b791de28e2 - Docs added

- new_features_561505
f6f65458c6da063b714e2a10d2c9c150c823d77f - added rectangle.py
6033f58f65373a57c71a3a6ab0ab76ac4b675226 - added triangle.py
41b07988147877ec2a6845a03bea8cbd16cd5a72 - fixed rectangle.py
