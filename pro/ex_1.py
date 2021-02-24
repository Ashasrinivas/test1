l = []
for i in range(2000, 3001):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))
print(l)


# factorial function

import math
n = int(input("enter the number : "))
result = math.factorial(n)
print("factorial of ", n,  "is", result)

n = int(input("enter the number: "))
result = 1
for i in range(n, 0, -1):
    result = result*i
print("factorial of ", n, "is", result)

# recursive function : function call itself
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter the number : "))
result = fact(n)
print(result)