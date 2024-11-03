


 #1

age = int(input("your age: "))

if age < 10 :
    print("less than 10")
else:
    print("more than 10")



# 2

number = int(input("enter number: "))


if number % 2 == 0 :
    print("ლუწი")
else: 
    print("კენტი")




# 3

number = int(input("enter number: "))

if number < 0:
    print("არ არი დადებითი")
else:
    print("დადებითი")



# 4

number = int(input("enter number: "))

numbertwo = int(input("enter number two: "))

if  number == numbertwo :
    print("same")
else:
    print("not same")
    


# 5


number = int(input("enter number: "))

if number % 2 == 0 and number > 100 :
    print("რიცხვი არის 100-ზე მეტი და ლუწი")
else:
    print("რიცხვი არ არის 100-ზე მეტი და ლუწი")


# 6

number = int(input("enter number: "))

if number % 5 == 0 or number % 10 == 0 :
    print("არის 5-ის ან 10-ის ჯერადი")
else:
    print(" არ არის 5-ის ან 10-ის ჯერადი")