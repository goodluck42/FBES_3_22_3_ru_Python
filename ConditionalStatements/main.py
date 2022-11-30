# + - * / ** // %

# assignment operators
# shorthand operators

a = 42

# a = a + 5

a += 5

a -= 10

a *= 2

a /= 2

a = int(a // 5)

# a = a % 2

a %= 2

a += 1
# a = 2
# a = a ** (a + 1)
a **= (a + 1)

# print(a)

# comparison operators

# > more than
# a = int(input())
# b = int(input())

# print("a =", a)
# print("b =", b)

# result: bool = a > b

# print("a > b: ", a > b)

# < less than

# print("a < b: ", a < b)

# >= (more than or equals)

# print("a >= b: ", a >= b)

# <= (less than or equals)

# print("a <= b: ", a <= b)

# == (equals)

# print("a == b", a == b)


# != (not equals)

# print("a != b", a != b)


# HubProgram

# age = int(input())
#
# if age >= 18:
#     print("You are allowed")
# else:
#     print("You are not allowed")


# Newborn, teenager, student, retired

# newborn 0-12
# teenager 13-19
# student 20-50
# retired 50+

age = int(input())

if age <= 12:
    print("newborn")
elif age <= 19:
    print("teenager")
elif age <= 50:
    print("student")
else:
    print("retired")

if age == 42:
    print("age equals 42")
else:
    print("age not equals 42")

print("1. start game")
print("2. load game")
print("3. exit game")

option = input()

if option == "start":
    print("game started")
elif option == "load":
    print("game loading")
elif option == "exit":
    print("exiting game")
else:
    print("Invalid command")

