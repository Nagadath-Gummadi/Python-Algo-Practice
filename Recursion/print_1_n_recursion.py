def print_1_to_n(n):
    if n==1:
        print(1)
    else:
        print_1_to_n(n-1)
        print(n)
    return
n=int(input('enter a number:'))
print('Numbers from 1 to ',n,' are:')
print_1_to_n(n)