#1Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import threading
from threading import Thread
import time

def display():
	time.sleep(5)
	print("hello world")

t = Thread(target=display)
t.start()
	

#2Make a thread that prints numbers from 1-10,waits for 1 sec between.

import threading
from threading import Thread
import time

def display():
	for x in  range(10):
		print(x)
		time.sleep(1)
		

t=Thread(target=display)
t.start()

#3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.Delay goes like 2sec-4sec-6sec-8sec-10sec

import threading
from threading import Thread
import time
def display():
	l=[1,2,3,4,5]
	for i in 1:
		a=2
		print(i)
		time.sleep(a)
t=Thread(target=display)
t.start()	



#4 Call factorial function using thread
def factorial():
	n=int(input("enter any number"))
	fact=1
	for x in range(1,n+1):
		fact=fact*x
	print(fact)
t=Thread(target=factorial)
t.start()
