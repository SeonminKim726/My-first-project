'''
age = int(input('What is your age?: '))

print "hello world"

print(f'Your age is {age}.')
print(f'Next year your age will be {age + 1}')
'''


'''
print('Starting program')


try:
    age = int(input('What is your age?: '))
    print(f'Your age is {age}.')
    print(f'Next year your age will be {age + 1}.')
except ValueError:
    print('You must pick an integer age.')


print('Your program ended normally')
'''

'''
print("Enter a number. I will divide 10 by that number, and output the result")
user_input = input("Pick a number: ")

done = False

while not done:
    try:
        user_number = int(user_input)                                           # try 있어도 되고 없어도 되고.
        result = 10 / user_number
        print(f'The result is {result}')
        done = True
    except ValueError:
        print("Please pick an integer.")
        user_input = input("Pick a number: ")
    except ZeroDivisionError:
        print("Don't pick 0")
        ukser_input = input("Pick a number: ")
    
print("The end")
'''
    
          
'''
try:
    block of code
    ...
    ...
    # if something "goes wrong" in here, and error will be raised and sent to the except statement.
except (code simiilar to an if statement):
    block of code
    ...
    ...

except NameError:
    # handle this type of error.
    print('This is a name error')
except ValueError:
    print('value error')
except TypeError:
    print('type error')
'''


'''
class Playlist:
    def __init__(self, name = "NEw Playlist", songs = []):
        self.name = name
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)
    
    def __add__(self, other):
        combined_name = self.name + "+" + other.name
        combined_song = self.songs + other.songs
        return Playlist(combined_name, combined_song)
    
    def __str__(self):
        return f"{self.name} {self.songs}"


p1 = Playlist("X", ["Song A", "Song B"])
p1.add_song("Song D")

p2 = Playlist("Y", ["Song C"])
print(p2)

combined = p1 + p2
print(combined)

'''



class ShoppingCart:
    def __init__(self, items = {}):
        self.items = items

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def __add__(self, other):
        combined = ShoppingCart()
        for item, qty in self.items.items():
            combined_items[item] += qty

        for item,qty in other.items.items():
            if item in combined.items:
                combined.items[item] += qty
            else:
                combined.items[item] = qty

    def __str__(self):
        return f"{self.items}"


c1 = ShoppingCart({"tea": 1, "energy drink": 2})
c1.add_item("clock")
print(c1)
c2= ShoppingCart({"energy drink": 3, "hat": 1})

combined = c1 + c2
print(combined)