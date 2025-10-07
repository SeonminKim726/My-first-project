#09/18/2025 lab시간에 다같이 풂

#1

larger_num = int(input("Enter the larger Number: "))
smaller_num = int(input("Enter the smaller Number: "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halves: {num}")


#2

word = input("Enter a word: ")
result = ""

for i in range(1 , len(word), 2):
    result += word[i]
print(result)



#3

for i in range(38, 1051, 2):
    print(i)




#4
word = ""
while True:
    user_in = input("Enter a letter: ")
    if user_in == "done":
        break
    else:
        word += user_in
print(word)



#5

total = 0

for num in range(51, 518, 2):
    total += num

print(f"The sum of all odd numbers between 50 and 517 is {total}")



#6

total = 0

while True:
    user_in = int(input("Enter an integer: "))
    if user_in >= 0:
        total += user_in
    else:
        break
print(total)



#7

n = 25

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    elif n % 2 == 1:
        n = 3 * n + 1

print(n)


#8

user_in = int(input("Enter a number: "))

for n in range (1, user_in + 1):
    if user_in % n == 0:
        print(n, end=" ")




#9

width = int(input("Enter a width: "))
length = int(input("Enter a length: "))
pattern = input("Enter a pattern: ")

for _ in range(length):
    for _ in range(width):
        print(pattern, end="")
    print()



#10
max_even = -1  # 짝수가 하나도 없으면 -1

while True:
    n = int(input("Enter a number: "))
    
    if n < 0:
        break  # 음수 입력 시 종료

    if n % 2 == 0:  # 짝수일 때
        if n > max_even:
            max_even = n

print(f"largest = {max_even}")



#11
user_number = int(input("Enter a number: "))
total = 0

for i in range(1, user_number + 1):
    total += i ** 2

print(total)