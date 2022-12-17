from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.stylist import Stylist
import repositories.stylist_repository as stylist_repository

stylists_blueprint = Blueprint("stylists", __name__)

@stylists_blueprint.route("/stylists")
def stylists():
    stylists = stylist_repository.select_all()
    return render_template("stylists/index.html")

def update(stylist):
    sql = "UPDATE stylists SET name = %s WHERE id = %s"
    values = [stylist.name, stylist.phone_number,stylist.id]
    run_sql(sql, values)