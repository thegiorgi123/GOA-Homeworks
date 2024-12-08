# def ---- definiton
# definition - ჩაშენებული სიტყვა, მაგალითად : if, else, for, while, elif, or and, def...
# def ქმნის ფუნქციას

def daenerys():
    print("daenerys targaryen rightful hair of seven kingdoms")

daenerys()
daenerys()
daenerys()


from turtle import *

# def walk():
#     forward(200)
# def walkback():
#     back(200)

# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
# left(90)
# walk()
# right(90)
# walk()
# walkback()

from turtle import *

# def walk():
#     forward(200)
# def fall_back():
#     back(200)
# def go_and_back():
#     walk()
#     fall_back()
    
# go_and_back()


# -----------------------------------

# def walk():
#     forward(200)
# def fall_back():
#     back(200)
# def go_and_back():
#     for i in range(5):
#         walk()
#         fall_back()
# go_and_back()

# -----------------------------------

# პარამეტრები / Parameters იწერებიან ფუნქციის შიგნით

def walk():
    forward(200)
def fall_back():
    back(200)
    

def go_and_back(გამეორება): #აქ ვწერთ მნიშვნელოას
    for i in range(გამეორება):
        walk()
        fall_back()
go_and_back(10) #მნიშვნელობა იღებს იმდენ რაოდენობას რასაც აქ დავწერთ, ეს კი შეგვიძლია სხვაგანაც გამოვიყენოთ, მაგალითად:
go_and_back(50)

exitonclick()

