#2025/10/16

#4
def find_winner(player1 = "Rock", player2 = "Rock"):
    if player1 == player2:
        return "It's a tie!"
    
    if (player1 == "Rock" and player2 == "Scissors") or (player1 == "Scissors" and player2 == "Paper") or (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
    


#8
def descending_order(num_1, num_2 = 15, num_3 = 5):

    a, b, c = num_1, num_2, num_3        #a = num_1 이런식으로 각각 따로 써도 됨

    if a < b:
        a, b = b, a

    if a < c:
        a, c = c, a

    if b < c:
        b, c = c, b
    
    return [a, b, c]




#15
def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    
# shorter way
# def is_negative(num):
    # return num < 0
    

def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

# shorter way
# def is_odd(num):
    # return num % 2 == 1


def report_negative_odds(lyst):
    output = []

    for num in lyst:
        if is_negative(num) and is_odd(num):
            output.append(num)

    return output
