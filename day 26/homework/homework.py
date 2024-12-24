# 1
from turtle import *

def draw_triangles():
    speed(100)
    x_cord = -750
    y_cord = 0

    for i in range(1, 121):
        penup()
        goto(x_cord, y_cord)
        pendown()
        if i % 2 == 1:
            color('green')
            forward(20)
            left(120)
            forward(20)
            left(120)
            forward(20)
            left(120)
        elif i % 2 == 0:
            color('blue')
            forward(20)
            left(120)
            forward(20)
            left(120)
            forward(20)
            left(120)
        x_cord += 30

        if x_cord >= 750:
            x_cord = -750
            y_cord -= 30
    exitonclick()

draw_triangles()




# 2

# def hello_world():
#     print("Hello")

# hello_world()

# # 3
# def even_or_odd(num):
#     if num % 2 == 0:
#         return "რიცხვი ლუწია!"
#     else:
#         return "რიცხვი კენტია!"
# print(even_or_odd(20))




# # # 4
# # from turtle import*


# # SQUARE
# def square():
#     forward(200)
#     left(90)
#     forward(200)
#     left(90)
#     forward(200)
#     left(90)
#     forward(200)
#     end_fill()
    
# square()


# # TRIANGLE
# def triangle():
#     forward(100)
#     right(90)
#     forward(50)
#     left(180)
#     forward(50)
#     right(90)
#     forward(100)
#     left(120)
#     forward(200)
#     left(120)
#     forward(200)

    
    

# triangle()



# # RHOMBUS
# def rhombus():
#     forward(100)
#     left(135)
#     forward(150)
#     left(45)
#     forward(100)
#     left(135)
#     forward(150)

# rhombus()

# # PS თვითოეულის შესამოწმებლად კომენტარში მოაქციეთ სამი ფიგურის ფუნქციიდან ორი, რათა ისინი ერთმანეთში არ აირიოს
    
# exitonclick()
