def isrighttriangle(a, b, c):
    sides = sorted([a, b, c])
    
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        return "is a right-angled triangle."
    else:
        return "Not a right-angled triangle."

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print(isrighttriangle(a, b, c))
else:
    print("Invalid triangle. The sum of any two sides must be greater than the third side.")
