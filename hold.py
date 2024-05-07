import psycopg2
import datetime
from faker import Faker
from database import connection

fake = Faker()

def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT user_id FROM users;")
        user_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT book_id FROM book;")
        book_ids = [row[0] for row in cur.fetchall()]

        max_holds_per_user = 2
        holds_per_user = {user_id: 0 for user_id in user_ids}

        total_holds = 200

        while total_holds > 0:
            user_id = fake.random_element(user_ids)
            if holds_per_user[user_id] < max_holds_per_user:
                book_id = fake.random_element(book_ids)
                hold_date = fake.date_between_dates(date_start=datetime.date(2020, 1, 1), date_end=datetime.date(2023, 12, 31))
                expiry_date = hold_date + datetime.timedelta(days=7)

                hold_date_str = hold_date.strftime('%Y-%m-%d')
                expiry_date_str = expiry_date.strftime('%Y-%m-%d')

                cur.execute("""
                    INSERT INTO hold (user_id, book_id, hold_date, expiry_date)
                    VALUES (%s, %s, %s, %s);
                """, (user_id, book_id, hold_date_str, expiry_date_str))
                holds_per_user[user_id] += 1
                total_holds -= 1

        conn.commit()
        print("Hold data inserted successfully")

    except Exception as e:
        conn.rollback()
        print("An error occurred while inserting hold data:", e)

    finally:
        cur.close()
        conn.close()

insert_dummy_data()
