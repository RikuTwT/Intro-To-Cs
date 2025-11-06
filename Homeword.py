# James Nickell

# Period 7

# Logical Operators Practice

# ~45 minutes


# Not
'''
# Your hint for the password
hint = 'Your hint is a top lane league champ, who is the king.'


# The password
password = "Sett"
 # Input to guess the password
guess = str(input('What is your first guess at the character?: '))


# What happens if youu get it wrong or right
if guess == "Sett":
    print("Great guess, well done")
if not guess == "Sett":
    print(hint)
    
'''

# And 
'''
# Asks for your age and if you have a license

age = int(input("How old are you?: "))

license = str(input("Do you also have your license?: "))


# If you fit the age and license requirement then it fills out
if age >= 21 and license == 'Yes':
    print('You are old enough to rent a car :)')
else:
    print("You cannot rent a car, no no no.")
    
'''


# Or
'''

# Asks your favorite champ
favorite_champ = str(input('Who is your favorite champion in all of league of legends?: '))

# Does something for you answer
if favorite_champ == 'Shaco' or favorite_champ == 'LeBlanc':
    print("You are incorrect, please pick another champ :c")
else:
    print("Thats a pretty good choice, please enjoy your game :)")
''' 


# And or
# Define your lane and your favorite league champ

lane = str(input('What lane do you enjoy playing the most?: '))

champ = str(input("What champ do you like playing in that lane?: "))


# Picks what to say based off what you say
if (lane == "Jungle" or lane == "Jg" or lane == "jg" or lane == "jungle" or lane == "Jungler" or lane == "jungler") and champ == "Viego" or champ == "Lillia":
    print("You are awesome, I appreciate your taste in champions.")
elif (lane == "Jungle" or lane == "JG" or lane == "Jg" or lane == "jg" or lane == "jungle" or lane == "Jungler" or lane == "jungler") and champ == "Shaco" or champ == "shaco" or champ == "Kayn" or champ == "kayn":
    print("Dishonor on you and your family you skilless pumpkin eater")
else:
    print("You're alright IG, maybe pick a better lane/champ..")
    
