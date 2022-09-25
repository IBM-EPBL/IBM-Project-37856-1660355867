from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT']) 
def home(): 
    return render_template('home.html')

@app.route("/about") 
def about(): 
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup") 
def signup(): 
    return render_template('signin.html')


app.run(debug = True) 