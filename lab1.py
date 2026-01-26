#question 1
'''import datetime
now=datetime.datetime.now()
print("currrent date time",now)'''
#question 2
'''fname=input("enter the first name")
lname=input("enter the last name")
print(lname,fname)'''
#question 3
'''n=int(input("enter a number"))
result=n+int(str(n)*2)+int(str(n)*3)
print("the expected result is:",result)'''
#question 4
'''a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
sum=a+b+c
if a==b==c:
    print(3*sum)
else:
    print(sum)'''
#question 5
'''x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
result=(x+y)**2
print("the expected result is:",result)'''
#question 6
'''p=float(input("enter the principal amount:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time in years:"))
f=p*(1+r/100)**t
print("the future value is:",round(f,2))'''
#question 7
'''a=input("enter a string:")
print(a)
#result=(int(a))
result=(float(a))
print("addition",result+5)
print("the value is:",result)'''
#question 8
'''n=int(input("enter the number"))
sum=n*(n+1)//2
print("the sum of first n natural numbers is:",sum)'''
#question 9
'''n=int(input("enter the value of the number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("the sum of digits is:",sum)'''
#question 10
'''ch=input("enter the value")
value=ord(ch)
print("the ascii value is:",value)'''
#question 11
'''n=input("enter the string:")
if n.isnumeric():
    print("the string is numeric")
else:
    print("the string is not numeric")'''
#question 12
'''for i in range(5):
    for j in range(3):
        print("*",end=' ')
    print()'''
#question 13
'''for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=',')'''
#question 14
'''import math
c=50
h=30
values=input("enter comma sepated values:").split(",")
result=[]
for d in values:
    q=math.sqrt((2*c*int(d))/h)
    result.append(str(round(q)))
print(",".join(result))'''
#question 15
n=int(input("enter the string:"))
for i in range(n,0,-1):
     print("*"*i)