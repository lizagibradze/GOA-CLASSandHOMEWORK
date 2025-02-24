


# 1



def remove_duplicate_words(s):
    s = s.split(" ")
    arr = []
    for word in s:
        if arr.count(word) >= 1:
            continue
        else:
            arr.append(word)
    return " ".join(arr)



# 2

def stray(arr):
    for num in arr:
        if arr.count(num) == 1:

            return num
        



# 3

def solution(nums):
    if not nums:
        return []
    return sorted(nums)
    




# 4

def capitals(word):

    indices = []

    for i in range(len(word)):
        if word[i].isupper():
            indices.append(i)

    return indices




# 5

def factorial(n):
    j = 1
    for i in range(1, n+1):
        j *= i
    return j
