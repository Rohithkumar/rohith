c=0
print("enter the number to be checked")
n=int(input())
temp=n
while(temp!=0):
	
    b=temp%10
    c=(c*10)+b
    temp=int(temp/10)
if(c==n):
         print("it is palindrome")
else:
	print("its not a palindrome")
