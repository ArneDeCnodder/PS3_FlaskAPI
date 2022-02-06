# UNPACKING ARGUMENTS

def add(x, y):
    return x+y
# nums = [3,5]
# print(add(*nums))
nums = {'x':15,'y':25}
print(add(**nums))

# UNPACKING KEYWORD ARGUMENTS

# def named(**kwargs):
#     print(kwargs)

# named(name='arne',leeftijd=15) #output is een dictionary
# nu omgekeerd
def named(name,leeftijd):
    print(name,leeftijd)

details = {"name":"Arne","leeftijd":15}
named(**details)

# OBJECT ORIENTED PROGRAMMING

class Student:
    # methods with two underscores are magic methods, you don't have to call it yourself
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.grades = (100,95,93,78,99)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return (f"Naam van de persoon is {self.name} met leeftijd {str(self.age)}")
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


nieuwe = Student("BOBBIE",15)
nieuwe2 = Student("ROB",20)
# print(nieuwe.name)
# print(nieuwe.grades)

# print(nieuwe.average())
# print(Student.average(nieuwe2))

# magic methods __str__ and __repr__

Arne = Student('Arne',23)
print(Arne) 


class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
        
    def add_item(self, name, price):
        self.items.append({'name':name,'price':price})

    def stock_price(self):
        items = self.items
        total = 0
        for item in items:
            total+= item['price']
        return total



