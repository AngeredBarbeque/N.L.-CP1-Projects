def calculate_area(x, y):
    z = x * y
    return z

def volume_calculation(a, b, c):
    temp = calculate_area(a, b)
    result = temp * c
    return result

widtha = 5
lengtha = 3
square = calculate_area(widtha, lengtha)
print(f"The square's size is: {square}")

depthv = 4
widthv = 6
lengthv = 2
cube = volume_calculation(depthv, widthv, lengthv)
print(f"The cube's size is: {cube}")