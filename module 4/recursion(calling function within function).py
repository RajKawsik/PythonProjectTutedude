# RECURSION

import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(100)

'''
def python():
        print("Python")
    python()            #repeats upto 1000 times which is system limit
                        #with above recursion limit function, modified it
python()
'''
n = 0

def python():
    global n
    n = n + 1           #changing "1" changes the add function but line will stop at 96 times
    print("Python", n)
    python()            #repeats upto 1000 times which is system limit
                        #with above recursion limit function, modified it
python()
