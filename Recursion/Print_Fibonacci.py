def getFibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    return getFibonacci(n-1)+getFibonacci(n-2)
def printFibonacci(n):
    if(n==1):
        print(0,end=' ')
        return 
    printFibonacci(n-1)
    output=getFibonacci(n)
    print(output,end=' ')
    return
print("Enter the value for n:")
n=int(input())
print("Fibonacci series upto",n,"is:",end=' ')
printFibonacci(n)
    
