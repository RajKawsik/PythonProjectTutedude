# a ---> 10 times

#counter variable
#while (test expr. ):
    #statement
    #increment / decrement

#increment
counter = 1
while counter <= 5:
    print('a')
    counter=counter+1
    # since counter is 1, after first output acc. to the formula, updates: counter = 1+1 = 2

#decrement
counter = 5
while counter >= 1:
    print('b')
    counter=counter-1
    #counter-=1
    #since counter is 5, after first output acc. to the formula, updates: counter = 5-1 = 4

count = 0
while (count<=10):
    print(count)
    count=count+1

#check if LHB and RHB is the same or else output will be never ending