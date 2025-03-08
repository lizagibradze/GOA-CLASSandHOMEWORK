
# 1

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


# an 

def find_next_square(sq):
    if (sq ** 0.5 % 1 == 0 ):
        return (sq ** 0.5 + 1) **2
    return -1
    


        # return 4.1 ** .5 % 1
    



# 2

def min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return [minimum, maximum]



# 3

# def series_sum(n):




