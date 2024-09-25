import pandas as pd
import pymysql as py
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:KushagraGupta192035@localhost:3306/Library")
s0=pd.read_sql_table("members",engine)
s0.set_index("registration_no",inplace=True)
list1=["academic","biography","mystery","fantasy"]
while True :
 print("\n","—★—"*25)
 print("\nAvailable Genres :-\n")
 for i in list1 :
  print(i)
 print("\nTo become a member of the library, press 1")
 print("\nTo issue a book, press 2")
 print("\nTo return a book, press 3")
 a=int(input("\nEnter your choice :- "))
 if a==1 :
  z=pd.read_sql_query("select count(*) from members",engine)
  z1=z.iloc[0,0]+1
  fname=input("Enter your first name :- ")
  lname=input("Enter your last name :- ")
  s0.loc[z1,"library_id"]=fname+lname+str(z1)
  s0.loc[z1,"first_name"]=fname
  s0.loc[z1,"last_name"]=lname
  s0.loc[z1,"address"]=input("Enter your address :- ")
  s0.loc[z1,"city"]=input("Enter your city :- ")
  s0.loc[z1,"contact_no"]=input("Enter your contact number :- ")
  s0.loc[z1,"email_id"]=input("Enter your email-id :- ")
  print("\nCongratulations ! You are now a member of our library. Enjoy reading !")
  print("\nYour library_id is :- ",fname+lname+str(z1))
  print("\nYou will have to pay a registration fees of Rs.1000. Thereafter you will have to pay Rs.75 as issue fees every month so as to be allowed to issue books from the library.")
  print("\nWarning :- If you don't pay issue fees for consecutively 3 months then your membership will get expired.")
  print("\nNote :- You cannot issue more than three books. It means that if you have already issued three books then you can't issue a fourth book until you have returned atleast one of the three books that you have already got issued.")
  s0.to_sql("members",engine,if_exists="replace")
 elif a==2 :
  library_id=input("\nEnter your library_id :- ")
  if library_id in list(s0.library_id) :
   x=pd.read_sql_query("select count(*) from issued_books where library_id ='"+library_id+"'",engine)
   x1=x.iloc[0,0]
   if x1<=2:
    genre=input("\nEnter the genre of your choice :- ")
    if genre in list1:
     s=pd.read_sql_table(genre,engine)
     s.set_index("book_id",inplace=True)
     s1=pd.read_sql_table("issued_books",engine)
     s1.set_index("book_id",inplace=True)
     print("\n\tAvailable Books :- ")
     print(s)
     book_id=int(input("\nEnter the book_id :- "))
     s1.loc[book_id,"book_name"]=s.loc[book_id,"book_name"]
     s1.loc[book_id,"library_id"]=library_id
     s1.loc[book_id,"day_of_issue"]=int(input("\nEnter the day(number) of issue :- "))
     s1.loc[book_id,"month_of_issue"]=int(input("\nEnter the month(number) of issue :- "))
     s1.loc[book_id,"year_of_issue"]=int(input("\nEnter the year of issue :- "))
     s=s.drop(book_id,axis=0)
     s.to_sql(genre,engine,if_exists="replace")
     s1.sort_values(by="book_id").to_sql("issued_books",engine,if_exists="replace")
     print("\nThe book has been issued successfully.")
     print("If the book is not returned within 15 days of issuing, a fine of Rs. 2 will be charged for each additional day.")
    else :
     print("\n The genre entered is invalid. Please note that the genre is case sensitive.")
   else :
    print("\nThe person having the entered library_id already has three issued books.")
  else :
   print("The library_id entered is invalid. Please note that the library_id is case sensitive.")
 elif a==3:
  s1=pd.read_sql_table("issued_books",engine)
  s1.set_index("book_id",inplace=True)
  library_id=input("\nEnter your library_id :- ")
  if library_id in list(s0.library_id) :
   if library_id in list(s1.library_id) :
    s2=pd.read_sql_query("select * from issued_books where library_id='"+library_id+"'",engine)
    s2.set_index("book_id",inplace=True)
    print("\nBooks issued by the person having library_id :- ",library_id," are :- \n")
    print(s2)
    book_id=int(input("\nEnter the book_id :- "))
    genre=input("Enter the genre of the book :- ")
    if genre in list1:
     s=pd.read_sql_table(genre,engine)
     s.set_index("book_id",inplace=True)
     day1=int(input("\nEnter the day(number) of returning :- "))
     month1=int(input("\nEnter the month(number) of returning :- "))
     year1=int(input("\nEnter the year of returning :- "))
     days=(year1-s2.loc[book_id,"year_of_issue"])*360 + (month1-s2.loc[book_id,"month_of_issue"])*30 + (day1-s2.loc[book_id,"day_of_issue"])*1
     if days<=15:
      print("\nThe book has been returned successfully.")
      print("\nYou don't have to pay any fine.")
     else :
      fine=(days-15)*2
      print("\nThe book has been returned successfully.")
      print("\nYou have to pay a fine of Rs. ",fine)
     s.loc[book_id,:]=s1.loc[book_id,"book_name"]
     s1=s1.drop(book_id,axis=0)
     s.sort_values(by="book_id").to_sql(genre,engine,if_exists="replace")
     s1.to_sql("issued_books",engine,if_exists="replace")
    else :
     print("\nThe genre entered is invalid. Please note that the genre is case sensitive")
   else :
    print("\nNo books are issued by the person having the entered library_id.")
  else :
   print("The library_id entered is invalid. Please note that the library_id is case sensitive.")
 else :
  print("\nPlease enter a valid choice.")