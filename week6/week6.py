#Write a function that takes an int adds two, multiples by 4, prints the result
'''
def my_fctn(number):
    number += 2
    number *= 4
    print(number)

#ex
my_fctn(10)
my_fctn(3)



#Starting with the value 10, add 2, then multiple it by 4. Take the result and add 2 to it, then multiple by 4 again.

def my_fctn(number):
    number += 2
    number *= 4
    return number

result1 = my_fctn(10)
result2 = my_fctn(result1)
print(result2)







def my_fctn(number):
    number += 2
    number *= 4
    return number

def add_ten(number):
    number += 10
    return result




#Call the function my_fctn 10 times.
def my_fctn(number):
    number += 2
    number *= 4
    return number

result = 10
for number in range(0,10):
    result = my_fctn(result)
print(result)

'''



'''

#Call the function my_fctn 100 times.
def my_fctn(number):
    number += 2
    number *= 4
    return number



#Write a funtion that return the product of two arguments.
def product(num1, num2):
    product = num1 * num2
    return product

print(product(4,3))




#2 arguments function으로 3 arguments 계산하기 (4, 3, 10)
def product(num1, num2):
    product = num1 * num2
    return product

x = product(4,3)

print(product(x,10))





#In python, a list starts with [ and end with ]

x = []  #this is a list with nothing in it.

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

#print the element of the lyst in position 1.
#print(lyst[1])

#print everything in the lyst.
#print(lyst)


#print the portioin of the list that is 3, False, 4.5
#print(lyst[2:5])


x = 'appl'
print(x)
#e가 필요하지

x += 'e'
print(x)
#수정 완료 !


'''


#lyst.append( element ) will add the element to the end of the lyst.

x = []  #this is a list with nothing in it.

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

print(lyst)

lyst += [12]
print(lyst)
