#booleans in python
from urllib.parse import uses_relative


print(5==4)
print(5!=4)

#if statements
movies_watched = {"the matrix","green book","her"}
while True:
    
    user_movie = input("Enter something you've watched recently (use 'stop' to stop): ").lower()

    if user_movie == 'stop':
        break

    if user_movie in movies_watched:
        print("Jij hebt deze film al gezien!")
    else:
        print(f"Nice de film {user_movie}, heb je nog niet gezien!")
        movies_watched.add(user_movie)

# loops

vrienden = ['Rutger','Maarten','Lukas','Yorbe']

for vriend in vrienden:
    print(vriend)

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)


# -- Part 2, must be completed before submitting! --
while True:
    user_input = input("Enter your choice: ").lower()
    if user_input == "a":
        print("Add")
    elif user_input=='q': 
        print("Quit")
        break
    else:
        print("Choose another input!")
