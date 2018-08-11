from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('welcome.html')


@app.route("/login", methods=['POST'])
def login ():
	if request.form['username'] == 'swap' and request.form['password'] == 'swap':
		print("Login successful.Redirecting to products page")
		return redirect(url_for('product_page'))

	else:
		return render_template('error1.html')

@app.route("/products")
def product_page():
	return render_template('products.html')
																										        

if(__name__ == "__main__"):
	app.run()


