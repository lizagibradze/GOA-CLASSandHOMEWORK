
# 1

def double_char(s):
    
    result = ""

    for char in s:
        result += char*2

    return result


# 2

def get_age(age):
    return int(age[0])

# 3
def feast(beast, dish):
  
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False


# 4

def array_plus_array(arr1,arr2):
    
    total = 0

    for num in arr1:
        total += num
    for num in arr2:
        total += num

    return total


# 5


def solution(number):
    if number < 0:
        return 0
    
    total_sum = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    
    return total_sum











