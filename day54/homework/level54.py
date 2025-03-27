
# 1


def sort_by_length(arr):
    z = 0
    aa = []
    while len(aa) != len(arr):
        for a in arr:
            if len(a) == z:
                aa.append(a)
        z += 1
    return aa 




    
# 2


def sequence_sum(begin_number, end_number, step):
    oo = 0
    for i in range(begin_number, end_number + 1, step):
        oo += i

    return oo




# 3


def series_sum(n):
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    
    sum = 1.0
    for i in range(1,n):
        sum += 1 / (1 + 3 * i)
    return '%.2f' % sum
    


# 4


def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n


# 5



def two_oldest_ages(ages):
    maxx = max(ages)
    ages.remove(maxx)
    return [max(ages), maxx]
