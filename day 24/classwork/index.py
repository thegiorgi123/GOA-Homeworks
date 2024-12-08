# # nums = [4, 5, 6]
# # message = "giorgi", str(10) + "wlis aris"   
# # new_message = "giorgi {3} wlis aris".format(10, 40, 16, 10+6)

# # newest_message = "giorgi {y} wlis aris {x}".format(x = 10, y = 16)



# # print(message)
# # print(new_message)
# # print(newest_message)

# sentence = "წითელი ვაშლი გაგორდა {x} ml-თი".format(x = 50)
# print(sentence)

# # ან
# sentence2 = f"წითელი ვაშლი გაგორდა {50} ml-თი"
# print(sentence2)

# # arr = ["group", "48", "aaa", "bbb"]
# # print(arr)
# name = "group 48 aaa bbb"
# split_name = name.split(" ")
# print(split_name)

# print("-----------------------------------")

# name2 = "giorgi, aaa, bbb, ccc"
# split_name2 = name2.split(",")
# print(split_name2)

# print("-----------------------------------")

# arr = ["grou48", "abcd", "bcde", "aaaa"]
# joined_arr = "!".join(arr)
# print(joined_arr)




# tolma = "იხვის ტოლმა არ არის ბატის ტიოლმა"
# splited_tolma = tolma.split(" ")
# print(splited_tolma)
# joined_tolma = ",".join(splited_tolma)
# print(joined_tolma)




# name = "giorgi tlashadze"
# updated_name = name.split(" ")
# updated_name = "VASHLI".join(updated_name)
# print(updated_name)


example = "hellofromtheothersie"
example_1 = example.replace("o", "HELP").split("HELP")
print(example_1)


# -------------------------------------------

example_1 = "giORgI".upper()
example_2 = "giORgI".lower()
example_3 = "giORgI".capitalize() # მხოლოდ პირველი სიტყვის პირველ ასოს ადიდებს
example_4 = "giORgI".title()  #ყველა სიტყვის ყველა პირველ ასოს ადიდებს
print(example_1)
print(example_2)
print(example_3)
print(example_4)
