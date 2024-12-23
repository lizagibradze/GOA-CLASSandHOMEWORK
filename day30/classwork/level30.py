



# def starts the function.

# say_hello is the name of the function.

# print("Hello!") is what the function does.

# anu say_hello() iqneba printshi rac weria

# print: Just displays a message, but you can't use it in further calculations or operations.

# return: Gives you a value that you can save, use in other parts of the code, or manipulate.


# return:
# def say_hello():
#     return "Hello!" 

# message = say_hello()
# print(message)



# Training on Convert boolean values to strings 'Yes' or 'No'.


#tu dadme shegvxvda "tu" "im shemtxvevashi" "am shemtxvevashi" "an" gamoviyenot if: else

# def bool_to_word(bool):
#     if bool:
#         return "Yes"
#     else:
#         return"No"



# test case

# bool = True
# print(bool_to_word(True))
# print(bool_to_word(False))





# 3


# def string_to_integer(_str):
#     return _str

# print(string_to_integer("1234"))
# print(string_to_integer("605"))
# print(string_to_integer("1405"))
# print(string_to_integer("-7"))

# #           parmeter
# def arr_sum(arr):
#     pass


# print(arr_sum([1, 5.2, 4, 0, -1]))

# arr = [1, 5.2, 4, 0, -1]


# def arr_sum_first_way(arr):
#     counter = 0
#     for num in arr:
#         # counter = counter + num
#         counter += num
#     return  counter

# def arr_sum_second_way(arr)
#     counter = 0 #1 + 5.2
#                 # len of arr ---->5
#     #         len(anu length) of arr --5
#     for num in range( len(arr)):
#         counter += arr[i]
#     return  counter



# print(arr_sum_first_way([1, 5.2, 4, 0, -1]))

# print(arr_sum_second_way([1, 5.2, 4, 0, -1]))

# 4
# def no_space(x):
#     return x.replace(" ","")

# print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
# print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
# print(no_space("8aaaaa dddd r     "))

# 5


# def sum_array(a):
#     return sum(a)

# print(sum_array([1, 5.2, 4, 0, -1]))
# print(sum_array([]))
# print(sum_array([-2.398]))




# Highest and Lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# Input: "1 2 3 4 5" => Output: "5 1"
# Input: "1 2 -3" => Output: "2 -3"
# Input: "1 2 -39 33 11 223 -4 13" => Output: "-39 223"





# def min_and_max_num(numbers):
#     num = list(int, num.split())
#     highest = max(num)
#     lowest = min(num)
#     return f"({highest} {lowest})"
# print(min_and_max_num)


#roca chven gvinda ramis wakitxva igi aucileblad unda gadavaqciot list ad

def high_lowest(_str):
    res = _str.split(" ")

    arr = []
    for i in res:
        arr.append(int(i))

    max_num = max(arr) # yvelaze dids
    min_num = min(arr) # yvelaze pataras

    return f"{max_num} {min_num}"




print(high_lowest("1 2 3 4 5")) # "5 1"
print(high_lowest("1 2 -3")) #"2 -3"
print(high_lowest("1 2 -39 33 11 223 -4 13"))# 1 2 -39 11 223 -4 13










# print("--------------format--------------")

# numb = 1
# name = "george"
# #           num gavastringot
# result = str(numb)+ " " + name + " and this is the end."

# result_1 = "{} {} and this is the end.".format(numb,name)

# result_2 = f"{numb} {name} and this is the end."


# print(result)
# print(result_1)
# print(result_2)












