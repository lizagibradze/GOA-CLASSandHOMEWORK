



def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y != 0:
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"
    





# def calculator(x, y, op):
#     if op == "+":
#         return x + y
#     if op == "-":
#         return x - y
#     if op == "*":
#         return x * y
#     if op == "/":
#     if y != 0:
#         return x / y
#     else:
#         return "unknown value"
 


#  2

def plural(n):
    if n == 1:
        return False
    else:
        return True



# 3

def am_i_wilson(n):
    return str(n) in["5", "13", "563"] 
    



# 4
def get_volume_of_cuboid(length, width, height):
    return length * width * height









