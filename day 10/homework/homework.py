# N1
age = int(input("რა არის თქვენი ასაკი?: "))
is_a_teenager = 10 <= age <= 19
print(is_a_teenager)

print("----------------")

is_not_a_teenager = 19 > age < 10
print(is_not_a_teenager)

# N2
print("----------------")

temperature = float(input("შემოიტანეთ ტემპერატურა(ცელსიუსში): "))

farenheit = (temperature * 9/5) + 32
print("თქვენს მიერ შემოტანილი ტემპერატურა ფარენჰეიტში არის: " + str(farenheit) + " ფარენჰეიტი.")

# N3
print("----------------")

num1 = 2
num2 = 5
num3 = 7

print(num1 > num2)
print(num2 > num3)
print(num2 >= num1)

num1 = 123
num2 = 241
num3 = 152

print((num1 > num2) or (num1 < num3))
print((num1 > num3) or (num1 > num2))
print((num3 == num2) and (num3 <= num1))

# N4
print("----------------")

for i in range(7):
    print("*" * i)

# N5
print("----------------")

age = 20
print(age > 5)
print(age >= 6)
print(age == 20)
print(age != 6)