# Write a program that takes integers from the user and adds them together until they type done. return the sum.
'''
total = 0
user_input = input("Enter a number of type done: ")
    
while user_input != "done":
    user_number = float(user_input)
    total += user_number
    user_input = input("Enter a number of type done: ")

print(f"total = {total}")
'''

from random import randint
#var_name = open('whatever your file name is . ext', 'w')

# if filename does not exist at that path:
    # my_file = open('numbers.txt', 'w')
# if filename does exist at that path:
    # pop up box that says are you sure

my_file = open('numbers.txt', 'w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(f'{number}\n')      # 이것도 똑같음 my_file.write(str(number) + '\n')

my_file.close()
