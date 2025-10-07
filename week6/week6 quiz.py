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
    n = 0
    while num % n == 0:
        result.append(n)
        n += 1
    return result

print(find_factors(12))


#7
#8
#9
#10
#11
#12
#13
#14
#15
#16
#17
#18
#19
