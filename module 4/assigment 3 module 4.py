#Task 1

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number: ")) #The input(n) should happen only once, outside the function.

print("Factorial of", n, "is", factorial(n))

#Task 2

n = int(input("Enter a number: "))
from math import *
print("Square root: ", round(sqrt(n),2))
print("Logarithm:", round(log(n),2))
print("Sine" , round(sin(n),2))