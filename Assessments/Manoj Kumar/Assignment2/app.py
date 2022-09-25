from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
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
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
