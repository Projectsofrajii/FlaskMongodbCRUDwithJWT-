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

# Template API 

## Overview
A Flask-based API to create, update, and delete templates.

## Screenshots
### 1️⃣ API Response (Success)
![API Response](images/success.png)