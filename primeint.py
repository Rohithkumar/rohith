a=int(input())
b=int(input())
count=0
for i in range(a+1,b):
	count=0
	for j in range(1,int(i+1)):
		if i%j==0:
			count=count+1
	if count==2:
	    print(i,end=" ")
