# main.py

import db_connector


def main():
    # Get all tables and relationships from the database
    db_connector.get_all_tables_and_relationships()


if __name__ == "__main__":
    main()
