#9/21/2025 functions


'''
#1

def pyramid_volume(x, y):
    return x**2 * y / 3

b = float(input())
h = float(input())
print(f"{pyramid_volume(b, h):.2f}")



#2

import math

def cone_volume(x, y):
    return math.pi * x**2 * h / 3

r = float(input())
h = float(input())
print(f"{cone_volume(r, h):.2f}")



#3

def total_score(x, y):
    return 2 * x + 3 * y

num_2 = int(input())
num_3 = int(input())
print(f"{total_score(num_2, num_3)}")



#4

def total_score(x, y):
    return 2 * x + 1 * y

aces = int(input())
winning_shots = int(input())
print(f"{total_score(aces, winning_shots)}")



#5

def leg_counter(x, y, z):
    return 2 * x + 4 * y + 4 * z

chickens = int(input())
cows = int(input())
pigs = int(input())
print(f"{leg_counter(chickens, cows, pigs)}")



#6

def battery_counter(x, y, z):
    return 2 * x + 4 * y + 6 * z

e_dolls = int(input())
rc_cars = int(input())
robo_dogs = int(input())

print(f"{battery_counter(e_dolls, rc_cars, robo_dogs)}")



#7

def resting_rate(age, athl_goal):
    if 20 <= age <= 39:
        if athl_goal == "Above Average":
            return "47-72"
        elif athl_goal == "Below Average":
            return "73-93"
    elif 40 <= age <= 59:
        if athl_goal == "Above Average":
            return "46-71"
        elif athl_goal == "Below Average":
            return "72-94"
    elif 60 <= age <= 79:
        if athl_goal == "Above Average":
            return "45-70"
        elif athl_goal == "Below Average":
            return "71-97"
        
user_age = int(input())
user_athl_goal = input("Enter the athletic goal (Above Average or Below Averge): ")

print(f"{resting_rate(user_age, user_athl_goal)}")

'''

#8

def pool_time(grade, time):
    if grade == k or 1 <= int(grade) <= 3:
        if time == "Morning":
            print("9 AM")
        elif time == "Afternoon":
            print("1 PM")
    elif 4 <= int(grade) <= 8:
        if time == "Morning":
            print("10 AM")
        elif time == "Afternoon":
            print("2 PM")
    elif 9 <= int(grade) <= 12:
        if time == "Morning":
            print("11 AM")
        elif time == "Afternoon":
            print("3 PM")

user_grade = input()
user_time = input("Enter the time (Morning or Afternoon): ")

print(f"{pool_time(user_grade, user_time)}")



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


#20

#21

#22

#23

#24

#25

#26

#27

#28

#29

#30

#31

#32

#33

#34
