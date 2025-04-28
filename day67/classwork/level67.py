


# class car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def __str__(self):
#         return f"{self.brand} {self.model} {self.year}"
    
#     def car_info(self):
#         return f"  the cars brand is {self.brand} the model is {self.model}  its from {self.year}"

# p1 = car("carrrr", "hhhh", 1212 )
# print(p1.car_info())





class kratos:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def __str__(self):
        return f"{self.name} {self.weapon}"


    def info(self):
        return f" im {self.name} {self.weapon}"
    
    def skill_points(self, points):
        return f"skill points: {points}"



k1 = kratos("kratos", "leviathan")
print(k1.info())
print(k1.skill_points(200)) 



# class Atreus(kratos):
#     pass


class Atreus(kratos):
    def __init__(self, name, age, weapon):
        self.name = name
        self.weapon = weapon
        self.age = age

        # kratos.__init__(self, age, weapon)


        # super().__init__(self, age, weapon)

        self.shape_shifter = True



    def __str__(self):
        return f" age: {self.age} weapon:{self.weapon}"




a1 = Atreus("ae ", 14, "bow and arrow")
print(a1)
print(a1.skill_points(50))
print(a1.shape_shifter)












# 1

def two_sort(array):
    array.sort()
    ww = array[0]
    result = "***".join(ww)
    return result

#  2



class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" {self.name} {self.age}"
    
c1 = cat("catt" , 5)
print(c1)







# 3



class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" {self.name} {self.age}"
    
c1 = cat("catt" , 5)
print(c1)


