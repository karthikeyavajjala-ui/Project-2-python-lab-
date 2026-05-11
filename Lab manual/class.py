class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)   # ✅ prints John
del p1           # delete after using it
print(p1.name)