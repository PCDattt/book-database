#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def view():
    try:
        conn = mysql.connector.connect(host='localhost',
                                             database='book',
                                             user='root',
                                             password='12345')
        if conn.is_connected():
            print("Connected to MySQL Server")
            cur = conn.cursor()
            cur.execute("SELECT book.title, book.pages, book.rating, "
                                " publisher.name as publisher_name,"
	                            " concat(author.lastname,' ', author.firstname) as author_name "
		                " FROM book JOIN book_author ON book.ID = book_author.book_ID "
				                  " JOIN author ON book_author.author_ID = author.ID "
                                  " JOIN publisher ON book.publisher_ID = publisher.ID ")
            rows = cur.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            conn.close()
            cur.close()
            print("MySQL connection is closed")
            return rows

def search(title="",publisher="",pages="",author="",rating=""):
    try:
        conn = mysql.connector.connect(host='localhost',
                                             database='book',
                                             user='root',
                                             password='12345')
        if conn.is_connected():
            print("Connected to MySQL Server")
            cur = conn.cursor()
            cur.execute("SELECT book.title, book.pages, book.rating, "
                                " publisher.name as publisher_name,"
	                            " concat(author.lastname,' ', author.firstname) as author_name "
		                " FROM book JOIN book_author ON book.ID = book_author.book_ID "
				                  " JOIN author ON book_author.author_ID = author.ID "
                                  " JOIN publisher ON book.publisher_ID = publisher.ID "
                        " WHERE book.title LIKE %s OR "
                                "publisher.name LIKE %s OR book.pages = %s "
                                " OR concat(author.lastname,' ', author.firstname) LIKE %s "
                        " OR book.rating = %s",
                        (title,publisher,pages,author,rating))
            rows = cur.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            conn.close()
            cur.close()
            print("MySQL connection is closed")
            return rows






