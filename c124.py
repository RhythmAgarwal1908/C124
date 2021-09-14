from re import U
from flask import Flask,jsonify,request
from werkzeug.exceptions import MethodNotAllowed
app = Flask(__name__)
tasks=[{'id':1,'title':U'Buy Groceries','Description':U'Milk,Chesse,Pizza,Fruit','Done':False},
       {'id':2,'title':U'Learn Python','Description':U'Need to find a Good Python Tutorial on Youtube','Done':False}
]
@app.route('/add-data',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({"Status":"error","Message":"Please Provide Data"},400)
    task={'id':tasks[-1]["id"]+1,'Title':request.json['title'],'Description':request.json.get("Description",""),'Done':False}
    tasks.append(task)
    return jsonify({"Status":"Success","Message":"Task Added Successful"})
@app.route('/get-data')
def get_task():
    return jsonify({"data":tasks})
if __name__ == "__main__":
    app.run(debug=True)