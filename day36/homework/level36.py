# 1

def filter_list(l):
    result = []
    

    for item in l:
        if type(item) != str:
            result.append(item)
    return result



# 2
def square_digits(num):
    num_str = str(num)
    
    result = []
    
    for digit in num_str:
        result.append(str(int(digit) ** 2))
    
    return int(''.join(result))






#4


def find_short(s):
    words = s.split()
    shortest = len(words[0])
    
    for word in words:
        if len(word) < shortest:
            shortest = len(word)
    
    return shortest



#5

def solution(text, ending):
    len_ending = len(ending)
    if len_ending > len(text):
        return 0 
    last_words_of_text = text[len(text)-len_ending:]

    return last_words_of_text == ending

    # return text[len(text)-len_ending:]


    

# 3



def get_middle(s):
    if len(s) % 2 == 0:
        start = int(len(s)*.5) - 1
        end = int(len(s)*.5) + 1
        return s[start:end]
    
    return s[int(len(s)*.5)]
#vigebt sigrdzis naxevars 

        # s[int(len(s)*.5)]














