import math

pi = math.pi
r = input("Enter the circle radius lenght to calculate the circle area:")
r_int = int(r)
circle_area = pi * r_int**2
circle_area_str = str(circle_area)

print(f"Your circle area is equals: {circle_area_str}")