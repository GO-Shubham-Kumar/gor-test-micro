import pymongo 
import urllib

def register_user(user_id, age, password):
    mongodb = pymongo.MongoClient("mongodb+srv://GO_Shubham_Kumar_Product_Architect:"+urllib.parse.quote_plus("Grey@2022")+"@cluster0.qyhhq.mongodb.net/Users?retryWrites=true&w=majority")
    dblist = mongodb.list_database_names()
    if "Users" in dblist:
        users_db = mongodb["Users"]
        users_collection = users_db["GO_Testing"]

        if users_collection.find_one({"userid":user_id}):
            print("User ID already exists")
            return 409
        else:
            users_collection.insert_one(
                {
                    "userid":user_id,
                    "age":age,
                    "password":password,
                    "timestamp": datetime.now()
                })
            print("User ID inserted")
            return 201

def login(user_id, password):
    mongodb = pymongo.MongoClient("mongodb+srv://GO_Shubham_Kumar_Product_Architect:"+urllib.parse.quote_plus("Grey@2022")+"@cluster0.qyhhq.mongodb.net/Users?retryWrites=true&w=majority")
    dblist = mongodb.list_database_names()
    if "Users" in dblist:
        users_db = mongodb["Users"]
        users_collection = users_db["GO_Testing"]

        if users_collection.find_one({"userid":user_id, "password":password}):
            print("Logged In")
            return 201 
        else:
            print("Invalid Credentials")
            return 404

if __name__ == '__main__':
    # socketio.run(app)
    login("Shubham.Kumar1", "Grey@2022")

    