import json
import sqlite3

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def connect_sqlite(db_path):
    return sqlite3.connect(db_path)
