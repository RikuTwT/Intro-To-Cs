# James Nickell

# Period 7

# Functions Practice

# 2:18 - 2:49

# Defines the "High", "Mid", and "Low" range of numbers
def high():
    print("That's a high number")
def mid_range():
    print("That's a somewhat high number")
def low():
    print("That's a low number")

# Asks for a number
number = int(input("What is your number?: "))

# Loops so that until you put 0 it will keep asking for numbers
while True:
    if number >= 1000:
        high()
    elif number <= 999 and number > 0:
        mid_range()
    elif number < 0:
        low()
    # Ends the loop if 0 is input 
    elif number == 0:   
        break
    number = int(input("What is your number?: "))

print("Ended")