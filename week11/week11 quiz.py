#1-(a)
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_major(self):
        return self.major
    
    def set_major(self, _major):
        self.major = _major
    
    def __str__(self):
        return f"Student Name: {self.name}, Major: {self.major}"

#1-(b)
class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []
    
    def get_number(self):
        return self.course_number
    
    def set_number(self, _course_number):
        self.course_number = _course_number
    
    def add_student(self, student):
        self.students.append(student)

    def show_student_enrollment(self):
        if not self.students:
            print("No students enrolled yet.")
        else:
            print("Students enrolled:")
            for student in self.students:
                print("-", student)

    def __str__(self):
        return f"Course: {self.course_name} ({self.course_number}), Enrolled: {len(self.students)} students"

#1-(c)
course1 = Course("Molecular Biology", "BIO201")

student1 = Student("Seonmin Kim", "Environmental Biochemistry")
student2 = Student("Minju Lee", "Biotechnology")

course1.add_student(student1)
course1.add_student(student2)

print(course1)
course1.show_student_enrollment()



#2-(a)
class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, _color):
        self.color = _color

    def speak(self):
        print(f"{self.name} says: Quack!")

    def __str__(self):
        return f"{self.name} the {self.color} duck"

#2-(b)
class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []
    
    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        if not self.ducks:
            print("there are no ducks in the pond.")
        else:
            print(f"In {self.name} pond:")
            for duck in self.ducks:
                duck.speak()

    def __str__(self):
        return f"Pond: {self.name}, Ducks: {len(self.ducks)}"
        
#2-(c)
pond1 = Pond("Sunshine Pond")

duck1 = Duck("Daisy", "yellow")
duck2 = Duck("Donald", "white")

pond1.add_duck(duck1)
pond1.add_duck(duck2)

print(pond1)
pond1.ducks_quack()



#3-(a)
class Lion:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name
    
    def set_name(self, _name):
        self.name = _name

    def roar(self):
        print(f"{self.name} says: Roar!")
    
    def __str__(self):
        return f"Lion: {self.name} ({self.gender})"

#3-(b)
class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []

    def add_lion(self, lion):
        self.lions.append(lion)

    def lions_roar(self):
        if not self.lions:
            print("There are no lions in the zoo.")
        else:
            print(f"In {self.location} Zoo:")
            for lion in self.lions:
                lion.roar()

    def count_lions(self):
        male_count = sum(1 for lion in self.lions if lion.gender.lower() == "male")
        female_count = sum(1 for lion in self.lions if lion.gender.lower() == "female")
        print(f"{male_count} male, {female_count} female")
    
    def __str__(self):
        return f"Zoo location: {self.location}, Lions: {len(self.lions)}"

#3-(c)
zoo1 = Zoo("Seoul Safari")

lion1 = Lion("Simba", "male")
lion2 = Lion("Nala", "female")

zoo1.add_lion(lion1)
zoo1.add_lion(lion2)

print(zoo1)
zoo1.lions_roar()
zoo1.count_lions()



#4-(a)
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position
    
    def set_position(self, _position):
        self.position = _position
    
    def __str__(self):
        return f"Employee: {self.name}, Position: {self.position}"
    
#4-(b)
class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget
    
    def set_budget(self, _budget):
        self.budget = _budget
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def show_staff_list(self):
        if not self.employees:
            print(f"There are no employees in {self.dept_name} department.")
        else:
            print(f"Employees in {self.dept_name} Department:")
            for emp in self.employees:
                print("-", emp)

    def is_large(self):
        return len(self.employees) >= 10
            
    def __str__(self):
        return f"Department: {self.dept_name}, Budget: ${self.budget}, Employees: {len(self.employees)}"

#4-(c)
employee1 = Employee("Alice", "Researcher")
employee2 = Employee("Bob", "Analyst")

bio_dept = Department("Bioinformatics", 500000)

bio_dept.add_employee(employee1)
bio_dept.add_employee(employee2)

print(bio_dept)
print(bio_dept.show_staff_list())
print("Is large department?", bio_dept.is_large())



#5-(a)
class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series
    
    def get_series(self):
        return self.series
    
    def set_series(self,_series):
        self.series = _series
    
    def communicate(self):
        print("Beep-Bloop-Blop")

    def __str__(self):
        return f"Droid {self.designation} (Series {self.series})"        

#5-(b)
class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []
    
    def add_droid(self, droid):
        self.droids.append(droid)
    
    def droids_communicate(self):
        if not self.droids:
            print(f"No droids aboard this starship.")
        else:
            print(f"All droids on {self.name} are communicating:")
            for droid in self.droids:
                print(f"{droid.designation} says: ", end = "")
                droid.communicate()

    def __str__(self):
        return f"Starship {self.name} with {len(self.droids)} droid(s)."

#5-(c)
droid1 = Droid("R2-D2", "Astromech")
droid2 = Droid("C-3PO", "Protocol")

falcon = Starship("Millennium Falcon")

falcon.add_droid(droid1)
falcon.add_droid(droid2)

print(falcon)
falcon.droids_communicate()



#6-(a)
class Post:
    def __init__(self, caption, likes):
        self.caption = caption
        self.likes = likes

    def get_likes(self):
        return self.likes
    
    def add_like(self):
        self.likes += 1

    def display(self):
        print(f"Post: {self.caption}")
    
    def __str__(self):
        return f"'{self.caption}' - {self.likes} likes"

#6-(b)
class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)

    def display_trending_posts(self):
        trending = [post for post in self.posts if post.get_likes() >= 10000]
        if not trending:
            print(f"{self.username} has no trending posts.")
        else:
            print(f"{self.username}'s trending posts:")
            for post in trending:
                post.display()

    def __str__(self):
        return f"Profile: {self.username}, Total posts: {len(self.posts)}"
    
#6-(c)
profile1 = Profile("seonmin_kim")

post1 = Post("Enjoying a sunny day!", 500)
post2 = Post("My new art just hit 12k likes!", 12000)

profile1.add_post(post1)
profile1.add_post(post2)

profile1.display_trending_posts()



#7-(a)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
    
    def set_price(self, _price):
        self.price = _price
    
    def display_details(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}")

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

#7-(b)
class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = sum(product.get_price() for product in self.products)
        return total
    
    def __str__(self):
        return f"ShoppingCart for Customer {self.customer_id}, Total items: {len(self.products)}"
    
#7-(c)
cart1 = ShoppingCart("CUST123")

product1 = Product("Wireless Mouse", 25.99)
product2 = Product("Mechanical Keyboard", 79.99)

cart1.add_product(product1)
cart1.add_product(product2)

total_price = cart1.calculate_total()
print(f"Total price of all products in the cart: ${total_price:.2f}")



#8-(a)

#8-(b)

#8-(c)



#9-(a)

#9-(b)

#9-(c)



#10-(a)

#10-(b)

#10-(c)



#11-(a)

#11-(b)

#11-(c)



#12-(a)

#12-(b)

#12-(c)