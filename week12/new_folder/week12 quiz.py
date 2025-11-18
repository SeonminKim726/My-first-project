#1
class Vector:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        return f"Vector: ({self.a}, {self.b})"

vector1 = Vector(3, 4)
vector2 = Vector(2, 4)

print("Is vector 1 and 2 same ?")
print(vector1 == vector2)



#2
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __str__(self):
        return f"Point: ({self.x}, {self.y})"
    
point1 = Point(3, 4)
point2 = Point(0, 0)

print("Is point 1 and 2 same ?")
print(point1 == point2)
print(point1.distance(point2))



#3
class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def __add__(self, other):
        return LinearEquation(self.m + other.m, self.b + other.b)
    
    def __str__(self):
        if self.m == 1:
            m_part = "x"
        elif self.m == -1:
            m_part = "-x"
        else:
            m_part = f"{self.m}x"
        
        if self.b > 0:
            b_part = f" + {self.b}"
        elif self.b < 0:
            b_part = f" - {abs(self.b)}"
        else:
            b_part = ""

        return f"y = {m_part}{b_part}"

    
eq1 = LinearEquation(2, 3)
eq2 = LinearEquation(-1, 5)

eq_sum = eq1 + eq2
print("Linear Equation 1:", eq1)
print("Linear Equation 2:", eq2)
print("Sum:", eq_sum)



#4
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes

        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60
        
        return Time(total_hours, total_minutes)
    
    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"
    
t1 = Time(1, 30)
t2 = Time(2, 45)

t_sum = t1 + t2
print("\nTime1:", t1)
print("Time2:", t2)
print("Sum:", t_sum)



#5
class RGBColor:
    def __init__(self, r, g, b):
        self.r = max(0, min(255, int(r)))
        self.g = max(0, min(255, int(g)))
        self.b = max(0, min(255, int(b)))

    def __add__(self, other):
        self.r = min(255, (self.r + other.r) // 2)
        self.g = min(255, (self.g + other.g) // 2)
        self.b = min(255, (self.b + other.b) // 2)
        return self

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)

c3 = c1 + c2
print("Color 1 = ", c1)
print("Color 2 = ", c2)
print("Combined Color:", c3)



#6
class RationalNumber:
    def __init__(self, numerator, denorminator):
        self.numerator = numerator
        self.denominator = denorminator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

r1 = RationalNumber(1, 3)
r2 = RationalNumber(1, 2)

r3 = r1 + r2

print(r1)
print(r2)
print(f"Sum:", r3)



#7
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        if self.b == 0:
            return f"{self.a}"
        if self.a == 0:
            return f"{self.b}i"
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        if self.b < 0:
            return f"{self.a} {self.b}i"



z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(-1, 4)
z3 = ComplexNumber(3, 2)


print(f"{z1} = {z2}? {z1 == z2}")
print(f"{z1} = {z3}? {z1 == z3}")

print("z1:", z1)
print("z2:", z2)
print("z3:", z3)



#8
class Playlist:
    def __init__(self, name = "New Playlist", songs = None):
        self.name = name
        self.songs = songs if songs is not None else []

    def add_song(self, song):
        self.songs.append(song)
        
    def __add__(self, other):
        new_name = f"{self.name} + {other.name}"
        new_list = Playlist(new_name, self.songs + other.songs)
        return new_list

    def __str__(self):
        return f"{self.name}: {self.songs}"

p1 = Playlist(songs=["Song A"])
p2 = Playlist("Favorite", ["Song C"])

p1.add_song("Song B")
p2.add_song("Song D")

p3 = p1 + p2

print("Combined Playlist:")
print(p3)



#9
class ShoppingCart:
    def __init__(self, initial_items=None):
        self.items = initial_items.copy() if initial_items else {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def __add__(self, other):
        combined = self.items.copy()
        for item, quantity in other.items.items():
            if item in combined:
                combined[item] += quantity
            else:
                combined[item] = quantity
        
        return ShoppingCart(combined)
    
    def __str__(self):
        if not self.items:
            return "ShoppingCart is empty"
        
        result = ""
        for item, quantity in self.items.items():
            result += f"{item}: {quantity}, "

        return result

# 사용 예제
cart1 = ShoppingCart()
cart1.add_item("tea")
cart1.add_item("energy drink")
cart1.add_item("energy drink")

cart2 = ShoppingCart({"energy drink": 3, "hat": 1})

combined = cart1 + cart2

print("Cart 1:", cart1)
print("Cart 2:", cart2)
print("Combined Cart:", combined)



#10
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
    def __mul__(self, n):
        self.width *= n
        self.height *= n
        return self

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"
    
r1 = Rectangle(4, 5)
print("Before multiplication:", r1)

r1 * 3
print("After multiplication:", r1)
print("Area:", r1.area())