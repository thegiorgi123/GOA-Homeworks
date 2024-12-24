# 1
def boolean_or_string(bool):
# თუ სადმე შეგვხვდა "თუ", "იმ შემთხვევაში", "ამ შემთხვევაში", "ან" გამოვიყენოთ if ან else
    if bool:
        return "yes"
    else:
        return "no"

print(boolean_or_string(True))
# bool = True
print(boolean_or_string(False))
# bool = False

print("----------------------------------------")
# 2
def string_to_integer(_str):
    return int(_str)
print(string_to_integer("1234"))
print(string_to_integer("605"))
print(string_to_integer("1405"))
print(string_to_integer("-7"))    

# 3
def arr_sum_second_way(arr):
def arr_sum_first_way(arr):
    counter = 0
    for num in range(len(arr)):
        counter += num
    return counter
        
print(arr_sum_first_way([1, 5.2, 4, 0, -1]))
# arr = [1, 5.2, 4, 0, -1]
print(arr_sum_second_way([1, 5.2, 4, 0, -1]))
print("----------------------------------------")