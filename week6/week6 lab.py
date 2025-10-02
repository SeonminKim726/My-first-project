# 5

def hailstone_seq(n):
    output_list = [n]
    while n != 1:
        #while loop till 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        output_list.append(int(n))

    return output_list

#print(hailstone_seq(25))



# 9

def count(cards):
    sum = 0
    
    for card in cards:
        temp_card = str(card)
        if temp_card in ["2", "3", "4", "5", "6"]:
            sum += 1
        elif temp_card in ["10", "j", "q", "k", "a"]:
            sum -= 1
    
    return sum
print(count(["a", "a", "k", "q", "q", "j"]))


