# 7. Dictionaries

#1
def is_isogram(word):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True



#2
def find_unique(numbers):
    counts = {}

    for n in numbers:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    for key in counts:
        if counts[key] == 1:
            return key
        


#3
def return_unique(numbers):
    counts = {}

    for n in numbers:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    uniques = []

    for key in counts:
        if counts[key] == 1:
            uniques.append(key)

    return uniques



#4
def get_name(names):
    name_list = []
    for key in names:
        name = names[key]
        name_list.append(name)
    return name_list



#5
def find_oldest(people):
    oldest_person = ""
    max_age = -1
    
    for key in people:
        age = people[key]

        if age > max_age:
            max_age = age
            oldest_person = key

    return oldest_person



#6
def letter_count(word):
    counts = {}
    for letter in word:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1        

    return counts



#7
def min_grade(exams):
    minimal_course = ""
    min_grade = 1000
    
    for key in exams:
        grade = exams[key]

        if grade < min_grade:
            min_grade = grade
            minimal_course = key

    return minimal_course



#8
def find_youngest(people):
    youngest_person = ""
    min_age = 100
    
    for key in people:
        age = people[key]

        if age < min_age:
            min_age = age
            youngest_person = key

    return youngest_person



#9
receipt = {}

receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3

print(receipt)

total = 0
for price in receipt.values():
    total += price


print("Total cost: $", total)



#10
menu = {}

menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3

for item, price in menu.items():
    print(item, price)



#11
def count_repetitions(elements):
    counts = {}
    
    for e in elements:
        if e not in counts:
            counts[e] = 1
        else:
            counts[e] += 1
            
    return counts



#12
def items_purchase(store, wallet):
    affordable_items = []
    
    for key in store:
        price = store[key]
        if price <= wallet:
            affordable_items.append(key)
    
    return affordable_items



#13
def total_sales(sales):
    sum = 0
    for key in sales:
        sold_units = sales[key]
        sum += sold_units

    return sum



#14
def high_earners(employee_salaries, given_salaries):
    above_salaries = []
    for key in employee_salaries:
        salaries = employee_salaries[key]
        if salaries > given_salaries:
            above_salaries.append(key)

    return above_salaries



#15
def total_donations(donations):
    total = 0
    for key in donations:
        donated_amount = donations[key]
        total += donated_amount

    return total



#16
calories = {
    "apple" : 95,
    "banana" : 105,
    "orange" : 62,
    "grape" : 3,
    "pear" : 102
}

def total_calories(fruits):
    total = 0
    for key in fruits:
        if key in calories:
            total += calories[key]
    return total



#17
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



#18
def majority_element(nums):
    counts = {}

    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    majority = None
    max_count = 0

    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]
            majority = key

    return majority