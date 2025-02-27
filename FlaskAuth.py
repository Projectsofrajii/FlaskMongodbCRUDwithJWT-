from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
CORS(app)

# MongoDB Connection
MONGO_URI = "mongodb+srv://rajii:1234@cluster0.dtlkb.mongodb.net/?retryWrites=true&w=majority"
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection test before API runs
    db = client["UserMaster"]
    user_collection = db["MasterDataManagement"]
    template_collection = db["TemplateMaster"]
    print("MongoDB Connection Successful!")
except pymongo.errors.ServerSelectionTimeoutError:
    print("MongoDB Connection Failed! Check host and port.")
    exit(1)   
except pymongo.errors.OperationFailure:
    print("MongoDB Authentication Failed! Check username/password.")
    exit(1)  
except Exception as e:
    print(f"MongoDB Error: {str(e)}")
    exit(1)  

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "SECRET_KEY"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=1)
jwt = JWTManager(app)

class UserAuth:
    def __init__(self): self.collection = db["users"]
    def register(self, data):
        if not all(k in data for k in ("first_name", "last_name", "email", "password")):
            return jsonify({"error": "Missing fields"}), 400
        if self.collection.find_one({"email": data["email"]}):
            return jsonify({"error": "User exists"}), 400
        data["password"] = generate_password_hash(data["password"])
        self.collection.insert_one(data)
        return jsonify({"message": "Registered successfully"}), 201
    def login(self, data):
        user = self.collection.find_one({"email": data["email"]})
        if user and check_password_hash(user["password"], data["password"]):
            token = create_access_token(identity=user["email"], expires_delta=datetime.timedelta(days=1))
            return jsonify({"token": token}), 200
        return jsonify({"error": "Invalid credentials"}), 401

class TemplateCRUD:
    def __init__(self): self.collection = db["TemplateMaster"]
    @jwt_required()
    def modify_template(self, template_id=None, method="GET", data=None):
        user = get_jwt_identity()
        if method == "POST":
            data["user_email"] = user
            self.collection.insert_one(data)
            return jsonify({"message": "Template created successfully"}), 201
        elif method == "GET":
            result = list(self.collection.find({"user_email": user}, {"_id": 0})) if not template_id else self.collection.find_one({"_id": template_id, "user_email": user}, {"_id": 0})
            return jsonify(result if not template_id else result or {"error": "Not found"}), (200 if result else 404)
        elif method == "PUT":
            updated = self.collection.update_one({"_id": template_id, "user_email": user}, {"$set": data})
            return jsonify({"message": "Updated" }), (200 if updated.modified_count else 404)
            # return jsonify({"message": "Updated" if updated.modified_count else "Not found"}), (200 if updated.modified_count else 404)
        elif method == "DELETE":
            deleted = self.collection.delete_one({"_id": template_id, "user_email": user})
            return jsonify({"message": "Deleted" }), (200 if deleted.deleted_count else 404)

auth, template = UserAuth(), TemplateCRUD()
app.add_url_rule("/register", "register", lambda: auth.register(request.json), methods=["POST"])
app.add_url_rule("/login", "login", lambda: auth.login(request.json), methods=["POST"])
app.add_url_rule("/template", "create_template", lambda: template.modify_template(method="POST", data=request.json), methods=["POST"])
app.add_url_rule("/template", "get_templates", lambda: template.modify_template(), methods=["GET"])
app.add_url_rule("/template/<string:template_id>", "get_template", lambda template_id: template.modify_template(template_id), methods=["GET"])
app.add_url_rule("/template/<string:template_id>", "update_template", lambda template_id: template.modify_template(template_id, "PUT", request.json), methods=["PUT"])
app.add_url_rule("/template/<string:template_id>", "delete_template", lambda template_id: template.modify_template(template_id, "DELETE"), methods=["DELETE"])

if __name__ == "__main__": app.run(debug=True,port=5678)
