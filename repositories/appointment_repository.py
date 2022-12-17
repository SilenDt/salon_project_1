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
