# odd even using OR

<<<<<<< HEAD
num = int(input())

x = lambda num : True if num | 1 == num + 1 else False

if(x):
=======
n = int(input())

def isEven(num):
    return True if num | 1 == num + 1 else False

if(isEven(n)):
>>>>>>> d2edcc40a93b55a00559d4aa69334b8c9324258d
    print("Even")
else:
    print("Odd")