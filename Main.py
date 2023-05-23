from flask import Flask,jsonify,request

app=Flask(__name__)
Task=[{
    "id":1,
    "title":"Playing",
    "Description":"FootBall",
    "Done":False
},{
    "id":2,
    "title":"Art",
    "Description":"Painting",
    "Done":False
}]
@app.route('/')
def firstfun():
    return "Moksha"
@app.route('/show-data')
def show_data():
    return Task
@app.route('/add-data',methods=["POST"])
def edit_data():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "message":"Pls provide the data"
        })
    else:
        task={
            "id":Task[-1]["id"]+1,
            "title":request.json["title"],
            "Description":request.json["Description"],
            "Done":False
            


        }
        Task.append(task)
        return jsonify({
            "status":"Scucess",
            "message":"Task Added scuesses"
            

        })
    

app.run(debug=True)