
a,b=input().split()
a=int(a)
b=int(b)
for i in range(a+1,b):
	c=0
	temp=i
	while(temp!=0):
		b=temp%10
		c=c+(b*b*b)
		temp=int(temp/10)
	if(c==i):
		print(c)
	
	
	
   
