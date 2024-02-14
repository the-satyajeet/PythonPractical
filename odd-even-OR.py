# odd even using OR

n = int(input())

def isEven(num):
    return True if num | 1 == num + 1 else False

if(isEven(n)):
    print("Even")
else:
    print("Odd")