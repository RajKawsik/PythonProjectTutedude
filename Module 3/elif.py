operand_1=int(input('Enter operand1: '))
operand_2=int(input('Enter operand2: '))
operator=input('Enter operator (+,-,*,/): ')
#if (text expr):
    #statement

if operator=='+':
    print(operand_1+operand_2)
elif operator=='-':
    print(operand_1-operand_2)
elif operator=='*':
    print(operand_1*operand_2)
elif operator=='/':
    print(operand_1/operand_2)
else:
    print("Invalid operator")

print('Thank you')