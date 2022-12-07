# try:
#     age = int(input())  # ValueError
#
#     if age >= 18:
#         credentials = "firefox/108"
#         print("allowed")
#
#     print(credentials)  # NameError
# except ValueError:
#     print("You got ValueError")
# except NameError:
#     print("Variable is undefined")
#
#
# try:
#     a = float(input())
#     b = float(input())
#
#     if b == 0:
#         print("Zero division")
#     else:
#         print(a / b)
# except ValueError:
#     print("You have entered incorrect value")
# except ZeroDivisionError:
#     print("Zero division")


# try:
#     a = int(input())
#     b = int(input())
#
#     print(a / b)
# except:
#     print("An error occurred")
#
# try:
#     a = int(input())
#     b = int(input())
#
#     print(a / b)
# except ZeroDivisionError as message:
#     print(message)


# Dont handle error
try:
    a = input()
    b = input()

    print(a, b)
except:
    print("error")
