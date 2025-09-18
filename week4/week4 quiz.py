#09/18/2025 lab시간에 다같이 풂
'''
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

for i in range(1 , len(word) - 1, 2):
    print(word[i])
    result += word




#3

for i in range(38, 1051, 2):
    print(i)



#4

while True:
    user_in = input("Enter a letter: ")
    if user_in == "done":
        break
    else:
        word += user_in
print(word)
'''


#5

total = 0

for num in range(51, 518, 2):
    total += num

print(f"The sum of all odd numbers between 50 and 517 is {total}")