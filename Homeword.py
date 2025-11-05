# James Nickell

# Period 7

# Logical Operators Practice

# 9:50 - 



'''

hint = 'Your hint is a top lane league champ, who is the king.'



password = "Sett"

guess = str(input('What is your first guess at the character?: '))

if guess == "Sett":
    print("Great guess, well done")
if not guess == "Sett":
    print(hint)
    
'''


'''

age = int(input("How old are you?: "))

license = str(input("Do you also have your license?: "))



if age >= 21 and license == 'Yes':
    print('You are old enough to rent a car :)')
else:
    print("You cannot rent a car, no no no.")
    
'''




favorite_champ = str(input('Who is your favorite champion in all of league of legends?: '))


if favorite_champ == 'Shaco' or favorite_champ == 'LeBlanc':
    print("You are incorrect, please pick another champ :c")
else:
    print("Thats a pretty good choice, please enjoy your game :)")