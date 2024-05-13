#Fibonacci Series
x=input("enter number")
y=input("enter 2nd number")
print(x)
print(y)
i=1
z=0
j=10
while i<(j-1):
    z=x+y
    print(z)
    x=y
    y=z
    i+=1
