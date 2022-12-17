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

def select(id):
    client = None
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        client = Client(result["name"], result["phone_number"], result["id"])
    return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM clients WHERE is = %s"
    values = [id]
    run_sql(sql, values)

def update(client):
    sql = "UPDATE clients SET name = %s WHERE id = %s"
    values = [client.name, client.id]
