a,b,c=map(int,input().split())
(a,b)=(b,a)
a=a*c
b=b+c
print(str(a)+ " " +str(b))