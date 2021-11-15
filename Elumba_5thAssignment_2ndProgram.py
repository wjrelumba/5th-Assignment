# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

def userInputs():
    numberOne = float(input("Enter first number: "))
    numberTwo = float(input("Enter second number: "))
    numberThree = float(input("Enter third number: "))
    return numberOne, numberTwo, numberThree

One, Two, Three = userInputs()

if One < Two and One < Three:
    small = One
else:
    if Two < One and Two < Three:
        small = Two
    else:
        if Three < One and Three < Two:
            small = Three
        else:
            pass

print(f"The lowest number is: {small:.2f}")    