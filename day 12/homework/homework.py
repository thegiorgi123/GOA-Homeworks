# N1.
for i in range(1, 50,2):
    print(i)

# N2.
for i in range(2):
    print("*" * 3)

print("-----------------")

# N3.
for i in range(5):
    print("*" * 3)

print("-----------------")

# N4.

for num1 in range(5):
    for num in range(4):
        print(num1, num)
        
# N5.
name = input("შემოიტანეთ თქვენი სახელი: ")
surname = input("შემოიტანეთ თქვენი გვარი: ")
age = input("შემოიტანეთ თქვენი ასაკი: ")
while int(age) < 18:
    print("თქვენი ასაკი არ აკმაყოფილებს ბარიერს, უნდა იყოთ 18 წლის, ან მეტი.")
    age = input("შემოიტანეთ თქვენი ასაკი: ")
gmail = input("შემოიტანეთ თქვენი მეილი: ")
password = input("შექმენით პაროლი: ")
password2 = input("გაიმეორეთ პაროლი: ")
while password2 != password:
    print("პაროლები ერთმანეთს არ ემთხვევა, გთხოვთ ცადოთ თავიდან!")
    password = input("შექმენით პაროლი: ")
    password2 = input("გაიმეორეთ პაროლი: ")
print("გილოცავთ, რეგისტრაცია წარმატებით გაიარეთ!")
