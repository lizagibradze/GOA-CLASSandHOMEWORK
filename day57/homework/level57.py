
# 1


def vowel_one(s):
    vowel = "aeiouAEIOU"
    res = ""

    for char in s:
        if char in vowel:
            res += "1"
        else:
            res += "0"
    return res


# 2
# def reduce_fraction(fraction):





# 3
def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalpha() or char.isdigit():
            count += 1
    return count


# 4


def solution(text, ending):
    len_ending = len(ending)
    if len_ending > len(text):
        return 0 
    last_words_of_text = text[len(text)-len_ending:]

    return last_words_of_text == ending

# 5




# def elimination(arr):
#     eee = []

#     for num in arr:
#         if num in eee:
#             return num
#         eee.append(num)
#     return None






