from flask import Blueprint, Flask, redirect, render_template, request

from models.client import Client
import repositories.client_repository as client_repository

clients_blueprint = Blueprint("clients", __name__)

#Index
@clients_blueprint.route("/clients")
def stylists():
    clients = client_repository.select_all()
    return render_template("clients/index.html")


#New
@clients_blueprint.route("/clients/new")
def new_client():
    return render_template("humans/new.html")