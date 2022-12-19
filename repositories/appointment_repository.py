from db.run_sql import run_sql

from models.appointment import Appointment
from models.client import Client
from models.stylist import Stylist

import repositories.appointment_repository as appointment_repository
import repositories.client_repository as client_repository
import repositories.stylist_repository as stylist_repository

def save(appointment):
    sql = "INSERT INTO appointments (client_id, stylist_id, date_time) VALUES (%s, %s, %s) RETURNING id"
    values = [appointment.client.id, appointment.stylist.id, appointment.date_time]
    results = run_sql(sql, values)
    id = results[0]['id']
    appointment.id = id

def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for result in results:
        client = client_repository.select(result["client_id"])
        stylist = stylist_repository.select(result["stylist_id"])
        appointment = Appointment(client, stylist, result["date_time"], result["id"])
        appointments.append(appointment)
    return appointments

def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        client = client_repository.select(result["client_id"])
        stylist = stylist_repository.select(result["stylist_id"])
        appointment = Appointment(client, stylist, result["id"])
    return appointment


def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM appointments WHERE is = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (client_id, appointment_id, time_date) = (%s, %s, %s) WHERE id = %s"
    values = [appointment.client.id, appointment.stylist.id, appointment.time_date, appointment.id]
    run_sql(sql, values)