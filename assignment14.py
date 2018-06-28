# #1- Write a Python program to read last n lines of a file.
# p=0
# count_line=0
# n=int(input("enter the number of lines you want to print from last"))
# f1=open('test.txt','r')
# for  line in f1:
#     count_line=count_line+1
# m=count_line-n
# f1.seek(0)
# for line in f1:
#     p+=1
#     if p>m:
#         print(line)

#2- Write a Python program to count the frequency of words in a file.
with open('test.txt','r')as f:
    content=f.read()
    words=content.split()
    print(words)
    s=set(words)
    print(s)
    for b  in s:
        print(words.count(b))






# #3- Write a Python program to copy the contents of a file to another file
# with open('test.txt','r')as f1:
#     with open('test2.txt','w') as f2:
#         for line in f1:
#             f2.write(line)



# #Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
# f=open('test.txt','r')
# content=f.readlines()
# f.close()
# # print(content)
# f1=open('test2.txt','r')
# abc=f1.readlines()
# f1.close()
# # print(abc)
# n = 0
# for i in content:
#     print(content[n]+abc[n])
#     n = n + 1
#




#5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
# import random
# with open('test.txt','w')as f:
#     for x in range(10):
#         n=random.randint(0,9)
#         f.write(str(n))
#         f.write("\n")
#
# with open('test.txt','r')as f:
#     l=f.readlines()
#
# l.sort()
#
# with open('test2.txt','w')as f:
#     for n in l:
#         f.write(n)
#         f.write("\n")
