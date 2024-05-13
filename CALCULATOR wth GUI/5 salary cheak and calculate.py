# calculate total salary of employee 1 and 2
# 15000 se kam ko 10% h.r or usse jyada wale ka 30%
x=input("enter your salary")
y=0
sal=0
if x<=15000:
    y=x*10/100
    sal=x+y
    print(sal)
else:
    y=x*30/100
    sal=x+y
    print(sal)
