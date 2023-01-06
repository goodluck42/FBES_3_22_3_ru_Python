import random
my_list = []

x = 5
my_list.append(random.randint(-10, 10))
my_list.append(x)
my_list.append(3)
my_list.append(4)
my_list.append(13)
my_list.append(42)

for value in my_list:
    print(value)