x=input("enter 1st number ")
y=input("enter second number ")
a=max(x,y)
while(1):
    
    if a%x==0 and a%y==0:
        print("lcm is ",a)
        break
    else:
        a+=1


    
