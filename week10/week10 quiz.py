'''
#1
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_quantity(self, quantity):
        self.quantity = quantity

product1 = Product("Coffee", 5.99, 10)

print("Name:", product1.get_name())
print("Price:", product1.get_price())
print("Quantity:", product1.get_quantity())

product1.set_price(6.49)
print("Updated Price:", product1.get_price())



#2
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_page_count(self):
        return self.page_count
    
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_page_count(self,page_count):
        self.page_count = page_count

book1 = Book("1984", "George Orwell", 328)

print("Title:", book1.get_title())
print("Author:", book1.get_author())
print("Page count:", book1.get_page_count())

book1.set_page_count(428)
print("Updated Page Count:", book1.get_page_count())



#3
class Movie:
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    def get_title(self):
        return self.title
    def get_director(self):
        return self.director
    def get_runtime_minutes(self):
        return self.runtime_minutes
    
    def set_title(self, title):
        self.title = title
    def set_director(self, director):
        self.director = director
    def set_runtime_minutes(self, runtime_minutes):
        self.runtime_minutes = runtime_minutes
    
movie1 = Movie("Interstellar", "Christopher Nolan", 148)

print("Title:", movie1.get_title())
print("Director:", movie1.get_director())
print("Runtime minutes:", movie1.get_runtime_minutes())

movie1.set_title("Inception")
print("Updated Movie Title:", movie1.get_title())




#4
class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_duration_seconds(self):
        return self.duration_seconds

    def set_title(self, title):
        self.title = title
    def set_artist(self, artist):
        self.artist = artist
    def set_duratiion_seconds(self, duration_seconds):
        self.duration_seconds = duration_seconds
    
song1 = Song("No surprises", "Sade", 229)

print(f"{song1.get_title()} - {song1.get_artist()} ({song1.get_duration_seconds()} seconds)")

song1.set_artist("Radiohead")

print(f"{song1.get_title()} - {song1.get_artist()} ({song1.get_duration_seconds()} seconds)")



#5
class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def get_name(self):
        return self.name
    def get_title(self):
        return self.title
    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name
    def set_title(self, title):
        self.title = title
    def set_salary(self, salary):
        self.salary = salary

    def greeting(self):
        return f"Hello. My name is {self.name}. I'm the {self.title}."
    def request_raise(self):
        new_salary = self.salary * 1.06
        return f"I'm currently making ${self.salary}. I'd like new salary of ${new_salary}."


# --- 예시 사용 ---
employee1 = Employee("Eugene", "CEO", 100)
print(employee1.greeting())
print(employee1.request_raise())

employee1.set_salary(120)
print(employee1.request_raise())



#6
class Student:
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA
    
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_GPA(self):
        return self.GPA

    def set_name(self, name):
        self.name = name
    def set_major(self, major):
        self.major = major
    def set_GPA(self, GPA):
        if 0 <= self.GPA <= 4.0:
            self.GPA = GPA

    def introduce(self):
        return f"Hi, I'm {self.name}. I'm studying {self.major}."
    def study_for_exam(self):
        old_GPA = self.GPA
        new_GPA = old_GPA + 0.2

        if new_GPA > 4.0:
            new_GPA = 4.0
        self.GPA = new_GPA
        return f"I'm hitting the books! My GPA increased from {old_GPA} to {new_GPA}."


# --- 예시 사용 ---
student1 = Student("Maria", "Computer Science", 3.9)

print(student1.introduce())
print(student1.study_for_exam())



#7
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    
    def set_make(self, make):
        self.make = make
    def set_model(self, model):
        self.model = model
    def set_year(self, year):
        self.year = year
    
    def print_vehicle_type(self):
        print (f"{self.year} {self.make} {self.model}")

car = Vehicle("Toyota", "Camry", 2021)
car.print_vehicle_type()

car.set_year(2020)
car.print_vehicle_type()


'''
#8




#9
#10
#11
#12
#13
#14
#15