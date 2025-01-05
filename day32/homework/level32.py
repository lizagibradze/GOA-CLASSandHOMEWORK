# 1



def string_to_array(s):
    if s == "":
        return ['']
    else:
        return s.split()




# 2

def string_to_number(s):
    return int(s)

print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("-7"))




# 3


def string_to_number(s):
    return int(s)

print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("-7"))

# (igive)

# 4

def fake_bin(x):
    
    result = ""
    
    for number in x:
        num = int(number)
        
        if num < 5:
            result += '0'
        else:
            result += '1'
    
   
    return result



# 5



def high_and_low(_str):
    res = _str.split(" ")

    arr = []
    for i in res:
        arr.append(int(i))

    max_num = max(arr)
    min_num = min(arr) 

    return f"{max_num} {min_num}"




print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3")) 
print(high_and_low("1 2 -39 33 11 223 -4 13"))



