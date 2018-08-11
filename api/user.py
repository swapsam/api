from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('login.html')


@app.route("/login", methods=['POST'])
def login ():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'swap' or request.form['password'] != 'swap':
			error = 'Invalid user.please try again'
		        #return render_template('error.html')
		else:
			print("Login success")
			return render_template('error.html',error="login success")
	return render_template('error.html', errror=error)
																										        

if(__name__ == "__main__"):
	app.run()


