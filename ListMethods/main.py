## APPEND

# numbers = []
#
# numbers.append(42)
#
# numbers.append(13)
#
# print(numbers)

## POP

# numbers = [randint(-100, 100) for _ in range(10)]  # list comprehension
#          0   1   2   3   4   5
# numbers = [10, 20, 30, 15, 42, 13]
#
# print("before pop =", numbers)
# print("len before =", len(numbers))
#
# index = 3
#
# numbers.pop(index)
# numbers.pop(4)
#
# numbers.pop()
#
# print("after pop =", numbers)
# print("len after =", len(numbers))

## REMOVE
# from random import randint
#
# users = [randint(0, 10) for _ in range(10)]  # list comprehension
#
# print("before remove =", users)
#
# value = int(input("Enter user id = "))

## REMOVE ERROR HANDLING
# try:
#     users.remove(value)
# except ValueError as message:
#     print(message)

## IN

# if value in users:
#     users.remove(value)
# else:
#     print("User not found")

# print("after remove =", users)


## INDEX
##            0   1   2   3   4
# numbers = [42, 13, 90, 10, 20]
# print(numbers)
# target = int(input())
#
# try:
#     index = numbers.index(target)
#     print("index of", target, "is", index)
#
#     numbers[index] *= 2
#     print(numbers)
# except ValueError:
#     print("value not found")


## COPY

# numbers = [42, 13, 10]
# copy = numbers.copy()
#
# copy.append(-10)
# numbers.append(37)
#
# print(numbers)
# print(copy)


## COUNT

# numbers = [10, 10, 42, 13, 10, 20, 30]
#
# number_count = numbers.count(10)
#
# print("ten count =", number_count)

## INSERT

# #         0        1        2
# books = ["Book1", "Book2", "Book3"]
#
# books.insert(0, "BookA")
# books.insert(1, "BookB")
#
# print(books)

# books = [("Book1", 10), ("Book2", 13), ("Book3", 42)]
#
# books.insert(0, ("BookA", 20))
# books.insert(1, ("BookB", 10))
#
# print("Book name =", books[1][0])
# print("Book count =", books[1][1])

## REVERSE

# numbers = [10, 42, 13, 20, 30]
#
# numbers.reverse()
#
# print(numbers)


## CLEAR

# numbers = [1, 20, 30, 42, 13]
#
# numbers.clear()
#
# numbers.append(10)
# numbers.append(42)
#
# print(numbers)


##

# from random import randint
# import random
#
# numbers = [random.randint(-50, 50) for _ in range(10)]
#
# print("before sort =", numbers)
#
# # numbers.sort(reverse=True)  # descending
# numbers.sort()  # ascending
#
# print("after sort =", numbers)

## EXTEND

# numbers = [10, 32, 42]
# numbers2 = [89, 13, 90]
#
# numbers.extend(numbers2)
#
# print(numbers)

## + OPERATOR ON LISTS

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# list3 = list1 + list2
#
# print("list1 =", list1)
# print("list2 =", list2)
# print("list3 =", list3)

# INDEXES
#          0   1   2   3   4     5   6
# numbers = [20, 42, 90, 13, 66] # 90  13
#
# numbers.append(90)
# numbers.append(13)
#
# number = numbers[len(numbers) - 1]
#
# print(number)
#
# last_number = numbers[-1]
#
# print(last_number)

# SLICES

numbers = [10, 40, 42, 13, 90, 80, 20]

slice1 = numbers[1:4]

print("slice1 =", slice1)

slice2 = numbers[:3]

print("slice2 =", slice2)

slice3 = numbers[3:]

print("slice3 =", slice3)

slice4 = numbers[:]
# slice4 = numbers.copy()

print("slice4 =", slice4)

slice5 = numbers[::2]

print("slice5 =", slice5)

slice5 = numbers[::-1]

print("slice5 =", slice5)
