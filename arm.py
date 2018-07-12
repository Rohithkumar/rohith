c=0
n=int(input())
temp=n
while(temp!=0):
    b=temp%10
    c=c+(b*b*b)
    temp=int(temp/10)
if c==n:
    print("yes")
else:
    print("no")
