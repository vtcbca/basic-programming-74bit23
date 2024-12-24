def factorial(x):
    if x == 1 or x == 0:
        return 1
    else: 
        return (x * factorial(x-1))
number = 10
result = factorial(number)
print("The factorial of", number, "is", result)