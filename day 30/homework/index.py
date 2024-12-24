# N1
arr = [1, -3, 3, -7, 5, -14]
sum_of_arr = sum(arr)
print(sum_of_arr)


print("----------------------------------")

# N2

arr = [-1, 2, 3, -5, 7]
square_of_arr = []
for i in arr:
    square_of_arr.append(i ** 2)
print(square_of_arr)


print("----------------------------------")

# N3

def sum_of_arr(num):
    if not num:
        return 0
    return sum(num)
arr = [1, 5.2, 4, 0, -1]
empty_arr = sum_of_arr([])
print("the sum of arr is:", sum(arr))
print("the sum of arr is:", empty_arr)



print("----------------------------------")

# N4

def average_of_arr(num):
    if not num:
        return 0
    return sum(num) / len(num)

arr = [1, 2, 3, 4, 5, 6]

result = average_of_arr(arr)
empty_result = average_of_arr([])
print("average of arr is:", result)
print("average of arr is:", empty_arr)



print("----------------------------------")

# N5
