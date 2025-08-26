#Celcius---> Farenheit
c=input('Celsius: ')
c=float(c)
f=(c * 9/5) + 32
print('Farenheit: ',f)
#Farenheit---> Celcius
f=input('Farenheit: ')
f=float(f)
c=(f - 32) * 5/9
print('Farenheit: ',c)

#SI calculator
p= input('P: ')
n= input('N: ')
r= input('R: ')
p=int(p)
n=int(n)
r=int(r)
si=(p*n*r)/100
print("Simple interest is: ", si)