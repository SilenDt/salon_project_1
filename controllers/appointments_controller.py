from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository
import repositories.client_repository as client_repository
import repositories.stylist_repository as stylist_repository

appointments_blueprint = Blueprint("appointments", __name__)

# INDEX
@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)

# NEW
@appointments_blueprint.route("/appointments/new")
def new_appointment():
    clients = client_repository.select_all()
    stylists = stylist_repository.select_all()
    return render_template("appointments/new.html", clients=clients, stylists=stylists)

# CREATE
@appointments_blueprint.route("/appointments", methods=["POST"])
def create_appointment():
    client_id = request.form["client_id"]
    stylist_id = request.form["stylist_id"]
    date_time = request.form["date_time"]
    client = client_repository.select(client_id)
    stylist = stylist_repository.select(stylist_id)
    date_time = appointment_repository.select("date_time")
    new_appointment = Appointment(client, stylist, date_time)
    appointment_repository.save(new_appointment)
    return redirect("/appointments")
