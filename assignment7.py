# Write a function"perfect"() that determines if parameter number is a perfect number.use this function in a program determines and print all the perfect numbers between 1 and 1000.
p = []
def perfect():
    for x in range(1, 1000):
        li = []
        sum = 0
        for y in range(1, x):
            if (x % y == 0):
                li.append(y)
        for a in li:
            sum = sum + a
        if (sum == x):
            p.append(x)
perfect()
print(p)

# print multiplication table of 12 using  recursion.
print("Print multiplication table of 12 using  recursion\n")
n = 12
i = 1
def table(n, i):
    if i > 10:
        return
    else:
        print(n * i)
        table(n, i + 1)
table(12, i)
print("\n...........")

# Write a function to find factorial of a number but also store the factorials calc ulated in a dictionary.
print("Write a function to find factorial of a number but also store the factorials calc ulated in a dictionary")
x = int(input("enter the number  whose factorial you want to calculate"))
dict = {}
def fact(a):
    if a == 1 or a == 0:
        return 1
    else:
        ans = a * fact(a - 1)
        return ans
ans = fact(x)
dict[x] = ans
print(dict)

# Write a function to calculate power of  a number raised to other(a^b) using recursion
print("Write a function to calculate power of  a number raised to other(a^b) using recursion")
x = int(input("enter any number whose power you want to calculate "))
y = int(input("enter the number you want to use the power"))
def power(x, y):
    ans = 1
    if y == 1:
        return x
    else:
        ans = x * power(x, y - 1)
        return ans
print(power(x, y))
print("\n................")
