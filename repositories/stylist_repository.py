from db.run_sql import run_sql
from models.stylist import Stylist

def save(stylist):
    sql = "INSERT INTO stylists (name) VALUES (%s) RETURNING id"
    values = [stylist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    stylist.id = id