
# 1
def first_non_consecutive(arr):
    pass

# 2

def to_alternating_case(string):
    stri = ""
    for i in string:
        if i.isupper():
             stri += i.lower()
        else:
             stri += i.upper()
    return stri

      
           
# 3
def correct(s):
    corr = ''
    for letter in s:
        if letter == '1':
            corr += 'I'
        elif letter == '5':
            corr += 'S'
        elif letter == '0':
            corr += 'O'
        else:
            corr += letter
    return corr
# 4

def is_palindrome(s):
    s = s.lower()
    return s[::-1] == s
    


# 5

def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary *10)
    if bonus == False:
        return "$" + str(salary)

# 6

def min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return [minimum, maximum]


# 7


def min_max(lst):
    min, max = lst[0], lst[0]

    for x in lst:
        if x > max:
            max = x
        elif x < min:
            min = x

    return [min, max]