import datetime

from faker import Faker
from database import connection

fake = Faker()


def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    try:
        for _ in range(200):
            username = fake.user_name()
            password = fake.password()
            email = fake.email()
            registration_date = fake.date_between_dates(date_start=datetime.date(2020, 1, 1),
                                                        date_end=datetime.date(2023, 12, 31))

            cur.execute("""
                INSERT INTO users (username, password, email, registration_date)
                VALUES (%s, %s, %s, %s);
            """, (username, password, email, registration_date))

        conn.commit()
        print("User data inserted successfully")

    except Exception as e:
        conn.rollback()
        print("An error occurred while inserting user data:", e)

    finally:
        cur.close()
        conn.close()


insert_dummy_data()
