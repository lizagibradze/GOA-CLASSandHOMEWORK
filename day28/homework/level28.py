# 1
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"



# 2

def remove_char(s):
    return s[1:-1]

print(remove_char("hello"))
print(remove_char("hiiiii"))


# 3


def string_to_number(s):
    return int(s)

print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("-7"))

   




# 4


def no_space(x):
    return x.replace(" ","")

print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
print(no_space("8aaaaa dddd r     "))




# 5


def sum_array(a):
    return sum(a)

print(sum_array([1, 5.2, 4, 0, -1]))
print(sum_array([]))
print(sum_array([-2.398]))








