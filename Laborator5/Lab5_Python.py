# 1. Create a class hierarchy for shapes, starting with a base class Shape. 
# Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods 
# to calculate area and perimeter for each shape.
import math

class Shape:
    def area(self): pass
    def perimeter(self): pass
    def calculate_center(self): pass
    def display(self): pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

    def display(self):
        print(f"Cerc cu  raza {self.r}")
        print(f"Arie: {self.area()}")
        print(f"Perimetru: {self.perimeter()}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Dreptunghi cu lungime {self.length} si  latime {self.width}")
        print(f"Arie: {self.area()}")
        print(f"Perimetru: {self.perimeter()}")

class Triangle(Shape):
    def __init__(self, lat1, lat2, lat3):
        self.lat1 = lat1
        self.lat2 = lat2
        self.lat3 = lat3

    def area(self):
        s = (self.lat1 + self.lat2 + self.lat3) / 2
        return math.sqrt(s * (s - self.lat1) * (s - self.lat2) * (s - self.lat3))

    def perimeter(self):
        return self.lat1 + self.lat2 + self.lat3

    def display(self):
        print(f"Triunghi cu laturile: {self.lat1}, {self.lat2}, {self.lat3}")
        print(f"Arie: {self.area()}")
        print(f"Perimetru: {self.perimeter()}")

circle = Circle(7)
circle.display()
rectangle = Rectangle(10, 3)
rectangle.display()
triangle = Triangle(5, 4, 5)
triangle.display()


# 2. Design a bank account system with a base class Account and subclasses 
# SavingsAccount and CheckingAccount. Implement methods for deposit, withdrawal, 
# and interest calculation.

class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Depunere: +{amount}")
        print(f"Suma depusa: {amount}. Sold nou: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append("Retragere: +{amount}")
            print(f"Retragere: {amount}. Noul sold: {self.balance}")
        else:
            print("Fonfuri insuficiente")

    def calculate_interest(self):
        pass

    def display(self):pass

    
class SavingsAccount(Account):
    def __init__(self, name, account_number, balance=0, interest_rate=0.02):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Noul sold: {self.balance}")

    def display(self):
        print("Tranzactii:", self.transactions)


class CheckingAccount(Account):
    def __init__(self, name, account_number, balance=0, overdraft_limit=100):
        super().__init__(name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Retragere: -{amount}")
            print(f"Retragere {amount}. Sold nou: {self.balance}")
        else:
            print("Fonduri insuficiente")

    def display(self):
        print("Tranzactii:", self.transactions)


savings = SavingsAccount("Razvan",account_number=1, balance=1000)
savings.deposit(500)
savings.calculate_interest()
savings.display()

checking = CheckingAccount("Maria", account_number=2, balance=500, overdraft_limit=200)
checking.withdraw(700)
checking.display()



# 3. Create a base class Vehicle with attributes like make, model, and year, and then 
# create subclasses for specific types of vehicles like Car, Motorcycle, and Truck. 
# Add methods to calculate mileage or towing capacity based on the vehicle type.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency, num_passengers):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency
        self.num_passengers = num_passengers

    def display_info(self):
        return super().display_info() + f", Consum combustibil: {self.fuel_efficiency} L/100 km, Pasageri: {self.num_passengers}"

    def calculate_mileage(self, distance):
        return distance / (self.fuel_efficiency / 100)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  

    def display_info(self):
        return super().display_info() + f", Consum combustibil: {self.fuel_efficiency} L/100 km"

    def calculate_mileage(self, distance):
        return distance / (self.fuel_efficiency / 100)

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity, num_passengers):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity  
        self.num_passengers = num_passengers

    def display_info(self):
        return super().display_info() + f", Capacitate Remorcare: {self.towing_capacity} tone, Passengers: {self.num_passengers}"

    def calculate_towing_capacity(self):
        return self.towing_capacity

car = Car("Toyota", "Camry", 2022, 7.8, 5) 
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 5.6) 
truck = Truck("Ford", "F-150", 2023, 3, 3)

print(car.display_info())
print("Mileage:", car.calculate_mileage(150))  

print(motorcycle.display_info())
print("Mileage:", motorcycle.calculate_mileage(100))  

print(truck.display_info())
print("Towing Capacity:", truck.calculate_towing_capacity())

