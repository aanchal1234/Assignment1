#Create a function to calculate the area of a circle  by taking radius from user.

radius =int(input("enter radius"))
def circle(r):
		area=3.14*r*r
		return area
		
area=circle(radius)
print(area)		