# items = [x for x in input().split(',')]
# items.sort()
# print(items)


# s = input("enter the sentence : ")
# l = []
# l.append(s.upper())
# print(l)

# l = []
# while True:
#     s = input("enter the sentence : ")
#     if s:
#         l.append(s.upper())
#     else:
#         break
# for sentence in l:
#     print(sentence)

# s = input("enter the sentence :  ")
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(set(words))))


# s = input()
# d = {"DIGITS" : 0, "LETTERS" : 0}
# for i in s:
#     if i.isdigit():
#         d["DIGITS"]+= 1
#     elif i.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
# print("LETTERS : ", d["LETTERS"])
# print("DIGITS:", d["DIGITS"])

#
# s = input()
# d = {"UPPER" : 0, "LOWER": 0}
# for i in s:
#     if i.isupper():
#         d["UPPER"] += 1
#     elif i.islower():
#         d["LOWER"] += 1
#     else:
#         pass
# print("UPPER :", d["UPPER"])
# print("LOWER :", d["LOWER"])

# l = input("enter the numbers : ")
# num = [x for x in l.split(",") if int(x)%2!= 0]
# print(",".join(num))

# def checkval(n):
#     if n % 2 == 0:
#         print("it is even")
#     else:
#         print("it is odd")
# checkval(7)

#
# def printdict():
#     d = dict()
#     d[1] = 1
#     d[2] = 2**2
#     d[3] = 3**2
#     print(d)
# printdict()
#
# def printdict():
#     d = {}
#     for i in range(1,21):
#         d[i] = i ** 2
#     print(d)
# printdict()
#
# def printdict():
#     d = {}
#     for i in range(1, 21):
#         d[i] = i ** 2
#     for v in d.values():
#         print(v)
# printdict()

# def printTuple():
#     l = []
#     for i in range(1, 21):
#         l.append(i**2)
#     print(tuple(l))
# printTuple()

#
# from functools import reduce
# li = [7,2,3]
# result  =  reduce((lambda x, y : x + y), li)
# print(result)

# total = 1
# li = [1,2,3,4]
# for i in li:
#     total = total * i
# print(total)


# l = []
# num = int(input("enter number of elements : "))
# for i in range(1, num + 1):
#     element = int(input("enter first number : "))
#     l.append(element)
#     result = reduce(lambda x, y : x + y, l)
# print(l)
# print(result)

# l = [1000, 2000, 300000, 500000, 988865, 345678, 9876543]
# n = int(input("enter the number : "))
# l.sort()
# print(l)
# print(l[-n:])

# l = [1, 2,3,4,5,6,7,8]
# for i in l:
#     if i % 2 == 0:
#         print(i, end = " ")

# num = [x for x in l if x %2 == 1]
# print(num)

# num = list(filter(lambda x : (x % 2 == 0), l))
# print(num)

# num = [x for x in range(1, 11) if x %2 == 0]
# print(num)
# num1 = list(filter(lambda x :(x % 2 == 0), range(1, 31)))
# print(num1)

# start = int(input("enter the starting number : "))
# end = int(input("enter the ending number : "))
# for i in range(start, end+1):
#     if i % 2 == 1:
#         print(i, end = " ")

# l = [-12, -12, -45, 56, 78, 90, 98, -987, -98]
# for num in l:
#     if num <= 0:
#         print(num)
# num = []


# l = [1,2,3,4]
# for i in l:
#     if (i == 4):
#         print("yes,", i, "is in the above list")
    # else:
    #     print("no,", i, "is not there in the above list")


# l = [1,2,3,4,5,-67,-89,-987,-45678,-87654]
# for i in l:
#     if i <= 0:
#         print(i)
# num = [x for x in l if x <= 0]
# print(num)
# num1 = list(filter(lambda x : x <= 0, l))
# print(num1)

# l = []
# for i in range(1, 20):
#     if i >= 0:
#         l.append(i)
# print(l)

num = list(filter(lambda x : x <= 0, range(1,20)))
print(num)