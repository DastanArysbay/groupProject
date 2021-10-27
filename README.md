# Assignment 3

Group project to create a web server in Python using PostgreSQL database.

Team: Aisha Bazylzhanova(SE-2004), Arysbay Dastan(SE-2004) 

## Installation 

To install, you need to download the web_server.py and models.py files from the repository and save them in the same folder. 

## Usage 

In models.py file you need to provide your data
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://YourUsername:YourPassword@localhost/NameOfYourDatabase'
   ```

When you can run web_server.py
   ```python
   C:\<your>\<path>\<to>\<the>\<folder>\web_server.py
   ```
   
In /signup route you provide login and password. If they are correct when the token is stored in the database. If not, an error message shows up.


Correct login and password stored in your database.   


In /protected route we can check, if the token is correct
   
## Examples 

```python
C:\Users\abazy>C:\Users\abazy\source\repos\ProjectsPython\assignment3\web_server.py
 * Serving Flask app 'models' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 930-302-590
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
   
```python
http://127.0.0.1:5000/signup/<login>/<password>
#Well done! Succsessfully added token on database. Token: <tokenvalue>
```
   
```python
http://127.0.0.1:5000/protected?token=<tokenvalue>
#Hello, token which is provided is correct
```
LICENSE ✔

requirements.txt ✔

src/ ✔

test/ ✔
