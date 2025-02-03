
# 1 dav wina



def remove_duplicate_words(s):
    s = s.split(" ")
    arr = []
    for word in s:
        if arr.count(word) >= 1:
            continue
        else:
            arr.append(word)
    return " ".join(arr)



# itvlis ramdenjer gameorda sityvebi . count
# sadac gamotovebaa mand daxlichavs sityvas.
# continue anu skip




































