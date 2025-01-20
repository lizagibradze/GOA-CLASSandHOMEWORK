

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










# def password(st):
#     if len(st) < 8:
#         return 0
    
#     upper_rule = 0
#     lower_rule = 0
#     digit_rule = 0

#     for char in st:
#         if char == char.upper():
#             upper_rule= 1
#         if char == char.lower():
#             lower_rule = 1
#         if char.isdigit():
#             digit_rule = 1

#     return upper_rule + lower_rule + digit_rule == 3






def password(st):
    if len(st) < 8:
        return 0
    
    upper_rule = 0
    lower_rule = 0
    digit_rule = 0

    for char in st:
        if char.isupper():
            upper_rule = 1
        if char.islower():
            lower_rule = 1
        if char.isdigit():
            digit_rule = 1

    return (upper_rule + lower_rule + digit_rule) == 3






def is_isogram(string):
    string = string.lower()  # Convert to lowercase to ignore case
    
    for i in range(len(string)):
        if string[i] in string[i + 1:]:  # Check if current character exists in the rest of the string
            return False  # If a duplicate is found, return False
    return True 


def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) > 1:
            return False
    return True


