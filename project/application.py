
import os
import requests
import json

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# api key to goodreads
GOOD_KEY = "IcbtMaQW4GsXKqiJhkuOqg"

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

class Book():
    def __init__(self, id, isbn, title, author, year):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

@app.route("/", methods = ["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        book_list = []
        Uisbn = request.form.get("search_isbn")
        Utitle = request.form. get("search_title")
        Uauthor = request.form.get("search_author")
        if Uisbn == '' and Utitle == '' and Uauthor == '':
            return render_template("index.html", empty_search = True)
        # find by isbn
        if Uisbn != '':
            check_isbn = db.execute("SELECT id, isbn, title, author, year FROM books WHERE isbn = :isbn", {'isbn':Uisbn})
            db.commit()
            book_isbn = check_isbn.fetchone()
            isbn_no_match = False
            if book_isbn == None:
                kommanda = text("SELECT id, isbn, title, author, year FROM books WHERE isbn LIKE :isbn")
                check_isbn = db.execute(kommanda.bindparams(isbn="%"+Uisbn+"%"))
                db.commit()
                book_isbn = check_isbn.fetchone()
                if book_isbn == None:
                    isbn_no_match = True
        else:
            book_isbn = False
            isbn_no_match = True
        # find by title
        if Utitle != '':
            check_title = db.execute("SELECT id, isbn, title, author, year FROM books WHERE title = :title", {'title':Utitle})
            db.commit()
            book_title = check_title.fetchone()
            title_no_match = False
            if book_title == None:
                # check_title = db.execute("SELECT id, isbn, title, author, year FROM books WHERE title ~* :title", {'title':Utitle})
                kommanda = text("SELECT id, isbn, title, author, year FROM books WHERE title LIKE :title")
                check_title = db.execute(kommanda.bindparams(title="%"+Utitle+"%"))
                db.commit()
                book_title = check_title.fetchone()
                if book_title == None:
                    title_no_match = True
        else:
            book_title = False
            title_no_match = True
        # find by author
        if Uauthor != '':
            check_author = db.execute("SELECT id, isbn, title, author, year FROM books WHERE author = :author", {'author':Uauthor})
            db.commit()
            book_author = check_author.fetchall()
            author_no_match = False
            if len(book_author) == 0:
                kommanda = text("SELECT id, isbn, title, author, year FROM books WHERE author LIKE :author LIMIT 10")
                check_author = db.execute(kommanda.bindparams(author="%"+Uauthor+"%"))
                db.commit()
                book_author = check_author.fetchall()
                if len(book_author) == 0:
                    book_list = False
                    author_no_match = True
                else:
                    for b in book_author:
                        book_list.append(b)
            else:
                author_no_match = False
                for b in book_author:
                    book_list.append(b)
        else:
            author_no_match = True
        if author_no_match == True and title_no_match == True and isbn_no_match == True:
            return render_template("index.html", no_match = True)
        return render_template("index.html", book_isbn = book_isbn, book_title = book_title, book_list = book_list,
                                isbn_no_match = isbn_no_match, title_no_match = title_no_match, author_no_match = author_no_match)

# book page
@app.route("/book/<int:book_id>", methods = ["GET", "POST"])
@login_required
def book(book_id):
    if request.method == "GET":
        user = session["user_id"]
        booki = db.execute("SELECT id, isbn, title, author, year FROM books WHERE id = :id", {'id':book_id})
        db.commit()
        book = booki.fetchone()
        otzivi = db.execute("SELECT rate, opinion FROM reviews WHERE user_id = :user_id AND book_id = :book_id", {'user_id':user, 'book_id':book_id})
        db.commit()
        otziv = otzivi.fetchone()
        reviews_of_others = db.execute("SELECT rate, opinion FROM reviews WHERE user_id <> :user_id AND book_id = :book_id", {'user_id':user, 'book_id':book_id})
        db.commit()
        review_of_others = reviews_of_others.fetchone()
        if otziv == None:
            if review_of_others == None:
                return render_template("book.html", book = book, rev_a = True)
            else:
                return render_template("book.html", book = book, rev_a = True, review_of_others = review_of_others)
        else:
            if review_of_others == None:
                return render_template("book.html", book = book, otziv = otziv)
            else:
                return render_template("book.html", book = book, otziv = otziv, review_of_others = review_of_others)
        # API Goodreads now is closed
        # res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": GOOD_KEY, "isbns": book['isbn']})
        # boo = res.json()
        # avg = boo['books'][0]['average_rating']
        # num_otz = boo['books'][0]['work_ratings_count']
        
#    else:
#        booki = db.execute("SELECT id, isbn, title, author, year FROM books WHERE id = :id", {'id':book_id})
#        db.commit()
#        book = booki.fetchone()
#        return render_template("book.html", book = book)


@app.route("/revd/<int:book_id>", methods = ["GET", "POST"])
@login_required
def revd(book_id):
    if request.method == "POST":
        user = session["user_id"]
        Urating = request.form.get("rating")
        Utext = request.form.get("review")
        db.execute("INSERT INTO reviews (rate, book_id, user_id, opinion) VALUES (:rate, :book_id, :user_id, :opinion)", {'rate':Urating, 'book_id':book_id, 'user_id':user, 'opinion':Utext})
        db.commit()
        return redirect(url_for('book', book_id = book_id))
#        booki = db.execute("SELECT isbn, title, author, year FROM books WHERE id = :id", {'id':book_id})
#        db.commit()
#        book = booki.fetchone()
#        return render_template("book.html", book = book, added = True, bookid = book_id)

@app.route("/api/<int:isbn>")
def api(isbn):
    return "not yet working"

# register
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        # got all data from form
        Uname = request.form.get("username")
        Upass = request.form.get("password")
        Uconf = request.form.get("confirmation")

        # check sql injection danger
        if Uname.find(';') != -1 or Upass.find(';') != -1:
            return render_template("error.html", error_name = "Symbol not allowed")
        if Uname.find(',') != -1 or Upass.find(',') != -1:
            return render_template("error.html", error_name = "Symbol not allowed")
        if Uname.find("'") != -1 or Upass.find("'") != -1:
            return render_template("error.html", error_name = "Symbol not allowed")

        #check password confirmation
        if Upass != Uconf:
            return render_template("error.html", error_name = "Passwords not match")

        # try to find user in base and if it is - send him out
        check1 = db.execute("SELECT id, username, password, num_rev FROM users WHERE username = :username", {'username':Uname})
        db.commit()
        if check1.fetchone() == None:
            PassHash = generate_password_hash(Upass)
            db.execute("INSERT INTO users (username, password, num_rev) VALUES (:username, :password, 0)", {'username':Uname, 'password':PassHash})
            db.commit()
            return render_template("login.html")
        else:
            return render_template("error.html", error_name = "Username is not available. Please choose other")

# login
@app.route("/login", methods = ["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        Uname = request.form.get("username")
        Upass = request.form.get("password")
        check2 = db.execute("SELECT * FROM users WHERE username = :username", {'username':Uname})
        db.commit()
        f2 = check2.fetchone()
        if f2 == None:
            return render_template("error.html", error_name = "No such user. Please register")
        session["user_id"] = f2.id
        return redirect("/")

# logout
@app.route("/exit")
def logout():
    session.clear()
    return redirect("/")
