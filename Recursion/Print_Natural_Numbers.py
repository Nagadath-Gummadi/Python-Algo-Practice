def printNatural(n):
    if(n==1):
        print(1,end=' ')
        return
    printNatural(n-1)
    print(n,end=' ')
    
import sys
sys.setrecursionlimit(2000) #for printing around 2000
print("Enter n:",end='')
n=int(input())
print("Natural numbers upto ",n," are:",end='')
printNatural(n)
