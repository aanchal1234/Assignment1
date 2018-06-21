#Create a class Animal as a base class and define method animal_attribute.create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
	def show(self):
		print("class Animal")
class Tiger(Animal):
		print("Tiger")
t=Tiger()
t.show()		

#What will be the output of following code:
class A:
	def f(self):
		return self.g()
		
	def g(self):
		return ('A')
		
class B(A):
	def g(self):
		return ('B')

a=A()
b=B()
print(a.f(), b.f())
print(a.g(),b.g())

#Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
		
class cop:
    def add(self,name,age,work_exp,designation):
        self.name=name
        self.age=age
        self.work_exp=work_exp
        self.designation=designation
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("work experience : ",self.work_exp)
        print("designation : ",self.designation)
    def update(self,name,age,work_exp,designation):
        self.name = name
        self.age = age
        self.work_exp = work_exp
        self.designation = designation

class mission(cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)

m1= mission()
m1.add_mission_details("assigned to petrolling")
m1.add("bhawna",19,0,"manager")
m1.display()
       
#Create a class Shape.initialize it with length and breadth Create the method Area.Create class	 rectangle and square which inherits shape and access the method Area.

class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
class Rectangle(Shape):
	def area_Rectangle(self):
		self.Area=self.length*self.breadth
		print("Area of Rectangle is :",self.Area)
class square(Shape):
	def area_square(self):
		self.Area=self.length*self.breadth
		print("Area of square is :",self.Area)

length=int(input("enter the length"))
breadth=int(input("enter the breadth"))

if length==breadth:
	b=square(length,breadth)
	b.area_square()
	
else:
	a=Rectangle(length,breadth)
	a.area_Rectangle()	
		
		
		
	
	
