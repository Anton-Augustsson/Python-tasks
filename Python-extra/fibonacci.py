def fib(n):
    if(n < 1):
        return 0
    
    elif(n == 1):
        return 1
    
    else:
        return fib(n-1) + fib(n-2)

for n in range(1,11):
    #print("\n n=" + str(n) + "  ger fib=" + str(fib(n)))
    print(fib(n))
