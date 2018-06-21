#Create a class Animal as a base class and define method animal_attribute.create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
	def show(self):
		print("class Animal")
class Tiger(Animal):
		print("Tiger")
t=Tiger()
t.show()		