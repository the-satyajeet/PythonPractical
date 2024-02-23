def fibonacciRecursive(n):
    if (n <= 1):
        return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

def printFibonacciRecursive(n):
    
    for i in range(n):
        print(f"{fibonacciRecursive(i)}", end=" ")
        
n = 10
printFibonacciRecursive(n)