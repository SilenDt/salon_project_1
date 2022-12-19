from db.run_sql import run_sql
from models.stylist import Stylist

def save(stylist):
    sql = "INSERT INTO stylists (name) VALUES (%s) RETURNING id"
    values = [stylist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    stylist.id = id

def select_all():
    stylists = []
    sql = "SELECT * FROM stylists"
    results = run_sql(sql)
    for result in results:
        stylist = Stylist(result["name"], result["id"])
        stylists.append(stylist)
    return stylists

def select(id):
    stylist = None
    sql = "SELECT * FROM stylists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        stylist = Stylist(result["name"], result["id"])
    return stylist

def delete_all():
    sql = "DELETE FROM stylists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM stylists WHERE is = %s"
    values = [id]
    run_sql(sql, values)

def update(stylist):
    sql = "UPDATE stylists SET name = %s WHERE id = %s"
    values = [stylist.name, stylist.id]
    run_sql(sql, values)