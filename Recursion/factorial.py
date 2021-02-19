def factorial(n):
    if n==1:
        return 1
    inter=factorial(n-1)
    return inter*n
print("Enter Value for n:")
n=int(input())
print("Factorial of",n,"is :",factorial(n))
