# + - * / // **, %
# =, *, **=, ...
# <, >, >=, <=, ==, !=
# and, or, not
# Logic table
# 0 - False
# 1 - True

# AND
# 0 and 1 => 0
# 1 and 0 => 0
# 1 and 1 => 1
# 0 and 0 => 0

# OR
# 0 or 1 => 1
# 1 or 0 => 1
# 1 or 1 => 1
# 0 or 0 => 0

# NOT
# 1 not

# age = int(input("Enter age: "))  # age = 20
# role = input("Enter role: ")  # student


# if age >= 18 and role == student:
# if age >= 18 and role == teacher:
# if age >= 18:
# if age >= 18:
#     if role == "student" or role == "intern":
#         print("Ur a student and ur allowed")
#     elif role == "teacher":
#         print("Teacher access allowed")
#     else:
#         print("Ur guest")
# else:
#     print("not allowed")

# print(1 and 0 or 1) #  1
# print(1 and 0 and 1 and 1 and 1)
# print(10 or 20 or 30 or 40)


num1 = 10
num2 = 15

if num1 == 0 or num2 == 0:
    print("Success")


a = 10

print(not (a % 2 == 0))