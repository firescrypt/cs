from flask import Flask, render_template      


app = Flask(__name__)

def p(n):
  return "Hello"+n

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template("index.html")
  
@app.route('/api/addbook/<string:name>/')
def addbook(name):
    return "adding book " + p(name)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)