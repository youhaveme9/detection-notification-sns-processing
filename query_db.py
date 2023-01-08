import sqlite3
from sqlite3 import Error
import os

print(os.path.exists("/home/youhaveme/yoloCar/sns-processing/cars_database.db"))

database = r"/home/youhaveme/yoloCar/sns-processing/cars_database.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()
    return rows


