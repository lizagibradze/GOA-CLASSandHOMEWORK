






# 2




def find_short(s):
    words = s.split()
    shortest = len(words[0])
    for i in words:
        if len(i) < shortest:
            shortest = len(i)
            
    return shortest




















