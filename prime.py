count=0
print("enter the number to check for prime")
n=int(input())
for i in range(1,n):
    if (n%i==0):
        count=count+1
if count==2:
    print("it is a prime number")
else:
    print("it is not a prime number")
		
