#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Terminaldan 4 arqumenti alırıq
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    # Bazaya qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Cursor yaradırıq
    cursor = db.cursor()

    # .format() istifadə edərək sorğunu qururuq
    # BINARY burada hərfin böyük-kiçikliyinə (case-sensitive) diqqət edir
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_searched)
    
    # Sorğunu icra edirik
    cursor.execute(query)

    # Nəticələri götürürük
    rows = cursor.fetchall()

    # Çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
