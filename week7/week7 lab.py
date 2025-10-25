#10/9/2025
'''
#4
def get_name(my_dict):
    #0. Empty List to storage names
    names = []
    #1. How to iterate through the dictionary
    for key in my_dict:
        #2. How do we access the value with the key ?
        name = my_dict[key]
        #3. How do you put the names in a list ?
        names.append(name)
    return names

names_dict = {"123": "Matt Priem", "456": "Even Linder", "789": "Jacob"}
#print(get_name(names_dict))

#5
def find_oldest(people):
    oldest_person = ""
    max_age = -1
    
    # How do we iterate throught the dict ?
    for name in people:
        age = people[name]

        # How do you find the oldest age ?
        if age > max_age:
            max_age = age
            # How do you get the name ?
            oldest_person = name

    return oldest_person
#print(find_oldest({ "Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))



#6
def letter_count(word):
    count_dict = {}
    for letter in word:
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] += 1        

    return count_dict

print(letter_count("mississippi"))

#9
'''


prices = {
    "flour" : 2.50,
    "sugar" : 1.80,
    "eggs" : 3.00,
    "milk" : 2.00,
    "butter" : 2.75,
    "vanilla" : 4.50,
    "chocolate" : 5.00
}

def total_cost(ingredients):
    total = 0
    for key in ingredients:
        if key in prices:
            total += prices[key]
    return total

print(total_cost(["eggs","orange"]))
