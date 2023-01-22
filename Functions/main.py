# def get_negatives(numbers):  # numbers - parameter
#     result = []
#
#     for item in numbers:
#         if item < 0:
#             result.append(item)
#
#     return result
#
#
# list1 = [10, -20, -50, 40, 42, -13, -90, 62]
# list2 = [-1, -5, 42, 30, -77, 74]
#
# result1 = get_negatives(list1)
# result2 = get_negatives(list2)
#
# print(result1)
# print(result2)

def divide(a, b=1):
    if b == 0:
        return "Infinity"

    result = a / b

    return result

a = int(input())
b = int(input())

result1 = divide(a, b)

print(result1)




# res = is_even(20)
#
# print(res)