#Take the input age of  3 people and determine oldest and youngest among them
a=int(input("enter age of person a : "))
b=int(input("enter age of person b : "))
c=int(input("enter age of person c : "))
if a>b:
	if b>c:
		print("a is oldest and c is youngest")
	else:
		if a>c:
			print("a is oldest")
		else:
			print("c is oldest")
		print("b is youngest")
else:
		if a>c:
			("b is oldest c is youngest")
		else:
			if b>c:
				print("b is oldest")
		else:
				print("c is oldest")
			print("a is youngest")	