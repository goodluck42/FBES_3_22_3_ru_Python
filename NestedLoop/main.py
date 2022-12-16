# i = 0
#
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#
#     print(i)
#     i += 1

#
# [    j0 j1 j2
#   i0[1, 2, 42],
#   i1[4, 0, 2],
#   i2[9, 2, 3]
# ]
# matrix[i0][j2] => 3

# i = 0
#
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1

# i = 0
# found = False
#
# while i < 3 and not found:
#     j = 0
#     while j < 3:
#         if i == 2 and j == 1:
#             print("loop break")
#
#             found = True
#             break
#         print("i =", i, "j =", j)
#         j += 1
#     i += 1


# i = 0

# while i < 3:
#     j = 0
#     while j < 3:
#         if i == 0 and j == 2:
#             j += 1
#             print("continued")
#             continue
#         print("i =", i, "j =", j)
#         j += 1
#     i += 1


# i = 0
#
# while i < 10:
#     if i >= 1 and i <= 5:
#         i += 1
#         continue
#
#     print(i)
#     i += 1


i = 0

while i < 5:
    j = 0
    while j < 5:
        if i == 2 or j == 2:
            print("   ", end="")
        else:
            print("*  ", end="")
        j += 1

    print()
    i += 1



# Do not do that
# print("* * * * *")
# print("*       *")
# print("*       *")
# print("*       *")
# print("* * * * *")