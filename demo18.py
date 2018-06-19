#An if statement that lets a competitor know which of these prizes they won based on the number of points they scored.
score=int(input("enter your score : "))
if score>180 and score<=200:
	print("congratulations!you won a chocolate")
elif score>150 and score<181:	
	print("congratulations you won a book")
elif score>50 and score<151:
	print("congratulations you won a wooden dog")
elif score>0 and score<51:
	print("sorry!no prize this time")