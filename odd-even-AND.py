# odd even using AND 
def isEven(n):
    if n&1 == 0:
        return True
    else:
        return False
    
num = int(input())

print("Even") if isEven(num) else print("Odd")