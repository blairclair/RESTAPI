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
