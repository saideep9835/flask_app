from datetime import timedelta,date
from flask import Flask, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from model import *
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:reddy123@localhost:5432/book'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()
   
    
    
if __name__ == "__main__":
    with app.app_context():
        main()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("SignIn.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/SignIn",methods=["POST"])
def SignIn():
    name = request.form.get("name")
    password = request.form.get("password")
    users = User.query.all()
    a = generate_password_hash(password, method='sha256')
    for user in users:
        if user.name == name :
            return render_template("search.html",name=name)
        else:
            continue
    return render_template("test.html")
@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("name")
    user = Test.query.all()
    
  
    return render_template("book_details.html",user=user, name=name)
@app.route("/review/<string:id>")
def review(id):
    
    usr = Test.query.all()
    for i in usr:
        if id == i.isbn:
            a = i.isbn
            b = i.title
            c = i.author
            d = i.year
    return render_template("review.html", isbn = a, title=b,author=c,year=d)
                

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "GET":
        return "Please submit the form"
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        mobile = request.form.get("mobile")
        dob = request.form.get("dob")
        email = request.form.get("email")
        gender = request.form.get("gender")
        t = datetime.now()
        a = User.query.all()
        for i in a:
            if i.email == email:
                return render_template("exist.html",email=email)
        
        user = User(name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email,gender=gender,timestamp=t)
        
        db.session.add(user)
        db.session.commit()
        
        
        return render_template("admin.html",users = User.query.all())

        #return render_template("submit.html", name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email, gender=gender)
       
        #return render_template("admin.html", name=name, password=generate_password_hash(password, method='sha256'),timestamp=date.today())
@app.route("/review/<string:isbn>/<string:title>",methods=["POST"])
def rating_details(isbn,title):
    print(isbn,title)
    n = request.form.get("nam")
    star = request.form.get("stars")
    name = request.form.get("name")
    response = request.form.get("shelf")
    rev = Review( user=n,isbn=isbn,rating=star,review=name)
    db.session.add(rev)
    db.session.commit()
    if response == "Yes":
        
        sh = Bookshelf(user=n,book=title)
        db.session.add(sh)
        db.session.commit()
    else:
        return render_template("rating_details.html", isbn=isbn,n=n,star=star,name=name)
    return render_template("rating_details.html", isbn=isbn,n=n,star=star,name=name)

@app.route("/shelf")
def shelf():
    b = Bookshelf.query.all()
         
    
    return render_template("shelf.html",c=b )