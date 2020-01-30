from databases import  add_user, get_user, get_password
from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session



from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#route for the home page
@app.route('/')
def lo():
    return render_template('login.html')
    

@app.route('/login', methods=['POST'])
def login():

    user =get_user(request.form['username'])
    if (user != None and get_password(request.form['username'])== request.form['password']):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return redirect(url_for("home"))
    else:
    	return redirect(url_for("lo"))
        # return redirect(url_for("signup"))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    # return render_template('signup.html')
    #check that username isn't already taken
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
        return redirect(url_for("lo"))
    else:
        return redirect(url_for("signuP"))

@app.route('/signuP')
def signuP():
    return render_template('signup.html')


@app.route('/logged-in', methods= ['POST', ' GET'])
def logged_in():     
    user = get_user(request.form['username'])

    login_session['password'] = user.password

    return render_template('logged.html')


@app.route('/logout')
def logout():
    return home()
    # return render_template('log_out.html')




@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/nav')
def nav():
    return render_template('navBarTest.html')






    
if __name__ == '__main__':
    app.run(debug=True)