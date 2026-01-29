class Person:
    def __init__(self, name: str, age: int):
        self.name =name
        self.age = age
    
    def  __repr__(self):
        return f"Person{self.name!r}, {self.age}"
    def __eq__(self, other):
        return isinstance(other, Person) and (self.name, self.age) == (other.name, other.age)
    
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person{self.name!r}, {self.age}"
    
    def __eq__(self, other):
        return isinstance(other, Person) and (self.name, self.age) == (other.name, other.age)
    
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person{self.name!r}, {self.age}"
    
    def __eq__(self, other):
        return isinstance(other, Person) and (self.name, self.age) == (other.name, other.age)
    
class Person: 
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person{self.name!r}, {self.age}"
    
    def __eq__(self, other):
        return isinstance(other, Person) and (self.name, self.age) == (other.name, other.age)
    

