class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"name of the employee is {self.name} and salary is {self.salary}")

class developer(employee):
    def __init__(self,name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus
    
    def display(self):
        print(f"developer name: {self.name}, salary of the developer is {self.salary} and bonus of the developer is {self. bonus} ")


p1=developer("Bibek", 100000, 20000)


    