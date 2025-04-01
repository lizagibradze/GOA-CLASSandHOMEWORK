
# 1

def solution(text, ending):
    len_ending = len(ending)
    if len_ending > len(text):
        return 0 
    last_words_of_text = text[len(text)-len_ending:]

    return last_words_of_text == ending

# 2

def even_or_odd(s):
    even = 0
    odd = 0
    for char in s:
        digit = int(char)
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
    
    if even > odd:
        return "Even is greater than Odd"
    elif odd > even:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"







# 3

def even_numbers(arr, n):
    even = []
    
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    
    return even[-n:]

# 4

def vowel_indices(word):
    vowel = "aeiouyAEIOUY"
    res = []
    for i in range(len(word)):
        if word[i] in vowel:
            res.append(i + 1)
    return res


# 5

# def geometric_sequence_elements(a, r, n):
    










