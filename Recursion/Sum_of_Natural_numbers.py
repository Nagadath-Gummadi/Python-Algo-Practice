def naturalSum(n):
    if(n==1):  
        return 1
    inter=naturalSum(n-1)
    return n+inter

print("Enter a natural number:")
n=int(input())
print("Sum upto ",n," is:",naturalSum(n))
