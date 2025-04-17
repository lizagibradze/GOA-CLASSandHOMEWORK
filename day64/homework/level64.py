

# 1



class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"
    
    def car_info(self):
        return f"  the cars brand is {self.brand} the model is {self.model}  its from {self.year}"

p1 = car("carrrr", "hhhh", 1212 )
print(p1.car_info())




# 2



class student:
    def __init__(self, name , age , grade ):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name} {self.age} {self.grade}"
    
    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False

p1 = student("gog", 1, 6 )
print(p1.is_passing())


# 3


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"
    
    def bark(self):
        return "woof"

p1 = dog("reee", 2)
print(p1.bark())


# 4

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 

    def __str__(self):
        return f"{self.width} {self.height}"
    
    def area(self):
        return f" the width is {self.width} and the height is {self.height}"

p1 = rectangle( 2, 5)
print(p1.area())




# 5




class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year} "
        
    def info(self):
        return f"the title is {self.title}, the author is {self.author} it is from {self.year}"

p1 = book("book", "someone", 1232) 
print(p1.info())       
