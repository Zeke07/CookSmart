from flask import Flask, session, redirect, url_for, render_template, request
import database
app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Change this to a secret key for your app
loggedin = False


def parseDict(dic):

    #print(dict(dic))
    dic_dic = dict(dic)

    #print(dic_dic)

    myFoods = ["myFood1", "myFood2", "myFood3", "myFood4", "myFood5"]
    quality = ["quantity1", "quantity2", "quantity3", "quantity4", "quantity5"]

    new_dict = {}

    for index, key in enumerate(dic_dic):
        if key == "quantity1":
            break
        #print(index)
        new_dict[dic_dic[key]] = dic_dic[quality[index]]
    if "" in new_dict:
        del new_dict[""]
    #print(new_dict)

    query = dict()
    for key in new_dict.keys():
        query[key] = {'$lte': float(new_dict[key]), '$gte': float(new_dict[key])-10.0}
    res = database.query_db(query)
    display_names = list()
    for i in res:
        display_names.append((i['Itemid'], i['Name']))

    print(display_names)
    return display_names

@app.route('/')
def h():
    # get user information from database
    return render_template("hac.html")

@app.route('/home')
def home():
    # get user information from database
    return render_template("hac.html")

@app.route('/food')
def food():
    # get user information from database
    return render_template("food.html")

@app.route('/data')
def data():
    # get user information from database
    return render_template("data.html")

@app.route('/about')
def about():
    # get user information from database
    return render_template("about.html")

@app.route('/profiles')
def profiles():
    if (loggedin):
        return redirect(url_for('user'))
    # get user information from database
    return render_template("profiles.html")

#EDIT

@app.route('/action_page.php')
def button():
    #return parseDict(request.args)
    return render_template('result.html')

    # return "we did it (again lol)"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']
        if username == 'bbadger' and password == 'bucky123':
            # Store the username in the session object
            session['username'] = username
            loggedin = True
            return redirect(url_for('user'))
        else:
            print("Login Failed")
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/user')
def user():
    # get user information from database
    return render_template("user.html")

@app.route('/dashboard')
def dashboard():
    return 'You are logged in!'

# Logout route
@app.route('/logout')
def logout():
    # Remove the username from the session object to log the user out
    loggedin = False
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, threaded=False)  # don't change this line!
