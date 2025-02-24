



# isogramshi ar meordeba asoebi . banani- ar ari isogrami. vashli - ki

def is_isogram(string):

    arr = []
    for i in range(10):
        arr.append(i)
    return arr
    

# es 1 xazshia

    return [i for i in range(10) if i >= 1   ]


#  for i in range(10) 0-idan 10-amde itvlis
# 



# 1
def is_isogram(string):
    arr = [i for i in string.lower() if string.lower().count(i) > 1]
    if (len(arr)> 1):
        return False
    else:
        return True
    


    





























