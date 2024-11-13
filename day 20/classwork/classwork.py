# arr = ["davit", "gio", "davit", "gio", "davit"]
# print(arr[2:])
# print(len(arr))

# # len - სიის ელემენტების რაოდენობას ითვლის
# for i in range(len(arr)):
#     print(arr[i])

new_arr = [1,23,3,4,5,56,6,6,6,7,7,78,2,342,3423,4234212,1,312,31,341]
for i in range(len(new_arr)):
    if new_arr[i] % 2 != 0:
        new_arr[i] = "კენტი"
print(new_arr)