# strings

#1

def is_fever(temp):
    unit = temp[-1]
    value = float(temp[:-1])
    
    if unit == "F":
        if value > 98.6:
            return True
        else:
            return False
    elif unit == "C":
        if value > 37:
            return True
        else:
            return False
    


#2

def is_boiling(temp):
    unit = temp[-1]
    value = float(temp[:-1])

    if unit == "F":
        if value >= 212:
            return True
        else:
            return False
    elif unit == "C":
        if value >= 100:
            return True
        else:
            return False
        


#3

def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance



#4

def is_isogram(word):
    i = 0
    while i < len(word):
        j = i + 1
        while j < len(word):
            if word[i] == word[j]:
                return False
            j += 1
        i += 1
    return True



#5

def get_drink_ID(flavor, capacity):
    return flavor[:3] + str(capacity)



#6

def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_sentence = ""

    i = len(words) - 1
    while i >= 0:
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += " "
        i -= 1
    
    return reversed_sentence



#7

def reverse_string(word):
    reversed_word = ""
    i = len(word) - 1

    while i >= 0:
        reversed_word += word[i]
        i -= 1
    return reversed_word



#8

def first_letters(sentence):
    words = sentence.split(" ")
    result = ""

    i = 0
    while i < len(words):
        result += words[i][0]
        i += 1

    return result



#9

def last_letters(sentence):
    words = sentence.split(" ")
    result = ""

    i = 0
    while i < len(words):
        result += words[i][-1]
        i += 1

    return result  



#10

def flip_flop(word):
    length = len(word)
    half = length // 2

    if length % 2 == 0:
        first_half = word[:half]
        second_half = word[half:]
        return second_half + first_half
    else:
        first_half = word[:half]
        middle = word[half]
        second_half = word[half+1:]
        return second_half + middle + first_half