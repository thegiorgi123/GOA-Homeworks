# name = input("შემოიტანეთ თქვენი სახელი!")
# surname = input("შემოიტანეთ თქვენი გვარი!")
# age = int(input("შემოიტანეთ თქვენი ასაკი!"))
# school = input("შემოიტანეთ კლასი!")
# fav_color = input("შემოიტანეთ საყვარელი ფერი!")

# list = [name, surname, age, school, fav_color]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])

# print("-----------------------------------")
# string = input("შემოიტანეთ სიტყვა")
# string = len(string)
# print("სთრინგის სიგრძეა", string)

# N3
print("-------------------------------------------------")

arr = ["davit", "gio", "davit", "gio", "davit"]
counter = 0
is_count = "davit"
for char in arr:
    if char == is_count:
        counter += 1
print(counter)

# N5
list = [5, 10, 15, 20]
average = sum(list)
print("საშუალოა : ", average)
