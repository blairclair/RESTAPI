# RESTAPI
A flask-SQL rest API

GOAL
-----
-----
To create a REST api to manage event participants and their information. The classes are named Partygoer and Partygoerinfo to
avoid confusion with Python's Event class.

Requirements
-------------
-------------
The requirements for compiling the api which are also listed in the requirements.txt
- flask
- flask-sqlalchemy
- flask-marshmallow
- marshmallow-sqlalchemy


Getting Started
---------------
---------------
**Using a virtual environment**

- Start your virtual environment by running the command *pipenv shell*
- Then install the required dependencies by running *pip3 install -r requirements.txt*
- Make your way into the python shell by running *python*
- From the python shell run *from app import db* and then *db.create_all()*. This creates your database based on the classes.
You should see a new file named ***db.sqlite*** in your directory. This holds your database information.
- Exit the python shell with *exit()*
- Start the application with *python app.py*

Querying the API
---------------
-------------
Open up a new terminal and paste the following commands changing the values to whatever you wish.
- To add a Partygoer:
```
curl -XPOST -H "Content-type: application/json" -d '{
"password": "MyPassword",
"creationdate": "March 21, 2019"
}' 'http://localhost:5000/partygoer'
```
- To get a list of all the Partygoers:
```
curl -XGET 'http://localhost:5000/partygoer'
```

- To edit a Partygoer's data (replace 1 with the id of the partygoer you wish to edit):
```
curl -XPUT -H "Content-type: application/json" -d '{
"password": "New password",
"creationdate": "March 21, 2019"
}' 'http://localhost:5000/partygoer/1'
```
- To delete a Partygoer and it's info (replace 1 with the id of the partygoer you wish to delete):
```
curl -XDELETE 'http://localhost:5000/partygoer/1'
```
- To add a Partygoerinfo
```
curl -XPOST -H "Content-type: application/json" -d '{
"email": "myemail@gmail.com",
"company": "mycompany",
"position": "myposition"
}' 'http://localhost:5000/partygoerinfo'
```
- To get a list of all Partygoerinfo:
```
curl -XGET 'http://localhost:5000/partygoerinfo'
```
- To edit a Partygoerinfo (replace 1 with the partygoerinfo id you wish to edit):
```
curl -XPUT -H "Content-type: application/json" -d '{
"email": "newEmail",
"company": "newCompany",
"position": "newPosition"
}' 'http://localhost:5000/partygoerinfo/1'
```
- To get a Partygoerinfo from a Partygoer id (replace 1 with the partygoer id you wish to get the info of):
```
curl -XGET 'http://localhost:5000/infofrompartygoer/1'
```
![](setup.gif)
