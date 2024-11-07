# N1

name = input("შემოიტანეთ თქვენი სახელი: ")
result = " "
for i in name:
    result += i + " "
print(result)

# N2

num1 = int(input("შემოიტანეთ საწყისი რიცხვი: "))
num2 = int(input("შემოიტანეთ საბოლოო რიცხვი: "))

for num in range(num1, num2 + 1):
    if num % 2 == 0 and num % 3 == 0:
        print("ეს რიცხვები არის 2-სა და 3-ის ჯერადი: ")
    else:
        print("ეს ციფრები არაა 2-სა და 3-ის ჯერადები")

# N3

result = 0
for i in range(5):
    number = int(input("გთხოვთ შემოიტანოთ ციფრი: "))
    result += number
average = result / 5
print(average)

# N4

for i in range(-100, 100):
    if i > 0:
        print(i)

N5

num = int(input("შემოიტანეთ ციფრი: "))
number = 0
while num > number:
    num = int(input("შემოიტანეთ ციფრი: "))
print(" ")

# N6.

rows = 8
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i, end = "")
    print(" " * (rows + i) + "*" * i)
