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