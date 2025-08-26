# FACTORIAL

# 0! = 1
# 1! = 1 * 0! = 1 * 1 = 1
# 2! = 2 * 1! = 2 * 1 = 2
# 3! = 3 * 2! = 3 * 2 = 6

def factorial(n):
    if n <2:                            #if function for avoiding 0 for 1! and 0!
        return 1
    else:
        return n * (factorial(n - 1))

result = factorial(2)
print(result)
