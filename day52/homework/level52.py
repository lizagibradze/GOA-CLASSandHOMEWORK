
# 1

def multi_table(number):
    return







# 2


def print_array(arr):
    ar = ""
    for i in arr:
        s += str(i) + ","
    return s[0:len(s)-1]








# 3



def string_clean(s):
    n = ''
    for i in s:
        if i not in '0123456789':
            n += i
    return n







# 4




def remove_consecutive_duplicates(s : str) -> str:
    s = s.split(" ")
    arr = []
    for i in range(len(s)):
        if s[i] != s[i-1] or i == 0:
            arr.append(s[i])
    return " ".join(arr)



# 5


