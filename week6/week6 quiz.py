#1
def skip_letter(word):
    result = []
    for i in range(0, len(word), 2):  # 0부터 2씩 증가
        result.append(word[i])
    return result



#2
def skip_letter(word):
    result = []
    for i in range(1, len(word), 2):
        result.append(word[i])
    return result



#3
def output_even(smaller_num, larger_num):
    result = []
    for i in range(smaller_num, larger_num+1):
        if i % 2 == 0:
            result.append(i)
    return result
    


#4
def output_odd(smaller_num, larger_num):
    result =[]
    for i in range(smaller_num, larger_num+1):
        if i % 2 == 1:
            result.append(i)
    return result



#5
def hailstone_seq(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result



#6
def find_factors(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result



#7
def ascending_order(num_1, num_2, num_3):
    nums = [num_1, num_2, num_3]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums



#8
def descending_order(num_1, num_2, num_3):
    nums = [num_1, num_2, num_3]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums



#9
def count(cards):
    total = 0
    for card in cards:
        if card in [2, 3, 4, 5, 6]:
            total += 1
        elif card in [7, 8, 9]:
            total += 0
        elif card in [10, 'j', 'q', 'k', 'a']:
            total -= 1
    return total



#10
def war_of_numbers(numbers):
    even_total = 0
    odd_total = 0
    result = ""
    for number in numbers:
        if number % 2 == 0:
            even_total += number
        else:
            odd_total += number

    if even_total > odd_total:
        result += "evens"
    else:
        result += "odds"
    return result



#11
def add_lists(lyst1, lyst2):
    result = []
    for i in range(len(lyst1)):
        sum = lyst1[i] + lyst2[i]
        result.append(sum)
    return result



#12
def largest_even(numbers):
    largest = -1
    for i in numbers:
        if i % 2 == 0:
            if i > largest:
                largest = i
    return largest



#13
def largest_odd(numbers):
    largest = -1
    for i in numbers:
        if i % 2 == 1:
            if i > largest:
                largest = i
    return largest



#14
def progress_days(miles):
    count = 0
    for i in range(1, len(miles)):
        if miles[i-1] < miles[i]:
            count += 1
    return count



#15
def lag_days(miles):
    count = 0
    for i in range(1, len(miles)):
        if miles[i-1] > miles[i]:
            count += 1
    return count



#16
def like_or_dislike(events):
    state = "nothing"
    for event in events:
        if event == state:
            state = "nothing"
        else:
            state = event
    return state



#17
def get_indices(lyst, item):
    result = []
    for i in range(len(lyst)):
        if lyst[i] == item:
            result.append(i)
    return result



#18
def list_of_multiples(num, length):
    result = []
    for i in range(1, length+1):
        result.append(num * i)
    return result



#19
def is_acronym(s, words):
    acronym = ""
    for word in words:
        acronym += word[0]
    if acronym == s:
        return True
    else:
        return False