
# 4


def remove_consecutive_duplicates(s : str) -> str:
    s = s.split(" ")
    arr = []
    for i in range(len(s)):
        if s[i] != s[i-1] or i == 0:
            arr.append(s[i])
    return " ".join(arr)






# 1


def number(bus_stops):
    peopleam= []
    for i in bus_stops:
        peopleam.append(i[0]-i[1])
    return  sum(peopleam)



# an

def number(bus_stops):
    count = 0
    for arr in bus_stops:
        count += arr[0]
        count -= arr[1]

    return count







# 2



def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
             return True
        else:
                return False
    else:
        return False


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False



# an


def is_leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:


# an


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    












