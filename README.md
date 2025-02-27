# FlaskMongodbCRUDwithJWT-

MongoDB username : rajii ; password :1234
1.Activate virtualenviroinment:
    on windows --> terminal/command prompt
        .... 2 methods can use either one
        1.venv/Scripts/activate
        2.Set-ExecutionPolicy Unrestricted -Scope Process
            .\.venv\Scripts\Activate

2.Install required packages using --> pip install -r requirements.txt

3.firewall disable if needed

4.Available Endpoints/routes check on terminal --> flask --app path_CurrentFile() routes

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

5.Based on the jwt token login credentials(email & password) the mapping with other collection handled
6.Better security → Ensured users can only access their own templates.
7.Multiple templates can create by same person(email)

have to handle multiple read and update operation for emailid  