# 4. Build an employee hierarchy with a base class Employee. Create subclasses for 
# different types of employees like Manager, Engineer, and Salesperson. Each subclass 
# should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.employee_id}")
        print(f"Nume: {self.name}")
        print(f"Salariu: {self.salary} lei")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, num_engineers, num_projects):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.num_engineers = num_engineers
        self.num_projects = num_projects
        self.projects = []
    def add_project(self, name_project):
            self.num_projects += 1
            self.projects.append(name_project)
            print(f"Proiectul '{name_project}' a fost adăugat. Nr proiecte acum: {self.num_projects}")

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Nr ingineri: {self.num_engineers}")
        print(f"Nr proiecte: {self.num_projects}")
        print(f"Proiecte: {self.projects}")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language, num_projects, tickets):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
        self.num_projects = num_projects
        self.tickets = tickets

    def display_info(self):
        super().display_info()
        print(f"Limbat de programare: {self.programming_language}")
        print(f"Nr proiecte: {self.num_projects}")
        print(f"Number of Tickets: {self.tickets}")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_quota, num_projects_selling, customer_list, employment_status):
        super().__init__(name, employee_id, salary)
        self.sales_quota = sales_quota
        self.num_projects_selling = num_projects_selling
        self.customer_list = customer_list
        self.employment_status = employment_status

    def add_client(self, name_client):
        self.customer_list.append(name_client)
        print(f"Clientul '{name_client}' a fost adăugat în lista de clienți.")

    def display_info(self):
        super().display_info()
        print(f"Cota vanzari: {self.sales_quota}")
        print(f"Nr proiecte vandute: {self.num_projects_selling}")
        print(f"Lista clienti: {self.customer_list}")
        print(f"Statutul angajatului: {self.employment_status}")

manager = Manager("Alin", 2, 80000, "Marketing", 10, 8)
engineer = Engineer("Alice", 16, 70000, "Python", 5, 100)
salesperson = Salesperson("Bob", 13, 60000, 100000, 3, ["Company A", "Company B"], "Full-time")

manager.add_project("Proiect A")
manager.display_info()
engineer.display_info()
salesperson.add_client("Company C")
salesperson.display_info()



# 5. Create a class hierarchy for animals, starting with a base class Animal. Then, 
# create subclasses like Mammal, Bird, and Fish. Add properties and methods to 
# represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, habitat, age):
        self.name = name
        self.habitat = habitat
        self.age = age
    
class Mammal(Animal):
    def __init__(self, name, habitat, age, color):
        super().__init__(name, habitat, age)
        self.color = color

    def hunt(self, prey):
        print(f"{self.name} vaneaza {prey}.")
    
    def climb(self, climb=""):
        print(f"{self.name} se urca {climb}.")

class Bird(Animal):
    def __init__(self, name, habitat, age, wingspan, fly):
        super().__init__(name, habitat, age)
        self.wingspan = wingspan
        self.fly = fly

    def can_fly(self):
        if self.fly == True:
            print(f"{self.name} zboara")
        else:
            print(f"{self.name} nu zboara")

    def peck(self):
        print(f"{self.name} are cioc")

    def build_nest(self):
        print(f"{self.name} face cuib")

class Fish(Animal):
    def __init__(self, name, habitat, age, scale_color):
        super().__init__(name, habitat, age)
        self.scale_color = scale_color

    def swim(self): print(f"{self.name} inoata")

    def lay_eggs(self, met):
        if met == "eggs":
            print(f"{self.name} face oua")
        else:
            print(f"{self.name} naste")
    def feed(self):
        print(f"{self.name} is eating")
leu = Mammal("Leul", "savannah", 5, "golden")
leu.hunt("gazele")
leu.climb("pietre")
vultur = Bird("Vulturul", "mountains", 3, 2.5, True)
vultur.can_fly()
vultur.peck()
vultur.build_nest()
goldfish = Fish("Peste", "pond", 1, "gold")
goldfish.swim()
goldfish.lay_eggs("eggs")
goldfish.feed()


# 6. Design a library catalog system with a base class LibraryItem and subclasses for 
# different types of items like Book, DVD, and Magazine. Include methods to check out, 
# return, and display information about each item.

class LibraryItem:
    def __init__(self, title, type, available=True):
        self.title = title
        self.type = type
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            return f"{self.title} checked out"
        else:
            return f"{self.title} is not available"

    def return_item(self):
        if not self.available:
            self.available = True
            return f"{self.title} returned"
        else:
            return f"{self.title} is available"

    def display(self):
        print(f"title: {self.title}")
        print(f"type: {self.type}")
        if not self.available:
            print("Status: Checked Out")
        else:
            print("Status: Available")


class Book(LibraryItem):
    def __init__(self, title, author, available=True):
        super().__init__(title, "book", available)
        self.author = author

    def display_info(self):
        super().display()
        print(f"author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, director, available=True):
        super().__init__(title, "DVD", available)
        self.director = director

    def display_info(self):
        super().display()
        print(f"director: {self.director}")


class Magazine(LibraryItem):
    def __init__(self, title, publication_date, available=True):
        super().__init__(title, "Magazine", available)
        self.publication_date = publication_date

    def display_info(self):
        super().display()
        print(f"publication date: {self.publication_date}")


book1 = Book("1984", "George Orwell")
dvd1 = DVD("Inception", "Christopher Nolan")
magazine1 = Magazine("Time", "15-04-2023")

book1.display_info()
dvd1.display_info()
magazine1.display_info()

print(book1.check_out())
print(dvd1.check_out())
print(magazine1.check_out())

print(book1.return_item())
print(dvd1.return_item())
print(magazine1.return_item())


