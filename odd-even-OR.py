# odd even using OR

num = int(input())

x = lambda num : True if num | 1 == num + 1 else False

if(x):
    print("Even")
else:
    print("Odd")