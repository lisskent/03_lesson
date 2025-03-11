from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO users(user_id, user_email, subject_id) VALUES(:user_id, :user_email, :subject_id)")
    connection.execute(sql, {"user_id": 1337, "user_email": "mail@mail.com", "subject_id": 3})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET user_email = :email WHERE user_id = :id")
    connection.execute(sql, {"email": 'mailmail2@mail.ru', "id": 1337})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_id = :id")
    connection.execute(sql, {"id": 1337})

    transaction.commit()
    connection.close()
