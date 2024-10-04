# N1.
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if 13 < age < 19:
        print("თქვენ ხართ თინეიჯერი")
else:
    print("თქვენ არ ხართ თინეიჯერი")

# N2.
score = int(input("შეიყვანეთ თქვენი ქულა(1-10): "))

is_A = score >= 9
is_B = 8 <= score < 9
is_C = 7 <= score < 8
is_D = 6 <= score < 7
is_F = 6 > score

print()