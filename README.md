# FlaskMongodbCRUDwithJWT-

MongoDB username : rajii ; password :1234
1.Activate virtualenviroinment:
    on windows --> terminal/command prompt
        1.Set-ExecutionPolicy Unrestricted -Scope Process
        2..\.venv\Scripts\Activate
        3.pip install -r requirements.txt --> To install required packages using
        3.python .\FlaskAuth.py
        4.http://127.0.0.1:5678 - hit the url

point tobe noted:
1.firewall disable if needed
2.Based on the jwt token login credentials(email & password) the mapping with other collection handled
3.Better security → Ensured users can only access their own templates.
4.Multiple templates can create by same person(email)
5.have to handle multiple read and update operation for emailid  

secured:
    for update - email value with be taken from access token itself , so no need of passing as params
    so one user cant accesss others data(update/delete)
    only admin can see every data 

Available Endpoints/routes check on terminal --> flask --app path_CurrentFile() routes

        Endpoint         Methods  Rule
        ---------------  -------  ------------------------------
        register         POST     /register        
        login            POST     /login
        create_template  POST     /template
        get_template     GET      /template/<string:template_id>
        get_templates    GET      /template
        delete_template  DELETE   /template/<string:template_id>
        static           GET      /static/<path:filename>
        update_template  PUT      /template/<string:template_id>

# API endpoints
1.http://127.0.0.1:5678/user_register 
    METHOD :POST 
    HEADER: BEARER TOKEN
    PAYLOAD : {
        "first_name" : "rajii",
        "last_name" : "r",
        "email" : "rajii@gmail.com",
        "password" : "rajii123"
    }
    Response:
    {
        "message": "Registered successfully"
    }

2. http://127.0.0.1:5678/user_login
    METHOD :POST 
    HEADER: BEARER TOKEN 
    PAYLOAD : {
        "email" : "rajii@gmail.com",
        "password" : "rajii123"
    }
    Response: sample resonse
    {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MDcyNTk1MiwianRpIjoiNDUwOWEzNjctMTNmZC00MGY4LTlkNzItZDQ1ZmUxMmNhYTE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImphY2tAZ21haWwuY29tIiwibmJmIjoxNzQwNzI1OTUyLCJjc3JmIjoiODRiNmFiZDEtMzE2Ni00ZTQyLTkwMTAtNzEwOTk5NWU4N2YwIiwiZXhwIjoxNzQwODEyMzUyfQ.XTA7uk9nBO1v0M_5LgG9NCOVEilQ5Mv0ALDAI2eir1M"
    }

3. create_template --> 
    http://127.0.0.1:5678/template
    METHOD :POST 
    HEADER: BEARER TOKEN 
    PAYLOAD : {
    "template_name":"Password Reset",
    "subject":"Reset Your Password",
    "body":"Click here to reset your password."
}
    Response: sample resonse
    {
    "message": "Template created successfully"
    }

3. READ_template -->  http://127.0.0.1:5678/template
    METHOD :GET 
    HEADER: BEARER TOKEN 

    Response: sample resonse
    [
    {
        "body": "Congratulations.",
        "subject": "job offer letter ",
        "template_name": "cheers...",
        "user_email": "rajii@gmail.com"
    }]

3.  UPDATE_template --> http://127.0.0.1:5678/template
    METHOD :PUT 
    HEADER: BEARER TOKEN 
    PAYLOAD : {
    "template_name":"cheers...",
    "subject":"job offer letter ",
    "body":"Congratulations."
    }
    Response: sample resonse
    {
    "message": "Updated Successfully."
    }

3.  DELETE_template -->http://127.0.0.1:5678/template
    METHOD :POST 
    HEADER: BEARER TOKEN 
    PAYLOAD : {
    "template_name":"Password Reset",
    "subject":"Reset Your Password",
    "body":"Click here to reset your password."
    }
    Response: sample resonse
    {
    "message": "Deleted Successfully."
    }