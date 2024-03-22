"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker  import Faker
# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Add the Relationships Table"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_relationship_query = """
        CREATE TABLE IF NOT EXISTS people
        (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
        );
    """
    cursor.execute(create_relationship_query)
    conn.commit()
    conn.close()

    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Populate the Relationships Table"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    fake = Faker()

    for _ in range(100):
        name = fake.name()
        age = fake.random_int(min=18, max=90)
        email = fake.email()

        insert_person_query = "INSERT INTO people (name, age, email) VALUES (?, ?, ?)"
        cursor.execute(insert_person_query, (name, age, email))
        conn.commit()
    conn.close()
    return 

if __name__ == '__main__':
   main()