from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.stylist import Stylist
import repositories.stylist_repository as stylist_repository

stylists_blueprint = Blueprint("stylists", __name__)

#index
@stylists_blueprint.route("/stylists")
def stylists():
    stylists = stylist_repository.select_all()
    return render_template("stylists/index.html", stylists=stylists)

#New
@stylists_blueprint.route("/stylists/new")
def new_stylist():
    return render_template("stylists/new.html")

#create
@stylists_blueprint.route("/stylists", methods=["POST"])
def create_stylist():
    name = request.form["name"]
    new_stylist = Stylist(name)
    stylist_repository.save(new_stylist)
    return redirect("/stylists")

#delete
@stylists_blueprint.route("/stylists/<id>/delete", methods=["POST"])
def delete_stylist(id):
    stylist_repository.delete(id)
    return redirect("/stylists")


#update
def update(stylist):
    sql = "UPDATE stylists SET name = %s WHERE id = %s"
    values = [stylist.name, stylist.phone_number,stylist.id]
    run_sql(sql, values)