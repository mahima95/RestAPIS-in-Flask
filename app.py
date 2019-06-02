from flask import Flask

app = Flask(__name__) #create instance of web app

@app.route("/hello")

def hello():
    return "Hello World!"

if __name__ == '__main__':
     app.run(debug =  True)


