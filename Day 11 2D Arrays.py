a={}
b=[]
max=-64
for i in range(6):
    b=list(map(int,input().split(' ')))
    a[i]=b
for i in range(4):
    for j in range(4):
        sum=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        if sum>max:
            max=sum
print(max)
