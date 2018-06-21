#Create a circle class and initialize it with radius.Make two methods getArea and get circumference inside this class.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area is=",3.14*self.radius*self.radius)
    def getCircumference(self):
        print("Circumference is=" ,2*3.14*self.radius)
radius=int(input("enter the radius"))
obj=Circle(radius)
obj.getArea()
obj.getCircumference()



#Create a Student class  and initialize it with name and rollnumber.Make methods to:Display-it should display all information of the Student.
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def Display(self):
        print("the name of student is--",self.name)
        print("rollno is--",self.rollno)
name=input("enter the name of student")
rollno=int(input("enter the rollno of student"))
obj1=Student(name,rollno)
obj1.Display()


# Create a temperature class.
#     Make two methodsQ.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class temperature:
    def __init__(self,fahrn,celc):
        self.fahrn=fahrn
        self.celc=celc
    def fah(self):
        fahrn=(1.8)*self.celc+32
        print("convert  fahreinheit into celsius",fahrn)
    def cel(self):
        celc=(self.fahrn-32)*5/9
        print("convert celsius into fahreinheit",celc)
n=int(input("enter any number"))
t1=temperature(n,n)
t1.fah()
t1.cel()


# **Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
# Make methods to
# 1. Display-Display the details.
# 2. Update- Update the movie details.
class moviedetail:
    def __init__(self,moviename,artistname,release,rating):
        self.moviename=moviename
        self.artistname=artistname
        self.release=release
        self.rating=rating
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.release)
        print(self.rating)
    def update(self):
        self.moviename="fukrey"
        self.artistname="varun"
        self.release=1232
        self.rating=4.5


moviename="carry on jatta"
artistname="gippy"
release=345
rating=4.2
m1=moviedetail(moviename,artistname,release,rating)
m1.display()
m1.update()
m1.display()

#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary

class Expenditure:
    def __init__(self):
        self.savings=500
        self.expenditure=1500
    def show(self):
        print("saving is ",self.savings)
        print("expenditureis",self.expenditure)
    def salary(self):
        self.salary=self.expenditure+self.savings
        print(self.salary)
a=Expenditure()
a.show()
a.salary()

