from PIL import Image, ImageDraw
import math
# API driven programming

class Polygon:
    def __init__(self, v):
        self.vertices = v
       # a tuple of 2-D points

    def getCoordinates (self):                #This function will automatically
        self.c1 = self.vertices[0]            #take first three coordinates. Also,
        self.c2 = self.vertices[1]            #smallest polygon will have 3 vertices
        self.c3 = self.vertices[2]

    def drawMethod(self):
        self.img = Image.new('RGB', (640, 480))
        draw = ImageDraw.Draw(self.img)
        draw.polygon((self.vertices))
        self.img.show()
    ## Area method gets overridden in child classes -- polymorphism example
    def area(self):
        pass

        
v = Polygon(((46, 70), (54, 70), (60, 150), (50, 200), (40, 150)))
v.drawMethod()

# Inheritance -- Rectangle and Triangle Inherit the attributes of Polygon
class Rectangle(Polygon):
    def area(self):
        self.getCoordinates()
        length = math.sqrt((self.c2[1] - self.c1[1])**2 + (self.c2[0] - self.c1[0])**2)
        width = math.sqrt((self.c3[1] - self.c2[1])**2 + (self.c3[0] - self.c2[0])**2)
        return length*width


class Triangle(Polygon):
    def area(self):
        self.getCoordinates()
        return abs(self.c1[0]*(self.c2[1] - self.c3[1]) + self.c2[0]*(self.c3[1] - self.c1[1]) + self.c3[0]*(self.c1[1] - self.c2[1]))/2
    
x = Rectangle(((0, 0), (0, 10), (5, 10), (10, 0)))

#print(x.area())

y = Triangle(((0, 50), (25, 60), (0, 0)))

#print(y.area())


### Encapsulation -- one can make the class members private and protected by adding __ or _ before
### variable names.

class Employee:
    # constructor                               # Remember that you should use underscore (for encapsulation) only
                                                # while defining any function, after that use directly the name of argument.
    def __init__(self, name, salary, project):
        # data members
        self.name = name    # Say public member accessible by everyone
        self.salary = salary
        #self.__salary = salary # private member -- "accessible" from within the class only
        # (scope of class)
        self.project = project
        # self._project = project #say protected member -- i.e. accessible within the class and "its subclasses"
        # (scope of class, and also its local scope)

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('SVS', '10K', 'Verification')
emp.show()
emp.work()
# print(emp.__salary) ## will give a runtime error


#To show protected aspects
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)      # This constructor will call all the methods of parent class

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)


