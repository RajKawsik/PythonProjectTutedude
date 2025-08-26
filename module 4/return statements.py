#def func():
#   statements
#   ...
#   return (expr)
#return(expr) --> WRONG (space is essential)

#function call

def add(a,b):
    print(a+b)
add(1,2)

def add1(a,b):
    c = a+b
    return c

a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
ans=add1(a,b)
print(ans)  # Variable 'ans' receives the returned result

#don't forget to assign variable name to function call. or else won't return

def mult(a,b):
    c = a * b
    return c

result = mult(2, "Mike ")
print(result)