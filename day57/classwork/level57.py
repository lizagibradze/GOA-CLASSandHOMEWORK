
# dav

def solution(text, ending):
    return text.endwith(ending)






# 1





# 2

def longest_word(string_of_words):
    r = string_of_words[0]
    for i in string_of_words.split():
        if len(i) >= len(r):
            r=i
    return r


# an

def longest_word(string_of_words):

    string_of_words = string_of_words.split(" ")
    long_word = string_of_words[0]
    
    for i in string_of_words:
        if len(long_word) <= len(i):
            long_word = i
        return long_word
# ?


