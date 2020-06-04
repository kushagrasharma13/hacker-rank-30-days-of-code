import math
import os
import random
import re
import sys

def checker(emailID):
    regex = '^[a-z0-9]+[\._]?[a-z]+[@]+[gmail]+[.]\w{3}$'
    if(re.search(regex,emailID)):
        return True 
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    l=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if checker(emailID):
            l.append(firstName)
    for _ in sorted(l):
        print(_)
            
        
