# odd Even using XOR
def isEven(n):
    if (n ^ 1) == (n + 1):
        return True
    else:
        return False
    

num = int(input())

if (isEven(num)):
    print("Even")
else:
    print("Odd")

