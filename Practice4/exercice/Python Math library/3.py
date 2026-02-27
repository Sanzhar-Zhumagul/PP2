import math
n = int(input("Input number of sides:"))
s = int(input("Input length of each side:"))
area = (n * s * s) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", int(area))