def return_unique(numbers):

	number_dicitonary = {}
	#load dictionary
	for number in numbers:
		if number not in number_dicitonary:
			number_dicitonary[number] = 1			
		else:
			number_dicitonary[number] += 1

	unique_numbers = []
	#find unique numbers in dictionary
	for number in number_dicitonary:
		if number_dicitonary[number] == 1:
			unique_numbers.append(number)

	return unique_numbers


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
