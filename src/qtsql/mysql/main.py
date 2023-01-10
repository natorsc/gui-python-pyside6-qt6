# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QtSql() MySQL."""

from pathlib import Path

from PySide6 import QtSql

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
DATABASE = str(SRC_DIR.joinpath('data', 'database', 'db.sqlite3'))



def read_all(query):
    query.exec('SELECT * FROM user;')
    print(f'Index da coluna: {query.record().indexOf("id")}')
    print(f'Nome da coluna: {query.record().fieldName(0)}')
    rows = 0
    while query.next():
        print(f'{query.value("id")} {query.value("name")}')
        rows += 1
    if rows == 0:
        print('A tabela está vazia.')


if __name__ == "__main__":
    import sys
    
    print(f'Drivers disponíveis: {QtSql.QSqlDatabase.drivers()}')

    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    # db.setHostName('localhost')
    # db.setPort(3306)
    # db.setDatabaseName('log_user')
    # db.setUserName('root')

    # if not db.open():
    #     print(f'Last error {db.lastError().text()}')
    #     print(f'Last error {db.lastError().databaseText()}')
    #     sys.exit(1)

    # query = QtSql.QSqlQuery()
    # query.exec('DROP TABLE user;')
    # query.exec("""CREATE TABLE IF NOT EXISTS user (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    #     name VARCHAR(40) NOT NULL
    #     );""")

    # print(f'Tabelas disponíveis: {db.tables()}')

    # # Create
    # name = 'Renato'
    # query.prepare('INSERT INTO user (name) VALUES (:name)')
    # query.bindValue(':name', name)
    # query.exec()

    # # Read
    # print('\n[!] READ [!]')
    # read_all(query=query)

    # # Update
    # print('\n[!] UPDATE [!]')
    # new_name = 'João'
    # query.prepare('UPDATE user SET name = :name WHERE id = :id;')
    # query.bindValue(':id', 1)
    # query.bindValue(':name', new_name)
    # query.exec()

    # read_all(query=query)

    # # Delete
    # print('\n[!] DELETE [!]')
    # query.prepare('DELETE FROM user WHERE id = :id;')
    # query.bindValue(':id', 1)
    # query.bindValue(':name', new_name)
    # query.exec()

    # read_all(query=query)
