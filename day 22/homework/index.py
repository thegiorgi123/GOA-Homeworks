# 1
list_of_names = ["გიორგი", "დავითი", "გიორგი", "ლუკა", "თამაზი", "დავითი", "ნიკოლოზი", "გიორგი"]
name_to_count = "გიორგი"
counter = 0
for name in list_of_names:
    if name == name_to_count:
        counter += 1
print(counter)

print("---------------------------------------------")


# 2
list_of_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_letters.reverse()
print(list_of_letters)

print("---------------------------------------------")

# 3

list_of_letters = [1, 2, 3, 4, 5]
print(list_of_letters * 5)

print("---------------------------------------------")

# 4

insert_arr = ["python", "css", "javascript"]
insert_arr.insert(2, "giorgi")
print(insert_arr)

print("---------------------------------------------")

# 5

arr = [1, 2, 3, "გიორგი", 4, 5, "გიორგი", 6, 7, "გიორგი"]
name = "გიორგი"
counter = arr.count(name)
print("ელემენტი მეორდება: ", counter, "-ჯერ")
element_to_remove = arr.remove(name)
element_to_remove = arr.remove(name)
element_to_remove = arr.remove(name)
print("განახლებული სიაა: ", arr)

print("---------------------------------------------")