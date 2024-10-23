# 1

name = input("what is your name?: ")

res = ""

for i in name:
    res += i + " "
print(res)





# 2


start = int(input("start: "))  
end = int(input("end: "))      

found = False  


for i in range(start, end):  
        print("ეს ციფრები არის " + str(i) + " - 3-ისა და 2-ის ჯერადები") 
        found = True 

if not found:
    print("not found")


# 3

result = 0

for i in range(5):
 number= int(input("enter an number:"))
 result += number

average = result / 5

print("result" , result )
print("average" , average)



# 4

for i in range(-100, 101):
 if i > 0:
    print(i)
 












