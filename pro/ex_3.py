import math
c = 50
h = 30
v = []
items = [x for x in input().split(',')]
for d in items:
    v.append(int(math.sqrt(2*c*float(d)/h)))
print(v)