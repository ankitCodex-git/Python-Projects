# prime cheak in range

x=input('enter number')
y=input("enter 2nd number")
while x<y:
    j=2
    flag=1
    while j<x:
        if x%j==0:
            flag = 0
            break
        else:
            j+=1
    if flag==1:
        print(x)
        x+=1
    else:
        x+=1
