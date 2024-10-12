# >
# <
# =
# >=
# <=
# ==   - უდრის
# !=   - არ უდრის
# boolean მონაცემთა ტიპები.
# არსებობს ორი მონაცემთა ტიპი - true/false

# # print(10 > 11) - false
# # print(10 < 11) - true
# print(10 == 10)

# print(15 != 9)


# # True - ყოველთვის 1
# # False - 0








# print(5 > 2)
# print(134 > 51)

# print(661 < 512)
# print(81 < 123)

# print(51 >= 51)
# print(13 >= 23)

# print(234 <= 252)
# print(52 <= 52)

# print(57 == 51)
# print(72 == 72)

# print(823 != 723)
# print(512 != 123)

# Logical Operators
# and
# or

# and არის აუცილებლობა! რომ იყოს true ყოველთვის
print(True and True) # ყოველთვის თრუა თუ მაინც 1 თრუ აქვს
print(False and True) # ყოელთვის ფოლსია თუ ერთი ფოლს აქვს
print("Hello" and "HI") # ყოველთვის მარჯვენა მხარე გამოაქვვს

print("------------------------------------------")

# or ის შემთხვევაში ერთი true თუ იყო გარეული აუცილებლად true იქნება, დანარჩენი ყოველთვის false.
print(True or False) # true
print(False or True) # true
print(False or False) # False

# num1 = 1 == 1 # true
# num2 = 2 == 2 # true
# print(num1 and num2)

num1 = 1 == 1 # true
num2 = 2 == 1 # false
print(num1 or num2)