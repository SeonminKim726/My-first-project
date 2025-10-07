'''
#function1

def pyramid_volume(base, height):
    volume = (base**2 * height) / 3
    return volume

print(f"Theh volume of the pyramid is {pyramid_volume(3,4)}")



#function8

def pool_times(grade, time):
    if grade == "k" or 1 <= int(grade) <= 3:        #아니면 k를 grade = 0으로 간주하고 코딩해도됨
        if time == "Morning":
            pool_time = "9 AM"
        else:
            pool_time = "1 PM"
    elif 4 <= int(grade) <= 8:
        if time == "Morning":
            pool_time = "10 AM"
        else:
            pool_time = "2 PM"
    elif 9 <= int(grade) <= 12:
        if time == "Morning":
            pool_time = "11 AM"
        else:
            pool_time = "3 PM"
    return pool_time

grade = input("Enter your grade: ")
time = input("Enter time: ")

print(f"Pool Time is: {pool_times("k", "Morning")}")



#function11

def convert_knuts(knuts):
    #1. For the number of knuts, how many galleons can I buy?
    
    galleons = knuts // (29*17)
    remaining_knuts = knuts - (galleons * 29 * 17)

    #2. Remaining knuts, how many sickles can I buy?

    sickles = remaining_knuts // 29


    #3. How many reamining knuts after buying sickles?

    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ""

    if galleons > 0:
        output += f"Galleons: {galleons} "
    if sickles > 0:
        output += f"Sickles: {sickles} "
    if knuts > 0:
        output += f"Knuts: {remaining_knuts} "

    return output

print(convert_knuts(544))               #print는 무조건 def 코드 바깥에 있을 것 !!



#function14

from random import randint

def guess_num(user_guess):
    output = ""
    value = randint(0,9)
    if user_guess == "even":
        if value % 2 == 0:
            output = "Correct"
        else:
            output = "Incorrect"
    elif user_guess == "odd":
        if value % 2 != 0:
            output = "Correct"
        else:
            output = "Incorrect"

    return output


user_input = input("Guess the random number (odd or even): ")
print(f"The guess is: {guess_num(user_input)}")

'''

#string1 (Takes in temerature and checks if it is fever)

def is_fever(temperature):

    # How can we extract the F and C ? Hint: word[-1]
    unit = temperature[-1]

    # If it is F -> 98.6 is a fever
    if unit == "F":
        if temperature[:-1] > 98.6:
            return True
        else:
            return False
        
    # If it is C -> 37 is a fever
    elif unit == "C":
        if temperature[:-1] > 37:
            return True
        else:
            return False
        
# Input and print should be outside of the function
user_input = input("Enter a temperature in F or C")
print(f"Is fever ? {is_fever(user_input)}")