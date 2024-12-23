


# 1

def positive_sum(arr):
#    [1,2,3,4,5]
    counter = 0 #15
    
    for i in arr:
        counter += i

    return counter

#2


def square_sum(arr):
    counter = 0 
    for i in arr:
        counter += i ** 2
        return counter







# 3

def litres(time):
    return int(time * 5)




# 4

def greet():
    return "hello world"

# 5

def count_positives_sum_negatives(arr):
    counter_of_positives = 0 
    sum_of_negatives = 0
    for element in arr:
        if element >0:
            counter_of_positives += 1
        else:
            sum_of_negatives += element
    return [counter_of_positives, sum_of_negatives]
