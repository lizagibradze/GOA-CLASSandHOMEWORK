
# 1


def high_and_low(numbers):
    
    x = numbers.split(" ")

    arr = []
    for char in x:
        arr.append(int(char))
    return " ".join([str(max(arr)), str(min(arr))])


















# 2





def validate_pin(pin):

    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    return False

        

# an


def validate_pin(pin):

    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False

        









# 3

# sum() ---> ციფერების სიის ჯამს გვაძჟლევს მაგ: sum( [1,2,3] ) ---> 6   







def odd_or_even(arr):
    
    if (sum(arr)% 2 == 0):
        return "even"
    else:
        return"odd"
        








# 4

def solution(nums):
    if not nums:
        return []
    return sorted(nums)










# 5





def greet(name): 
    
    return f"Hello {name.capitalize()}!" 

























