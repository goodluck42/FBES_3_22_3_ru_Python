import random

# base_id = 0
# max_id = 12000
#
# target_id = int(input())
#
# while base_id < max_id:
#     if base_id == target_id:
#         print("User found")
#         break
#     base_id += 1


# base_id = 0
# max_id = 12000
#
# target_id = int(input())
#
# user_found = False
#
# while base_id < max_id:
#     if base_id == target_id:
#         user_found = True
#         break
#     base_id += 1
#
# if user_found:
#     print("User found")
# else:
#     print("Not found")




# i = 0
#
# while i < 42:
#     if i == 13:
#         break
#         print("Hello im break operator")
#     print(i)
#     i += 1
#
# print("end of loop")



# base_id = 0
# max_id = 12
#
# while base_id < max_id:
#     random_age = random.randint(6, 100)
#     print("User age", random_age)
#
#     if random_age < 18:
#         print("not allowed")
#         base_id += 1
#         continue
#
#     print("Confirmed age; You are allowed; Your age", random_age)
#
#     base_id += 1

# i = 0
#
# while i < 5:
#     if i == 2:
#         break
#
#     if i == 3:
#         print("i == 3")
#         i += 1
#         continue
#
#
#     print(i)
#     i += 1
#
# print("end of loop")



# i = 0
#
# while i < 5:
#     i += 1
#     print(i)
#     if i == 2:
#         print("i equals 2")
#     else:  # don't do that
#         continue

while True:
    try:
        num1 = int(input("Enter first number: "))
        op = input()
        num2 = int(input("Enter second number: "))

        if op == "+":
            print(num1 + num2)

        print("Type 0 to exit")

        user_input = input()

        if user_input == "0":
            break
    except:
        print("Error")