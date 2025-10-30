#1
def skip_letter(word):
    output = []
    for i in range(0, len(word), 2):
        output.append(word[i])

    return output

#2
def skip_letter(word):
    output = []
    for i in range(1, len(word), 2):
        output.append(word[i])
    
    return output

#3
def output_even(smaller_num, larger_num):
    output = []
    for i in range(smaller_num, larger_num + 1):
        if i % 2 == 0:
            output.append(i)

    return output

#4
def output_odd(samller_num, larger_num):
    output = []
    for i in range(samller_num, larger_num + 1):
        if i % 2 == 1:
            output.append(i)

    return output     

#5
def hailestone_seq(n):
    output = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            output.append(n)
        elif n % 2 == 1:
            n = 3 * n + 1
            output.append(n)
                          
    return output

#6
def find_factors(num):
    output = []
    for i in range(1, num + 1):
        if num % i == 0:
            output.append(i)
    
    return output

#7
def ascending_order(num_1, num_2, num_3):
    nums = [num_1, num_2, num_3]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

#8
def descending_order(num_1, num_2, num_3):
    nums = [num_1, num_2, num_3]
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            
    return nums

#9
def count(cards):
    total = 0
    for card in cards:
        if card  in [2, 3, 4, 5, 6]:
            total += 1
        elif card in [7, 8, 9]:
            total += 0
        elif card in [10, "j", "q", "k"]:
            total -= 1
    
    return total

#10
def war_of_numbers(numbers):
    even_total = 0
    odd_total = 0

    for i in numbers:
        if i % 2 == 0:
            even_total += i
        else:
            odd_total += i

    if even_total > odd_total:
        return "evens"
    elif odd_total > even_total:
        return "odds"
    
#11
def add_lists(lyst1, lyst2):
    output = []
    for i in range(len(lyst1)):
        output.append(lyst1[i] + lyst2[i])

    return output

#12
def largest_even(numbers):
    largest_even = -1
    for number in numbers:
        if number % 2 == 0:
            if number > largest_even:
                largest_even = number
    
    return largest_even


#13
def largest_odd(numbers):
    largest_odd = -1
    for number in numbers:
        if number % 2 == 1:
            if number > largest_odd:
                largest_odd = number
    
    return largest_odd

#14
def progress_days(lyst):
    for i in range(len(lyst)):
        for j in range(i+1, len(lyst)):
            if lyst[i] 


#15


#16


#17


#18


#19