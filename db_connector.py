# db_connector.py

from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd
import config

# Create a connection string
connection_string = f"{config.DATABASE['drivername']}://{config.DATABASE['username']}:{config.DATABASE['password']}@{config.DATABASE['host']}:{config.DATABASE['port']}/{config.DATABASE['database']}"

# Create a new engine instance
engine = create_engine(connection_string)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Create a MetaData instance
metadata = MetaData()


def get_all_tables_and_relationships():
    """Function to get all tables and relationships from the database"""
    metadata.reflect(bind=engine)
    for table in metadata.tables.values():
        print(f"Table: {table.name}")
        for fk in table.foreign_keys:
            if fk.column.foreign_keys:  # Check if the list is not empty
                print(
                    f"    Foreign key: {fk.column} references {list(fk.column.foreign_keys)[0].column}"
                )
            else:
                print(f"    Foreign key: {fk.column} has no references")


def read_table_data(table_name):
    """Function to read data from a specific table"""
    query = f"SELECT * FROM {table_name}"
    result = pd.read_sql_query(query, con=engine)
    return result
