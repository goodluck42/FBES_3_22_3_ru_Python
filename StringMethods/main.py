# immutable (неизменяемый) (ValueType)
# int, bool, str, float, tuple

# mutable (изменяемый) (ReferenceType)
# list, dict, str (immutable)

# a = 42
# b = 42

# print(id(a))
# print(id(b))

# l1 = []
# l2 = []
#
# print(id(l1))
# print(id(l2))

# \t \n - Escape sequences
# str1 = "Hello"
# str2 = "Friend"
#
# print(f"{str1} {str2}")

## UPPER & LOWER
# text = "Some text"
#
# result = text.upper()
# # result = text.lower()
#
# print(result)


## REPLACE

# text = "Some text text"
#
# result = text.replace("text", "fruits", 1)
#
# print(result)

## IS METHODS

# text = "Sometext"
#
# if text.isalpha():
#     print("alpha")
# else:
#     print("not alpha")
#
# if text.islower():
#     print("islower")
# else:
#     print("not is lower")
#
# text2 = "900"
#
# if text2.isdigit():
#     print("digit string")
# else:
#     print("not digit string")

## CAPITALIZE

# text = "today is a nice day. have fun."
#
# result = text.capitalize()
#
# print(result)

## STARTSWITH & ENDSWITH

# text = "today is a nice day. have fun."
#
# if text.startswith("today"):
#     print("starts")
# else:
#     print("not starts")
#
# if text.endswith('.'):
#     print("ends")
# else:
#     print("not ends")

# SPLIT & JOIN

# text = "hello friend how are you"
#
# words = text.split(" ")
#
# print(words)
#
# print(len(words))
#
# result = "_".join(words)
#
# print(result)

# camelCase
# PascalCase
# kebab-case
# snake_case


## FIND

text = "hello friend how are you"

idx = text.find("friend")

print(idx)