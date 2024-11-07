number = int(input("შემოიტანეთ მთელი რიცხვი: "))
if number >= 10:
    print("დამაკმაყოფილებელია!")
else:
    print("შემოტანილი ციფრი ნაკლებია 10-ზე!")
    
print("----------------------------------------------")

number = int(input("შემოიტანეთ მთელი რიცხვი რიცხვი!: "))
if number % 2 == 0:
    print("რიცხვი ლუწია!")
else:
    print("რიცხვი კენტია!")
    
print("------------------------------------------------")

number = int(input("შემოიტანეთ ნებისმიერი რიცხვი!: "))
if number >= 0:
    print("რიცხვი დადებითია!")
else:
    print("რიცხვი უარყოფითია!")
    
print("-------------------------------------------------")

number = int(input("შემოიტანეთ რიცხვი!: "))
number2 = int(input("შემოიტანეთ მეორე რიცხვი!: "))
if number == number2:
    print("თქვენი შემოტანილი რიცხვები ტოლია!")
else:
    print("თქვენი შემოტანილი რიცხვები არაა ერთმანეთის ტოლი!")
 
 
print("---------------------------------------------------")
number = int(input("შემოიტანეთ რიცხვი!: "))
if (number > 100) and (number % 2 == 0):
    print("რიცხვი დამაკმაყოფილებელია!")
else:
    print("რიცხვი არადამაკმაყოფილებელია!")

print("-----------------------------------------------------")

number = int(input("შემოიტანეთ რიცხვი!: "))
if number % 5 == 0 or number % 10 == 0:
    print("რიცხვი არის 5-ის ან 10-ის ჯერადი.")
else:
    print("რიცხვი არ არის 5-ის ან 10-ის ჯერადი.")
    

print("-------------------------------------------")

num = 5
for i in range(num):
    print(' ' * (num - i - 1), end='')
    print('*' * (2 * i + 1))

print("-------------------------------------")


num1 = int(input("შემოიტანე ციფრი!: "))
num2 = int(input("შემოიტანე ციფრი!: "))
num3 = int(input("შემოიტანე ციფრი!: "))
num4 = int(input("შემოიტანე ციფრი!: "))
num5 = int(input("შემოიტანე ციფრი!: "))
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print("-------------------------------------")
list = [num1, num2, num3, num4, num5]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

print("-----------------------------------------")
# BOSS LVL

numbers = [9,5,94,711,52,96,71,8]
min_number = numbers[0]
for number in numbers:
    if number < min_number:
        min_number = number
print("ყველაზე პატარა ციფრია: ", min_number)

print("----------------------------------------------")

user1 = input("enter your answer: ")
user2 = input("enter your answer: ")
user3 = input("enter your answer: ")
user4 = input("enter your answer: ")
arr = [user1, user2, user3, user4, "lomi"]
for item in arr:
    print(item)


arr = [9, 5, 6, 2, 17, 182]
min_num = arr[0]
for number in arr:
    if number < min_num:
        min_num = number
print(min_num)



                   