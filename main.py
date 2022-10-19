from flask import Flask,request

app = Flask(__name__)
counter = 0
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/update_cdn",methods = ['POST', 'GET'])
def update_cdn():
    global counter
    if request.method == 'GET':
        if counter%5 == 0:
            counter = counter + 1
            print(counter)
            return "slice1,slice2"
        else:
            counter = counter+1
            print(counter)
            return "idle"

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=False, port=5000)