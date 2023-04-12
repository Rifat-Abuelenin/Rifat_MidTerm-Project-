from flask import Flask //we have flask import from flask class 
app = Flask(__name__)//here we assigned varaible to the flask 


@app.route("/") //this is called the root for the page like main page 
@app.route("/home")//to navigate between the web pages 
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")//to navigate between the web pages 
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True) //here we inseted going and refresh the web server every time we can just refresh the page and will update the form  
