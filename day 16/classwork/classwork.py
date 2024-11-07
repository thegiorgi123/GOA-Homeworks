# #  list - სია, იწერება [] - ის გამოყენებით, მაგ : ["giorgi", "hi", "hello" ]

# # arr = ["Giorgi", "HELLO", "HI"]
# # print(arr[2], arr[1])

# movies = ["lord of the rings", "Game of thrones", "Spiderman", "The Witcher", "Batman"]

# print(movies[0] + "," +  movies[1] + "," + movies[2] + "," + movies[3] + "," + movies[4] + ".")
# print(movies[-1])

# name = "Giorgi"
# print(name[0])

# # თუ უკნიდან გვინდა არჩევა მაშინ მოვდივართ პირიქით : -1, -2, 03...


# name = "oashdkajshdkajhsdpyhlihlkqwjebkqwbrli"
# print(name[-7])



# rows = 8
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * i, end = "")
#     print(" " * (rows + i) + "*" * i)


num = 5
for i in range(num):
    print(' ' * (num - i - 1), end='')
    print('*' * (2 * i + 1))