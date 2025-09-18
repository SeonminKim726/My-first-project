#09/18/2025

#1

larger_num = int(input("Enter the larger Number: "))
smaller_num = int(input("Enter the smaller Number: "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halves: {num}")

