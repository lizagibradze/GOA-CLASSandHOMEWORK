



# def digitize(n):
#     n.split()
#     n.reverce()
#     return n







# def digitize(n):
#     digits = []
#     for digit in str(n)[::-1]: 
#         digits.append(int(digit))
#     return digits

# print(digitize(1325))




# def digitize(n):
#     digits = []
#     for digit in str(n): 
#         digits.append(int(digit))
#     return digits[::-1]
# print(digitize(1325))



# def ixvis_tolma():
#     return "იხვის ტოლმა"

# print(ixvis_tolma())




# def ixvis_tolma(number1, number2, number3):
#     return number1 + number2 +number3

# print(ixvis_tolma(1))


# def digitize(n):
#     lst = []
#     for i in str(n):
#         lst.append(int(i))
#         return lst[::-1]
    




# def get_count(sentence):
#     vowels = "aeiou"

#     count = 0

#     for char in sentence:
#         if char in vowels:
#             count += 1


#     return count

# print(get_count("aaueo iio"))





def filter_list(l):

    result = []

    for item in l:
        if type(item) != str:
            result.append(item)
    

    return result
