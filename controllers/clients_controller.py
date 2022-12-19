from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.client import Client
import repositories.client_repository as client_repository

clients_blueprint = Blueprint("clients", __name__)

#Index
@clients_blueprint.route("/clients")
def clients():
    clients_list = client_repository.select_all()
    return render_template("clients/index.html", clients=clients_list)

#New
@clients_blueprint.route("/clients/new")
def new_client():
    return render_template("clients/new.html" )

#create
@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    new_client = Client(name, phone_number)
    client_repository.save(new_client)
    return redirect("/clients")

#delete
@clients_blueprint.route("/clients/<id>/delete", methods=["POST"])
def delete_client(id):
    client_repository.delete(id)
    return redirect("/clients")
