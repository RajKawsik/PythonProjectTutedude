#Task 1

a = int(input("Enter a number: "))
divide = a/2
if divide == int(divide):
    print(a, " is an even number")
else:
    print(a, " is an odd number")

#Task 2

counter = 0

for x in range(1, 51):
    counter = counter + x

print("The sum of integers from 1 to 50 is:", counter)