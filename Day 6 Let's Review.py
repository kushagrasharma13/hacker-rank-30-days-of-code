n=int(input())
for i in range(n):
    a=input()
    k=''
    l=''
    for i in range(len(a)):
        if i%2==0:
            k+=a[i]
        else:
            l+=a[i]
    print(k,l)
