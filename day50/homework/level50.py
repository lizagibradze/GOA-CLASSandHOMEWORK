# 1

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s



# 2


def lovefunc( flower1, flower2 ):
    if flower1 %2 == 0 and flower2 %2 != 0:
        return True
    elif flower1 %2 != 0 and flower2 %2 == 0:
        return True
    else:
        return False





# 3

def is_triangle(a, b, c):
    if a+b <= c or a+c <=b or b+c <= a:
        return False
    else:
        return True




# 4

def longest(a1, a2):
    new_string = set(a1 + a2)
    sort_string = sorted(new_string)
    return "".join(s for s in sort_string)



# 5

def invert(lst):
    lst2 = []
    for num in lst:
        lst2.append(num*-1)
    return lst2


# 6

def open_or_senior(data):
    res = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res
    


# 7


def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
    





# 8

def printer_error(s):
    cnt, l = 0, 0
    for c in s:
        l += 1
        if 109 < ord(c) <= 122:
            cnt += 1
    return str(cnt) + "/" + str(l)






# 9
def dna_to_rna(dna):
    dna_list = []
    for letter in dna:
        if letter == "T":
            dna_list.append("U")
        else:
            dna_list.append(letter)
    return "".join(dna_list)





  




# 10


def bmi(weight, height):
    bmm = (weight / (height * height))

    if bmm <= 18.5:
        return "Underweight"
    elif bmm <= 25.0:
        return "Normal"
    elif bmm <= 30.0:
        return "Overweight"
    else:
        return "Obese"





