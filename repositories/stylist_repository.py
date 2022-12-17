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

def delete_all():
    sql = "DELETE FROM stylists"
    run_sql(sql)