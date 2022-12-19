from db.run_sql import run_sql
from flask import Blueprint, Flask, redirect, render_template, request

from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository
import repositories.client_repository as client_repository
import repositories.stylist_repository as stylist_repository

appointments_blueprint = Blueprint("appointments", __name__)

#INDEX
@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)