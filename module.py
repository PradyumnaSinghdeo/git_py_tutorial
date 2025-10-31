
# Code Example 4: Real-World Example – Library System

# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.is_checked_out = False
    
#     def check_out(self):
#         if not self.is_checked_out:
#             self.is_checked_out = True
#             print(f"{self.title} checked out")
        
#         else:
#             print(f"{self.title} is already checked out.")
            
#     def return_book(self):
#         if self.is_checked_out:
#             self.is_checked_out = False
#             print(f"{self.title} returned ")
#         else:
#             print(f"{self.title} was not checked out.")
            
# book1 = Book("1984", "George Orwell", "1234567890")
# book1.check_out()
# book1.return_book()


# # Code Example 5: Advanced – Customizing Object Creation


# class singletone:
#     _instance = None
    
#     def __new__ (cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# a = singletone()
# b = singletone()
# print(a is b)


# Inheritance

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def showDetails(self):
#         print(f"The prorammer name is {self.name} and the Id Is {self.id}")
        
# class Programmer(Employee):
#     def showCompany(self):
#         print(f'The company name is TCS')
        
# e = Employee('Khurana', '422')
# e.showDetails()
# e2 = Programmer('Raja', '445')
# e2.showDetails()
# e2.showCompany()




# Class Method

# class Employee:
#     company = "Apple"
    
#     def show(self):
#         print(f'The name of the employee is {self.name}, and the company name is {self.company}')
#     @classmethod    
#     def new_company(self, newcompany):
#         self.company = newcompany
        
# e1 = Employee()
# e1.name = "Harry"
# e1.show()

# e1.new_company("Tesla")
# e1.show()
# print(Employee.company)

# dir() Method
# x = [1, 2, 3]
# print(dir(x))


# __dict__ Method
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# p =Person("John", 30)
# # print(p.__dict__)

# Help() Method

# print(help(Person))







