# 2 numbers, if you add them = 7
# Square of the number
# 1(not 2) function call to be used

def add(x,y):
    return x + y
def square(z):
    return z * z

result = square(add(6,1))
print(result)