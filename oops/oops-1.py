#oops
#class declaration
'''class details():
    name='koushik'
    age=13
    place='HYD'
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place        
    def display(self):
        print(self.name,self.age,self.place)        
a=details()
print(dir(a))
a.Data('satya',25,'USA')
a.display()'''

#object intialization
'''class details():
    #create a consrtuctor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details('sam',25,'HYD')
print(dir(a))
a.display()'''

#task
'''class details:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("place:", self.place)
        
name = input("enter the name: ")
age = input("enter the age: ")
place = input("enter the place: ")
a = details(name, age, place)
print(dir(a))
a.display()'''

#Task1 ans
'''class details():
    #create a consrtuctor
    def __init__(self,name,age,place):
        self.name=input('enter your name ')
        self.age=int(input('enter your age '))
        self.place=input('enter your place ')
    def display(self):
        print(self.name,self.age,self.place)
a=details('sam',25,'HYD')
print(dir(a))
a.display()'''

#task2
'''class details():
    def __init__(self):
        self.name = input("Enter your name: ")
        self.mobile_number = int(input("Enter your mobile number: "))
        self.email_id = input("Enter your email ID: ")
    
    def display(self):
        print("Name:", self.name)
        print("Mobile Number:", self.mobile_number)
        print("Email ID:", self.email_id)

a = details()
print(dir(a))
a.display()'''

#diff b/w _ and __
class Employee():
    def __init__(self):
        self .name='koushik'
        self._mail='koushikgujju11@gmail.com'
        self.__salary=100000#private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mail)
#print(a.__salary)
print(a._Employee__salary)


