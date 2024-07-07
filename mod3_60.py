def trapezoid_area(a, b, h):
    area = 0.5 * (a + b) * h
    return area

a = float(input("Enter the length of the first base: "))
b = float(input("Enter the length of the second base: "))
h = float(input("Enter the height: "))

area = trapezoid_area(a, b, h)

print(f"The area of the trapezoid is {area:.2f} square units.")
