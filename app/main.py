from flask import Flask,request
import random
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
            if random.randint(0,1):
                msg = "Switch Slice 1 to Slice 2"
            else:
                msg = "Switch Slice 2 to Slice 1"
            return msg
        else:
            counter = counter+1
            print(counter)
            return "idle"
@app.route("/upgrade_cache",methods = ['POST', 'GET'])
def upgrade_cache():
    global counter
    if request.method == 'GET':
        if counter%5 == 0:
            counter = counter + 1
            print(counter)
            if random.randint(0,1):
                msg = "Upgrade Cache Slice 1"
            else:
                msg = "Upgrade Cache Slice 2"
            return msg
        else:
            counter = counter+1
            print(counter)
            return "idle"

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=False, port=5000)