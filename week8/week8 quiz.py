# 1
from random import randint

def toss_coin(guess = 0):
    value = randint(0,1)
    if guess == value:
        return "Correct!"
    else:
        return "Incorrect!"



# 2
from random import randint

def guess(guess = "even"):
    value = randint(0,9)
    if value % 2 == 0:
        if guess == "even":
            return "Correct!"
        else:
            return "Incorrect!"
    else:
        if guess == "even":
            return "Incorrect!"
        else:
            return "Correct!"



# 3
def count_duplicates(num_1 = 0, num_2 = 0, num_3 = 0):
    a, b, c = num_1, num_2, num_3
    if a == b and b == c:
        return "There are 3 of the same number"
    elif a == b or a == c or b == c:
        return "There are 2 of the same number"
    else:
        return "Each number is unique"



# 4
def find_winner(player1 = "Rock", player2 = "Rock"):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "Rock" and player2 =="Scissors") or (player1 == "Scissors" and player2 == "Paper") or (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


#5
def find_relations(name = ""):
    relations = {
        "Darth Vader" : "Father",
        "Leia" : "Sister",
        "Han" : "Brother in law",
        "R2D2" : "Droid"
    }
    if name in relations:
        return relations[name]
    #아니면 이렇게 해도 됨
    return relations.get(name.lower(), "Unknown")



# 6
def hailstone_seq(n = 40):
    output = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            output.append(n)
        else:
            n = 3 * n + 1
            output.append(n)

    return output
        


# 7
def ascending_order(num_1, num_2 = 5, num_3 = 25):
    a = num_1
    b = num_2
    c = num_3

    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    return [a, b, c]



# 8
def descendng_order(num_1, num_2 = 15, num_3 = 5):
    a = num_1
    b = num_2
    c = num_3

    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b

    return [a, b, c]



# 9
def get_indices(lyst, value = 0):
    indices = []
    for i in range(len(lyst)):
        if lyst[i] == value:
            indices.append(i)
    return indices



# 10
def find_factors(num = 36):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    
    return factors
            
    
    
# 11
def list_of_multiples(num, length = 5):
    multiples = []
    for i in range(1, length + 1):
        multiples.append(num * i)

    return multiples



# 12
def is_even(num):
    return num % 2 == 0
        
def report_evens(lyst):
    even_lyst = []
    for n in lyst:
        if is_even(n):
            even_lyst.append(n)

    return even_lyst



# 13
def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u"]

def report_vowels(word):
    vowel_lyst = []
    for n in word:
        if is_vowel(n):
            vowel_lyst.append(n)

    return vowel_lyst



# 14
def is_two_digit_number(num):
    return (num in range(-99, -9)) or (num in range(10, 100))
        
def report_two_digit_numbers(lyst):
    new_lyst = []
    for n in lyst:
        if is_two_digit_number(n):
            new_lyst.append(n)

    return new_lyst



# 15
def is_negative(num):
    return num < 0

def is_odd(num):
    return num % 2 == 1
    
def report_negative_odds(lyst):
    negative_lyst = []
    for n in lyst:
        if is_negative(n) and is_odd(n):
            negative_lyst.append(n)
    
    return negative_lyst