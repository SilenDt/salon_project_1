from db.run_sql import run_sql
from models.client import Client

def save(client):
    sql = "INSERT INTO clients (name, phone_number) VALUES (%s, %s) RETURNING id"
    values = [client.name, client.phone_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id

def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for result in results:
        client = Client(result["name"], result["phone_number"],result[id])
        clients.append(client)
    return clients

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)
