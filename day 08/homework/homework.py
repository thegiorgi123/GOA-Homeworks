# # N1.
# age = int(input("შეიყვანეთ თქვენი ასაკი: "))
# if 13 < age < 19:
#         print("თქვენ ხართ თინეიჯერი")
# else:
#     print("თქვენ არ ხართ თინეიჯერი")


# N2.
score = int(input("შეიყვანეთ თქვენი ქულა(1-10): "))

is_A = score >= 9
is_B = 8 <= score < 9
is_C = 7 <= score < 8
is_D = 6 <= score < 7
is_F = 6 > score

print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)


# N3.

a = True
b = False

print(a and a)
print(a and b)
print(b and b)
print(b and a)
print(a or a)
print(a or b)
print(b or b)
print(b or a)

# N4.

a = int(input("შემოიტანეთ ერთნიშნა მთელი რიცხვი: "))
b = int(input("შემოიტანეთ ერთნიშნა მთელი რიცხვი: "))

print(a == b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a != b)

# N5.

a = 5
b = 6
c = 8

is_a_greatest = a > b and a > c
is_b_middle = ( b > a and b < c) or ( b > c and b < a )
is_c_least = c < a and c < b

print(is_a_greatest)
print(is_b_middle)
print(is_c_least)

 # N6.

score = int(input("შეიტანეთ მთელი რიცხვი. (1-100)"))

is_pass = score >= 50
is_high_pass = 75 < score < 95
is_perfect = score == 100
is_failing = score < 50

print(is_pass)
print(is_high_pass)
print(is_perfect)
print(is_failing)

# N7.
# P = True
# Q = False

# P_and_not_Q = P 