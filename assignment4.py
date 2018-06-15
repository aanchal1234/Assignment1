#Find the length of tuple
t={1,2,3,4}
print(len(t))


#larger and smallest in tuple
t1={6,7,8,9}
print(max(t))
print(min(t))

#product of all elements
t1=(1,2,3,4)
c=1

for a  in range(0,4)
	k=t1[a]
	c=k*c
	print(c)

#intersection
s1=set([1,2,3,4])
s2=set([4,5,6,7])
print(s1&s2)

#difference
s1=set([1,2,3,4])
s2=set([4,5,6,7])
print(s1-s2)

#create dictionary
l={}
d={}
for x in range(0,10):
	name=input("enter any name")
	marks=int(input("enter any marks")
	d[name]=marks
	l.append(marks)
print(l)
print(d)
l.sort()
print(l)

#count the number of occurence of each letter 
s="MISSISSIPPI"
a=list(s)
a=s.count('M')
b=s.count('I')
c=s.count('S')
d=s.count('P')
d1={'M':a,'I':b,'S':c,'P':d}

print("The number of occurence of each letter MISSISSIPPI")
print(d1)