# Enter your code here. Read input from STDIN. Print output to STDOUT
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
fine=0
if b[0]>=a[0] and b[1]>=a[1] and b[2]>=a[2]:
    fine=0
elif b[0]<a[0] and b[1]==a[1] and b[2]==a[2]:
    fine=15*(a[0]-b[0])
elif b[1]<a[1] and b[2]==a[2]:
    fine=500*(a[1]-b[1])
else:
    if b[2]<a[2]:
        fine=10000
print(fine)
