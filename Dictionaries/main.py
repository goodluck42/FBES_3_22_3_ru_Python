# student1 = {
#     "name": "Vadim",
#     "surname": "Siga",
#     "gender": True,
#     "age": 20,
#     "grades": [12, 10, 12, 11, 9],
# }
#
# student2 = {
#     "name": "Seymur",
#     "surname": "Bagirov",
#     "gender": True,
#     "age": 21,
#     "grades": [12, 10, 12, 11, 12],
# }
#
# student2["age"] -= 1
#
# print(student2["age"])
#
# students = []
#
# students.append(student1)
# students.append(student2)
#
# print(students[1]["surname"])  # Bagirov

#####################################
# list, dict

# student = {
#     "name": "Vadim",
#     "surname": "Siga",
#     "gender": True,
#     "age": 20,
#     "grades": [12, 10, 12, 11, 9],
# }

# POP
# student.pop("gender")

# del student["gender"]

# print(student)

# KEYS & VALUES

# keys = student.keys()
#
# for k in keys:
#     print(k)
#
# values = student.values()
#
# print('-' * 12)
#
# for v in values:
#     print(v)


# for k in student:
#     print(f"key = {k} | value = {student[k]}")

# ITEMS

# for k, v in student.items():
#     print(f"k = {k} | v = {v}")

games = [
    {
        "publisher": "Activison",
        "name": "game1"
    },
    {
        "publisher": "Activison",
        "name": "game1"
    }
]


def my_sum(a, b=5):
    print(a + b)


my_sum(10, 6)


def get_values():
    a = 5
    b = 42

    return a, b


res1, res2 = get_values()

print(res1)
print(res2)