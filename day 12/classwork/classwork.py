# for i in range(100):
#     print("goa1" * i)


# range ---> 3 არგუმენტი ანუ: ფუნქციებს გადაეცემათ ბრჩხილებში მაგალითები.
# ეს არგუმენტებია: range(start, end, step)
# ანუ იგივეა რაც(0, 10, 1)


# start - დაწყება
# end - დასასრული
# step - ნაბიჯი(რამდენი ერთეულით გადაინაცვლოს)


# for i in range(1, 10000, 2):  # კენტი
#     print(i)

# for i in range(0, 10000, 2):  # ლუწი
#     print(i)


# გვაქვს for / while loop-i

# while statement - true/ false

# while true:
#     print("Daenerys!")

# i = 1
# while 1 > 10:
#     print("Daenerys!")



# i = 0
# while i < 10:
#     print("Daenerys!", i)
#     i = i + 1

# i = 10
# while i > 1:
#     print("giorgi", i)
#     i -= 1

# i = 1
# while i < 10:
#     print("giorgi", i)
#     i += 1


# i = 1
# while i < 10000:   # კენტი
#     print("1", i)
#     i += 1



# i = 2
# while i < 10000:   # ლუწი
#     print("1", i)
#     i += 2


# user_password = input("please enter your password: ")
# password = "123"
# while user_password != password:
#     user_password = input("please try again!: ")
# print("login succesfully!")


super_number = input("please enter super number: ")
number = "151"
while super_number != number:
    super_number = input("Please, try again!: ")
print("super number is succesful!")