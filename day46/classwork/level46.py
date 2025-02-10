

# def row_sum_odd_numbers(n):
#     return n ** 3


def math_position(x, position):

    # ! 2

    arr = []

    while x > 0:
        sum = x % position

        arr.append(sum)

        x =  x // position



    return arr [::-1]

print(math_position(5, 2))

# nashtiani gayopa aris % it





# x = 0
# y = "101"
# ზოგადი ფორმულა
# x = x * 2 + int(თიოეული y -ის წევრი)

# 




# def filter_list(l):
    
#     list = []
#     for i in l:
#         if type(i) ==  int:
#             list.append(i)
            
#     return list






def disemvowel(string_):

    result = ""
    for i in string_ :
        if i.lower(i) not in "aeiou":
            result += i
    return result 




    


def descending_order(num):


    res =  list(str(num))
    res.sort(reverse = True)
    return int(''.join(res))



