from flask import Flask,jsonify,request

app=Flask(__name__)

Contact_list=[{
    "Contact":"4588777567",
    "Name":"Raju",
    "Done":False,
    "id":1,
},{
    "Contact":"9876543222",
    "Name":"Rahul",
    "Done":False,
    "id":1
}]

@app.route('/show-data')
def show_data():
    return Contact_list
@app.route('/add-data',methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "message":"Pls provide the data"
        })
    else:
        Contact={
            "Contact":request.json["Contact"],
            "Name":request.json["Name"],
            "Done":False,
            "id":Contact_list[-1]["id"]+1
            


        }
        Contact_list.append(Contact)
        return jsonify({
            "status":"Scucess",
            "message":"Contact Added scuesses"
            

        })
    

app.run(debug="True")