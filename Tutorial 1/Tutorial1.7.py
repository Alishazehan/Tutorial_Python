def findq(x, y):
    if x > 0 and y > 0:
        return "Q 1 (Top-Right)"
    elif x < 0 and y > 0:
        return "Q 2 (Top-Left)"
    elif x < 0 and y < 0:
        return "Q 3 (Bottom-Left)"
    elif x > 0 and y < 0:
        return "Q 4 (Bottom-Right)"
    elif x == 0 and y == 0:
        return "Origin (0,0)"
    elif x == 0:
        return "Y-axis"
    else:  # y == 0
        return "X-axis"

# Input from user
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Output the quadrant
print(findq(x, y))
