from flask import Flask, render_template, request

from priv.models import Entry 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

app = Flask(__name__)

engine = create_engine(os.environ["DATABASE_URL"], echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.rollback()

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/get_entries", methods=["GET"])
def get_entries():
	return_dict = dict()
	return_dict["data"] = list()
	for entry in session.query(Entry):
		dict_item = dict()
		dict_item["title"] = entry.title
		dict_item["body"] = entry.body
		return_dict["data"].append(dict_item)

	return return_dict

@app.route("/add_entry", methods=["GET"])
def add_entry():
	title = request.args.get("title")
	body = request.args.get("body")

	entry = Entry()
	entry.create_entry(title, body)
	session.add(entry)
	session.commit()

	return "Entry added!"

if __name__ == '__main__':
	app.run(debug=True)