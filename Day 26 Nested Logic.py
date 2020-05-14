# Enter your code here. Read input from STDIN. Print output to STDOUT
a=list(map(int,input().split(' ')))
e=list(map(int,input().split(' ')))
fine=0
if e[0]>=a[0] and e[1]>=a[1] and e[2]>=a[2]:
    fine=0
elif e[0]<a[0] and e[1]==a[1] and e[2]==a[2]:
    fine=15*(a[0]-e[0])
elif e[1]<a[1] and e[2]==a[2]:
    fine=500*(a[1]-e[1])
else:
    if e[2]<a[2]:
        fine=10000
print(fine)
