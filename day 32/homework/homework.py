# N1

def string_to_arr(arr):
    return arr.split()

string = "I love arrays they are my favorite"
result = string_to_arr(string)
print(result)


print("---------------------------------------------")

# N2
 
def string_to_number(arr):
    return int(arr)

string = "1234"
result = string_to_number(string)
print(result)

print("---------------------------------------------")

# N5
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    max = max(num_list)
    min = min(num_list)
    return min, max

nums = "1, 2, 3, 4, 5"
result = high_and_low(nums)
print(result)