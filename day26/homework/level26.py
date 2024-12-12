
# def green()
#     if kenti :
#         green
#     else:
#         red





# 1


from turtle import *

def draw_triangle(color, size):
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(size)
        left(120)
    end_fill()

def draw_triangles():
    speed(0)
    size = 50
    for i in range(1, 121): 
        x = (i % 10) * 60 - 300
        y = -(i // 10) * 60 + 300
        penup()
        goto(x, y)
        pendown()
        if i % 2 != 0:
            draw_triangle("green", size)
        else:
            draw_triangle("blue", size)

if __name__ == "__main__":
    draw_triangles()
    done()




# 2


def hello_world():
    print("hello world")

hello_world()






#3

def even_or_odd(n):
    if n % 2 == 0:
        print("არ არის კენტი")
    else:
        print("არის კენტი")

even_or_odd(11) 
even_or_odd(6)




# #4


def shape1():
    print("******")
    print("******")
    print("******")
    print()


def shape2():
    print("     *")
    print("    ***")
    print("  *******")
    print("***********")
    print("     *")
    print("     *")
    print()




def shape3():
    print("*******")
    print(" *******")
    print("  ********")
    print("    ********")
    print()




def draw_figures():
    for _ in range(120):
        shape1() 
        shape2()  
        shape3()  

draw_figures()









