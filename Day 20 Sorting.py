n=int(input())
a=list(map(int,input().split(' ')))
new_swap=0
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            new_swap+=1
print('Array is sorted in',new_swap,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])
