

def fact(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def nCr(n, r):
    if r > n:
        return "r cannot be greater than n"
    
    return fact(n) // (fact(r) * fact(n - r))

# Get user input
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Compute and print nCr
print(f"nCr ({n}C{r}) = {nCr(n, r)}")
