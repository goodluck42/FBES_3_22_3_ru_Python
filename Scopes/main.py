#############
# a = int(input())
#
# if a > 0:
#     value = 13
#
# print(value)

#############

# def add(a, b):
#     result = a + b
#
#     return result

#############

# counter = 0


# def print_counter():
#     print(counter)
#
#
# def increment_counter():
#     global counter
#     # counter = counter + 1
#     counter += 1
#
#
# increment_counter()
#
# print_counter()


#############

# def cook(*args):
#     print(f"args len = {len(args)}")
# #    print(args[0])
# #    print(args[1])
# #    print(args[2])
#     for item in args:
#         print(item)
#
#
# cook("Вода", "Морковь", "Чеснок", "Зелень")
#
def fn(*args):
    for item in args:
        print(item)

values = [10, 20, 30, 40, 50]
fn(values)  # fn([10, 20, 30, 40, 50])
fn(*values)  # fn(10, 20, 30, 40, 50)


# def fn(a, b, c):
#     print(a + b + c)
#
#
# fn(c=13, b=42, a=20)
############
# def fn(**kwargs):
#     print(kwargs["blablabla"])  # 10
#     print(kwargs["value"])  # 42
#     print(kwargs["ololo"])   # 9
#
#
# fn(blablabla=10, value=42, ololo=9)
