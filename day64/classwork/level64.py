
# class HumanPerson:
#     x = 0

















class HumanPerson:
    def _init_(self, name, age):
        self.name = name
        self.age = age



def my_name(self):
    return self.name













def my_name_age(self):
    return f"მე ვარ {self.n} ვარ {self.age}"




h1 = HumanPerson("Davit", 20)
print(h1.name)
print(h1.age)
print(h1.my_name())
print(h1.my_name_age())
print(h1)



h2 = HumanPerson("liza", 15)
print(h1.my_name_age())
print(h2.upper())











# 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def lower(self):
        return self.name.lower()

p1 = Person("liza", 15)

print(p1.lower())







class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"
    
    def name_surname_age(self):
        return f" my name is {self.name} my surname is {self.surname} i am {self.age}"

p1 = Human("liza", "gibradze", 15)
print(p1.name_surname_age())





# dict_1 = {
#     "x": 1,
#     "y":2,

# }



# print(dict_1["name"])







# h1 = HumanPerson()
# print(h1.x())


