n = 1           # GLOBAL VARIABLE

def fn():
    n = 5       # LOCAL VARIABLE
    print('in',n)
fn()
print('out',n)

n = 1           # GLOBAL VARIABLE

def fn():
    # LOCAL VARIABLE
    print('in',n)
fn()
print('out',n)      #Run to see output (n = 1) becomes local variable also

#Whenever you create a new variable with the same name inside a function,
#it becomes local and is used only within that function.
#The global variable is used everywhere else,
#unless you use the global keyword to tell Python to use it inside the function.