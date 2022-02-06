# list comprehensions
nummers = [1,3,6]
doubled = [num * 2 for num in nummers]
print(nummers, doubled)

vrienden = ["Ralf","Rutger","Maarten","Ronald","Lukas"]

R_vrienden = [vriend for vriend in vrienden if vriend.startswith("R") ]
print(vrienden, R_vrienden)

# dictionary

vriend_leeftijd = {"Maarten":25,"Rutger":22,"Lukas":21}
vriend_leeftijd['Yorbe'] = 21
print(vriend_leeftijd)

vrienden = [
    {"leeftijd":25,"naam":"Arne"},
    {"leeftijd":15,"naam":"Jeole"},
    {"leeftijd":65,"naam":"Raf"}
]
print(vrienden[0]['naam'])

# functions

def say_hello(name):
    print(f"Goedendag, {name}!")

naam = input('Wat is je naam?: ')
say_hello(naam)

# Complete the function by making sure it returns 42. .
def return_42():
    # Complete function here
    return 42
    # pass  # 'pass' just means "do nothing". Make sure to delete this!

# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.
def my_function(first, last):
    return first*last
