#x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(x[2])

#print(x[1:4])


#lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#for element in lyst:
#    print(element)

#print(lyst)
#lyst.append('Saturday')
#lyst.append('Sunday')
#print(lyst)

#word = 'appl'
#print(word)
#word += 'e'
#print(word)

##Wednesday의 nes만 print
#x = lyst[2]
#print(x[3:6])



# Friday를 Funday로 바꾸기

#lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(lyst)

#lyst[4] = 'Funday'

#print(lyst)



# 이렇게는 안됨

#word = 'apfel'
#print(word)

#word[2] = 'p'
#print(word)




#x = 'apple'
#y = x
#print(x)
#print(y)

#x += 's'
#print(x)
#print(y)




# immutable object



# mutable object (Friday를 Funday로 바꿈)

#x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#y = x

#print(X)
#print(y)

#x[4] = 'Funday'

#print(x)
#print(y)



#workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(workdays)
#workdays[4] = 'Funday'
#print(workdays)




#workdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

#print(workdays)
#workdays[4] = 'Funday'
#print(workdays)



# Write a function that takes a string as an arguement, and returns a list containing all of the words in that string.

# = 'Peter Piper picked a peck of pickled peppers.'
#result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']

#def string_to_list(word):
    #words = []
    # collect a word
    #built_word = ''
    #for letter in word:
        #if letter == ' ':
            # add built_word into the list
            #words.append(built_word)
            #built_word = ''
        # once we have a full word, let's add it to the list of words.
        #else:
            #built_word += letter
    #words.append(built_word)
    #return words



#def string_to_list_alt(word):
    #words = []
    #built_word = ''
    #for index in range(len(word)):
        #if word[index[ == ' ' or index == len(word)-1:
            #words.append(built_word)
            #built_word = ''
        #else:
            #built_word += word[index]

    #return words
        


    # once we have a full word, let's add it to the list of words.


#print(string_to_list(my_word))




def string_to_list_with_vowels(word):
    words = []
    # collect a word
    built_word = ''
    vowel_count = 0
    for letter in word:
        print(letter, vowel_count, built_word)
        if letter == ' ':
            # add built_word into the list if amount of vowels >= 2.
            if vowel_count >= 2:
                words.append(built_word)
            built_word = ''
            vowel_count = 0
        # once we have a full word, let's add it to the list of the words.
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count += 1
    if vowel_count >=2:
        words.append(built_word)
    return words

my_word = 'Peter Piper picked a peck of pickled peppers'
result = ['Peter', 'Piper', 'picked', 'a', 'pickled', 'peppers']

print(string_to_list_with_vowels(my_word))






# Write a function that takes a string as an arguement, and returns a dictionary containing all of the unique words in that string.

phonebook = {'matt':5073891438, 'ashley':12345}
print(phonebook)

# To add to a dictionary, we use name_of_dict[key] = value
phonebook['waters'] = 789
print(phonebook)


# To look up a value in a dictionary, use use name_of_dict[key]
print(phonebook['matt'])

for person in phonebook:
    print(person, phonebook[person])





# Write a function that takes a string as an arguement, and returns a list containing all of the unique words in that string.

my_words = 뭐지 여기 모르겠음
def string_to_dictionary(word):
    string_as_list = word.split()
    word_dictionary = []
    for word in string_as_list:
        if word in word_dictionary:
            pass
        else:
            pass
        word_dictionary[word] = 'in word'
    return word_dictionary

print(string_to_dictionary(my_words))
