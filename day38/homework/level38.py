


#1



def boolean_to_string(b):
    if b:
        return "True"
    else:
        return "False"



# 2

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2



#3


def maps(a):
    result = []
    
    for num in a:
        result.append(num * 2)
    return result

#4



def digitize(n):
    n_str = str(n)[::-1]
    
    digits = []
    for digit in n_str:
        digits.append(int(digit))
    return digits


# 5
def abbrev_name(name):
    words = name.split()
    return f"{words[0][0].upper()}.{words[1][0].upper()}"
