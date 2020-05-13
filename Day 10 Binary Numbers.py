n=int(input())
a=0
b=0
while n>=1:
    f=n//2
    r=n%2
    n=f
    if r==1:
        a+=1
        b=max(b,a)
    else:
        a=0
print(b)
