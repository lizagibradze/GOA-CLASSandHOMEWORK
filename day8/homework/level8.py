age = int(input("რამდენი წლის ხარ: "))

between = 13 < age < 19

print(between)


# დავალება 2


grade = int(input("შენი ნიშანი: "))

is_A = grade >=9


print(is_A)


3

is_B =  8 <= grade < 9

print(is_B)


4

is_C =7 <= grade < 9

print(is_C)


5

is_D =6 <= grade < 7

print(is_D)


6

is_F = grade <6

print(is_F)


# დავალება3



true_variable= True
false_variable = False


print("True or True:", true_variable or true_variable) 

print("True or False:", true_variable or false_variable)

print("False or True:", false_variable or true_variable)

print("False or False:", false_variable or false_variable)


# დავალება4

num1 = int(input("პირველი ციფრი: "))

num2 = int(input("მეორე ციფრი: "))

print(num1==num2)
print(num1<num2)
print(num1>num2)
print(num1<=num2)
print(num1>=num2)
print(num1!=num2)




# დავალება5

a = 5
b =10
c = 2

is_a_greatest = a > b and a > c 
is_b_middle = (b > a and b < c) or (b < a and b > c)
is_c_least = c < a and c < b

print("Is a the greatest?",is_a_greatest) #თუ a არის უდიდესი ამ სამიდან.
print("Is b the middle value?",is_b_middle ) #თუ b არის საშუალო მნიშვნელობა 
print("Is c the least?",is_c_least)#თუ c არის სამიდან უმცირესი.

# დავალება6


score = 60
is_pass = score >=50


is_high_pass = 75 <= score < 90

is_perfect = score == 100

is_failing = score <50

print("pass?", is_pass)
print("high pass?",is_high_pass)
print("perfect?", is_perfect)
print("failing?", is_failing)




# დავალება7

P = True
Q = False

P_and_not_Q = P and not Q 
not_P_and_Q = not P and Q  
P_xor_Q = (P and not Q)or(not P and Q)


print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)



