#write a function that returns a dictionary containing how many times each letter appears.

def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            #add in key value pair. What are key and value?
            letter_dictionary[letter] += 1
        else: #key is NOT in dictionary
            #add in key value pair. What are key and value?
            letter_dictionary[letter] = 1

    return letter_dictionary

my_word = 'peter piper picked a peck of pickled peppers'

#output 방식 1 (result = p 9 \ e ? \ ...)
letter_dict = letter_counter(my_word)

for letter in letter_dict:
    print(letter, letter_dict[letter])

#output 방식 2 (result = {'p':9, 'e':? ...})
print(letter_counter(my_word))




#
def add_three(x):
    y = x + 3
    return y

var0 = 7
var1 = add_three(var0)



#
import math
x = math.sqrt(16)
print(x)




#mY_fctns1

#my_fctns2
def print_a_list(lyst):
    for element in lyst[::]:
        print(element)


import math
import my_fctns1
import my_fctns2

x = [1,2,3,4,5]

print








#
import my_fctns1_for_cis121_f25_section1_at_9am as my_stuff

x = my_stuff.add_three(7)


def abc():
    return my_stuff.add_three(5)

print(abc())