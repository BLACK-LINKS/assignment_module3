r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))

pi = 3.14

volume = pi * r * r * h
surface_area = 2 * pi * r * (r + h)

print("The volume of the cylinder is", volume)
print("The surface area of the cylinder is", surface_area)
