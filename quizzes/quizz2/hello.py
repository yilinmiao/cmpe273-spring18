from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

map = {}
user_id = '1'
@app.route('/users', methods = ['POST'])
def user():
    """modify/update the information for <user_id>"""

    name = request.form["name"]
    map[user_id] = name
    return "POST, id = {}, name = {}\n".format(user_id, name)

@app.route('/users/<user_id>', methods = ['GET','DELETE'])
def getname(user_id):
    #user_id = request.get["user_id"]
    if(request.method == 'GET'):
        return "GET, id = {}, name = {}\n".format(user_id, map[user_id])
    else:
        map[user_id] = ''
        return "No Content"