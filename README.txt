Python Libraries used:-
a).pandas
b).sqlalchemy
c).pymysql
Database library is created using MySQL.

Brief explanation of the project:-
The program allows a user to:-
i). become a member of the library by registering itself into the Library's database.
ii). Issue upto 3 books from the library, i.e., at any point of time, the user cannot hold more than 3 books. For issuing a fourth book, it has to return atleast 1 of the previously issued books.
iii).Return the books back and also generates the fine to be paid in case of late returning.
Internal functioning:-
i). The python program (main.py) provides the user 3 with 3 options, each for performing one of the 3 above mentioned tasks.
ii). The books are categorized on the basis of their genres.
iii). The data of the books, registered members and issued books is stored in the form of tables in a database named library in MySQL.
iv). Whenever a user performs any of the 3 tasks in the pyhton program, the data in the tables get modified accordingly.
