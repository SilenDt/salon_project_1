from db.run_sql import run_sql
from models.client import Client

def save(client):
    sql = "INSERT INTO clients (name, phone_number) VALUES (%s, %s) RETURNING id"
    values = [client.name, client.phone_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id