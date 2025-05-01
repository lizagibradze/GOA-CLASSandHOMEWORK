
# 1

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" {self.name} {self.age}"
    
d1 = dog("dogg" , 5)
print(d1)


# 2

class student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.grade = grade
        self.subject = subject

    def __str__(self):
        return f"{self.name} {self.grade} {self.subject}"
    
    def student_info(self):
        return f"  my name is {self.name} i study {self.subject} my grade is {self.grade}"

p1 = student("liza", "math", 10 )
print(p1.student_info())


# 3

# 4

# 5
