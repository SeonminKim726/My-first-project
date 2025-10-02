# functions

#1

def pyramid_volume(b, h):
    return b**2 * h / 3



#2

import math

def cone_volume(r, h):
    return math.pi * r**2 * h / 3



#3

def total_score(num2, num3):
    return 2 * num2 + 3 * num3



#4

def total_score(aces, winning_shots):
    return 2 * aces + 1 * winning_shots



#5

def leg_counter(chickens, cows, pigs):
    return 2 * chickens + 4 * cows + 4 * pigs



#6

def battery_counter(e_dolls, rc_cars, robo_dogs):
    return 2 * e_dolls + 4 rc_cars + 6 * robo_dogs



#7

def resting_rate(age, athl_goal):
    if 20 <= age <= 39:
        if athl_goal == "Above Average":
            return "47-72"
        elif athl_goal == "Below Average":
            return "73-93"
    elif 40 <= age <= 59:
        if athl_goal == "Above Average":
            return "46-71"
        elif athl_goal == "Below Average":
            return "72-94"
    elif 60 <= age <= 79:
        if athl_goal == "Above Average":
            return "45-70"
        elif athl_goal == "Below Average":
            return "71-97"


            
#8

def pool_time(grade, time):
    if grade == "k" or 1 <= int(grade) <= 3:        #아니면 k를 grade = 0으로 간주하고 코딩해도 됨
        if time == "Morning":
            return "9 AM"
        elif time == "Afternoon":
            return "1 PM"
    elif 4 <= int(grade) <= 8:
        if time == "Morning":
            return "10 AM"
        elif time == "Afternoon":
            return "2 PM"
    elif 9 <= int(grade) <= 12:
        if time == "Morning":
            return "11 AM"
        elif time == "Afternoon":
            return "3 PM"



#9

def traffic_light(color):
    if color == "red":
        return "Stop"
    elif color == "green":
        return "Go"
    elif color == "yellow":
        return "Yield"



#10

def access_rights(user_role):
    if user_role == "user":
        return "limited"
    elif user_role == "guest":
        return "view"
    elif user_role == "admin":
        return "full"



#11

def convert_knuts(knuts):
    galleons = knuts // (29*17)
    remaining_knuts = knuts - (galleons * 29 * 17)

    sickles = remaining_knuts // 29

    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ""

    if galleons > 0:
        if galleons > 1:
            output += f"{galleons} galleons "
        else:
            output += f"{galleons} galleon "
    if sickles > 0:
        if sickles > 1:
            output += f"{sickles} sickles "
        else:
            output += f"{sickles} sickle "
    if remaining_knuts > 0:
        if remaining_knuts > 1:
            output += f"{remaining_knuts} knuts"
        else:
            output += f"{remaining_knuts} knut"
    
    return output


    
#12

def convert_bronze(bronze_coins):
    gold_coins = bronze_coins // (15 * 20)
    remaining_bronze = bronze_coins - (gold_coins * 15 * 20)

    silver_coins = remaining_bronze // 20
    remaining_bronze = remaining_bronze - (silver_coins * 20)

    output = ""
    if gold_coins > 0:
        output += f"{gold_coins} gold "
    if silver_coins > 0:
        output += f"{silver_coins} silver "
    if remaining_bronze > 0:
        output += f"{remaining_bronze} bronze"

    return output



#13

from random import randint

def toss_coin(guess):
    output = ""
    value = randint(0,1)
    if guess == value:
        output = "Correct"
    else:
        output = "Incorrect"

    return output



#14

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



#15

def count_duplicates(num_1, num_2, num_3):
    if num_1 == num_2 == num_3:
        return "You entered the same number 3 times"
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        return "You entered the same number 2 times"
    else:
        return "Each number is unique"
    


#16

def highway_directions(highway_num):
    if 1 <= highway_num <= 99:  # primary
        if highway_num % 2 == 0:
            return f"I-{highway_num} runs east/west"
        else:
            return f"I-{highway_num} runs north/south"
    elif 100 <= highway_num <= 999:  # auxiliary
        primary = highway_num % 100
        if primary == 0 or primary > 99:
            return f"I-{highway_num} is an invalid highway number"
        else:
            if primary % 2 == 0:
                return f"I-{highway_num} runs east/west"
            else:
                return f"I-{highway_num} runs north/south"
    else:  # 0 이하 또는 1000 이상
        return f"I-{highway_num} is an invalid highway number"



#17

def check_letter(letter):
    vowels = "aeiou"
    if letter in vowels:
        return "Vowel"
    else:
        return "Consonant"
    


#18

def serve_icecream(selected_flavor):
    available = ["Vanilla", "Chocolate", "Strawberry"]
    
    if selected_flavor in available:
        return f"Here is your {selected_flavor} ice cream!"
    else:
        return f"Sorry, we don't have {selected_flavor} ice cream."
    


#19

def serve_coffee(selected_coffee):
    available = ["Espresso", "Latte", "Cappuccino"]

    if selected_coffee in available:
        return f"Here is your {selected_coffee}!"
    else:
        return f"Sorry, we don't have {selected_coffee}"



#20

def find_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif player1 == "Rock" and player2 == "Scissors" or player1 == "Scissors" and player2 == "Paper" or player1 == "Paper" and player2 == "Rock":
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"



#21

def triangle_type(side_1, side_2, side_3):
    if side_1 == side_2 == side_3:
        return "equilateral"
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        return "isosceles"
    else:
        return "scalene"
    


#22

def find_relation(name):
    if name == "Darth Vader":
        return "Father"
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother in law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "Unknown"
    


#23

def find_relation(name):
    if name == "Moriarty":
        return "Archenemy"
    elif name == "Watson":
        return "Best Friend"
    elif name == "Mrs. Hudson":
        return "Landlady"
    elif name == "Inspector Lestrade":
        return "Detective"
    else:
        return "Unknown"



#24

def skip_letter(word):
    result = ""

    for i in range(1, len(word), 2):
        result += word[i]
    return result



#25

def skip_letter(word):
    result = ""
    
    for i in range(0, len(word), 2):
        result += word[i]
    return result



#26

def output_even(smaller_num, larger_num):
    for num in range(smaller_num, larger_num + 1):
        if num % 2 == 0:
            print(num, end=", ")



#27

def odd_sum(smaller_num, larger_num):
    result = 0

    for num in range(smaller_num, larger_num + 1):
        if num % 2 == 1:
            result += num
    return result



#28

def create_word():
    word = ""

    while True:
        letter = input("Enter a letter (type 'done' to finish): ")
        if letter == "done":
            break
        word += letter  # 입력받은 글자를 단어에 추가
    return word

#result = create_word()
#print(result)



#29

def sum_loop():
    sum = 0

    while True:
        num = int(input("Enter an integer: "))

        if num < 0:
            break
        sum += num
    return sum

#result = sum_loop()
#print(result)



#30

def hailstone_seq(n):
    result = ""

    while n != 1:
        result += str(n) + " "
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    result += "1"
    return result


    
#31

def find_factors(num):
    factors = ""
    for i in range(1, num + 1):
        if num % i == 0:
            factors += str(i) + " "
    return factors



#32

def design_rug(width, length, pattern):
    rug = ""
    for line_num in range(length):
        rug += pattern * width + "\n"
    return rug



#33

def square_sum(num):
    if num < 1:
        return "unknown"
    total = 0
    for i in range(1, num + 1):
        total += i ** 2
    return total



#34

def cube_sum(num):
    if num < 1:
        return "unknown"
    total = 0
    for i in range(1, num + 1):
        total += i ** 3
    return total