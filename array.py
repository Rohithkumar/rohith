x=0
y=0
x,y=input().split()
x=int(x)
y=int(y)
a=[int(i) for i in input().split()]
sum=0
for i in range(0,y):
	sum=sum+a[i]
print(sum)

