# int, str, bool, float, tuple, list
####################################
# ValueType = неизменяемые
# int
# str
# bool
# float
# tuple

############################
# ReferenceType = изменяемые
# list

# a = 42
# b = a
#
# a = 13
#
# print(hex(id(a)))
# print(hex(id(b)))
#################################
# a = []
# b = a
#
# a.append(13)
# b.append(42)
#
# print(hex(id(a)))
# print(hex(id(b)))
#
# print(a)  # 13
# print(b)  # 13 42

## INDEX
# text = "Hello"
#
# index = text.index('l')
#
# print(index)

##
list1 = []

list1.append(20)

print(list1)

##

# text = "Hello"  # HELLO
#
# uppercase = text.upper()
#
# print(uppercase)
# print(text)

###############
## ESCAPE SEQUENCES

# text = "Hello\n"
#
# print(text)
# print(len(text))
#
# print("Hello\n\t\tWorld")
# print("Helloy")

#####
# list2 = [1, 2, 42, 13, 10, 20]
#
# i = 0
#
# while i < len(list2):
#     print(list2[i])
#
#     i += 1

#############################
# text = "Goodbye cruel world"

# text[0] = 'H' ## Ошибка
# print(text[0])
# result = text[:7]

# print(result)

# for i in text:
#     print(i)

####################
## STRING FORMAT
# a = 10
# b = 42
#
# print(a, "+", b, "=", a + b)
# print(f"{a} + {b} = {a + b}")

## CONCATENTAION & REPLICATION

# text1 = "Hello"
# text2 = "World"
#
# text3 = text1 + text2
#
# text4 = text1 * 3
#
# print(text3)
# print(text4)

text = "Hello 123"

if text.isdigit():
    print("IT IS DIGIT")

# text.isalnum()





for char in text:
    print(type(char))
