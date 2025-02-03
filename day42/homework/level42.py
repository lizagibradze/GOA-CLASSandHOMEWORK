
# 1
def sum_mix(arr):
    
    total = 0

    for num in arr:
        total += int(num)

    return total










# 2



def double_char(s):
    
    result = ""

    for char in s:
        result += char*2

    return result









# 3
def array_plus_array(arr1,arr2):
    

    count_1 = 0
    for i in arr1:
         count_1 += i
    count_2 = 0
    for i in arr2:
       count_2 += i

    return count_1 + count_2




# 4


def reverse_words(s):

    split_word = s.split(" ")[::-1]
    return " ".join(split_word)






# 5

def sum_str(a, b):
    if a:
        num1 = int(a)
    else:
        num1 = 0

    if b:
        num2 = int(b)
    else:
        num2 = 0

    return str(num1 + num2)


