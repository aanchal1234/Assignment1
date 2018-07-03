#1
import pymysql
db=pymysql.connect("localhost",'root','aanchal98','student')
cursor=db.cursor()
# qr1="create  table zipcode(zipcode_id int,city char(5),state char(5),zipcode  int)"
# qr2="create  table titles(title_id int,title char(20),publisher_id int,publisher_year int)"
# qr3="create  table author_titles(author_title_id int,author_id varchar(10),title_id  int(8))"
# qr4="create  table   authors(author_id int,first_name char(4),middle_name char(3),last_name char(12))"
# qr5="create  table book(book_id int,title_id int,location char(10),genre char(5))"
# cursor.execute(qr1)
# cursor.execute(qr2)
# cursor.execute(qr3)
# cursor.execute(qr4)
# cursor.execute(qr5)
# db.close()
#
# #2
# import  pymysql
# db=pymysql.connect("localhost",'root','aanchal98','student')
# cursor=db.cursor()
# qr1="insert into zipcode(100,"Ambala",'haryana',seventh)"
# qr2="insert into titles(101,"carry on jyatt",312,100,2018)"
# qr3="insert into author_titles(101,"abcd",10121)"
# qr4="insert into authors(101,"bhawna","dua","abc")"
# qr5="insert into  book(101,123,fgh,def)"
# try:
#     cursor.execute(qr1)
#     cursor.execute(qr2)
#     cursor.execute(qr3)
#     cursor.execute(qr4)
#     cursor.execute(qr5)
#     db.commit()
# except:
#     db.rollback()
# db.close()

#3
import  pymysql
db=pymysql.connect("localhost",'root','aanchal98','student')
qr1="update student set city="Ambala" where zipcode_id='123'"
qr2="update student set title_id=101 where  title='hello world'"
qr3="update student set author_id=abc where  title_id=12345"
qr4="update student set  first_name="bhawma"  where middle_name='def'"
qr5="update student set book_id=102 where title_id=105"
try:
    cursor.execute(qr1)
    cursor.execute(qr2)
    cursor.execute(qr3)
    cursor.execute(qr4)
    cursor.execute(qr5)
    db.commit()
except:
    db.rollback()
db.close()



