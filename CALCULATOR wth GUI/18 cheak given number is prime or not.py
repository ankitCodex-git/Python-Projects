# cheak given number is prime or not
x= input("enter number")
flag=1
j=2
while j<x:
    if x%j==0:
        flag=0
        break
    else:
        j+=1
if flag ==1:
    print ("prime")
else:
    print("not prime")


