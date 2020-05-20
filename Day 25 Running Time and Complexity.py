import math

def check_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_divisor=math.floor(math.sqrt(n))
    for i in range(3,1+int(max_divisor),2):
        if n%i==0:
            return False
    return True

T=int(input())
for _ in range(T):
    n=int(input())
    if check_prime(n):
        print('Prime')
    else:
        print("Not prime")
