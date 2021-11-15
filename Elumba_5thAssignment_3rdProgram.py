# Program 3: Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person.
# Rules:
# 0 - 12 : Kid
# 13 - 17 : Teen
# 18 : Debut
# 19 above : Adult

def userInput():
    ageF = int(input("Enter your age: "))
    return ageF

age = userInput()

if age >= 0 and age < 13:
    print("Kid")
else:
    if age > 12 and age < 18:
        print("Teen")
    else:
        if age == 18:
            print("Debut")
        else:
            if age >= 19:
                print("Adult")
            else:
                pass