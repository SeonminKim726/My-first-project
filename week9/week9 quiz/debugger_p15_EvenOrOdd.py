from random import randint

def guess(guess="even"):
	value = randint(0, 9)
	
	if value // 2 == 0:
		actual = "even"
	else:
		actual = "odd"
	
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"
	
print("\nFinal result: " + guess())