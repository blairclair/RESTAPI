from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#initializes everything needed for the application
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


#defines and initializes the Partygoer class
class   Partygoer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(100))
	creationdate = db.Column(db.String)

	def __init__(self, password, creationdate):
		self.password = password
		self.creationdate = creationdate

class   PartygoerSchema(ma.Schema):
	class Meta:
		fields = ('id', 'password', 'creationdate')

partygoer_schema = PartygoerSchema()
partygoers_schema = PartygoerSchema(many=True)

#defines and initializes the Partygoerinfo class
class   Partygoerinfo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String)
	company = db.Column(db.String)
	position = db.Column(db.String)

	def __init__(self, email, company, position):
		self.email = email
		self.company = company
		self.position = position

class   PartygoerinfoSchema(ma.Schema):
	class Meta:
		fields = ('id', 'email', 'company', 'position')

partygoerinfo_schema = PartygoerinfoSchema()
partygoerinfos_schema = PartygoerinfoSchema(many=True)

#Adds a new Partygoer
@app.route('/partygoer', methods=['POST'])
def add_partygoer():
	password = request.json['password']
	creationdate = request.json['creationdate']

	new_partygoer = Partygoer(password, creationdate)
	
	db.session.add(new_partygoer)
	db.session.commit()	
	return partygoer_schema.jsonify(new_partygoer)

#Gets all the partygoers
@app.route('/partygoer', methods=['GET'])
def get_partygoers():
	all_partygoers = Partygoer.query.all()
	result = partygoers_schema.dump(all_partygoers)
	return jsonify(result)

#Gets a single Partygoer
@app.route('/partygoer/<id>', methods=['GET'])
def get_partygoer(id):
	partygoer = Partygoer.query.get(id)
	return partygoer_schema.jsonify(partygoer)

#Updates a Partygoer
@app.route('/partygoer/<id>', methods=['PUT'])
def update_partygoer(id):
	partygoer = Partygoer.query.get(id)

	password = request.json['password']
	creationdate = request.json['creationdate']

	partygoer.password = password
	partygoer.creationdate = creationdate

	db.session.commit()

	return partygoer_schema.jsonify(partygoer)

#Deletes a Partygoer
@app.route('/partygoer/<id>', methods=['DELETE'])
def delete_partygoer(id):
	partygoer = Partygoer.query.get(id)
	partygoerinfo = Partygoerinfo.query.get(id)
	db.session.delete(partygoer)
	db.session.delete(partygoerinfo)
	db.session.commit()
	return partygoer_schema.jsonify(partygoer)

#Adds a new partygoerinfo
@app.route('/partygoerinfo', methods=['POST'])
def	add_partygoerinfo():
	email = request.json['email']
	company = request.json['company']
	position = request.json['position']
	new_partygoerinfo = Partygoerinfo(email, company, position)
	
	db.session.add(new_partygoerinfo)
	db.session.commit()

	return partygoerinfo_schema.jsonify(new_partygoerinfo)

#Gets all Partygoerinfos
@app.route('/partygoerinfo', methods=['GET'])
def get_partygoerinfos():
	all_partygoerinfos = Partygoerinfo.query.all()
	result = partygoerinfos_schema.dump(all_partygoerinfos)
	return jsonify(result)

#Gets a single Partygoerinfo
@app.route('/partygoerinfo/<id>', methods=['GET'])
def get_partygoerinfo(id):
	partygoerinfo = Partygoerinfo.query.get(id)
	return partygoerinfo_schema.jsonify(partygoerinfo)

#Updates a Partygoerinfo
@app.route('/partygoerinfo/<id>', methods=['PUT'])
def update_partygoerinfo(id):
	partygoerinfo = Partygoerinfo.query.get(id)

	email = request.json['email']
	company = request.json['company']
	position = request.json['position']

	partygoerinfo.email = email
	partygoerinfo.company = company
	partygoerinfo.position = position

	db.session.commit()

	return partygoerinfo_schema.jsonify(partygoerinfo)

#Given the id of a Partygoer gets their info
@app.route('/infofrompartygoer/<id>', methods=['GET'])
def getinfofromparty(id):
	partygoerinfo = Partygoerinfo.query.get(id)
	return partygoerinfo_schema.jsonify(partygoerinfo)

if __name__ == "__main__":
	app.run(debug=True)
