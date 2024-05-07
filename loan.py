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

        max_loans_per_user = 2
        loans_per_user = {user_id: 0 for user_id in user_ids}

        loan_entries = 400

        while loan_entries > 0:
            user_id = fake.random_element(user_ids)
            if loans_per_user[user_id] < max_loans_per_user:
                book_id = fake.random_element(book_ids)
                loan_date = fake.date_between_dates(date_start=datetime.date(2020, 1, 1), date_end=datetime.date(2023, 12, 31))
                due_date = loan_date + datetime.timedelta(days=14)

                # Convert date objects to string
                loan_date_str = loan_date.strftime('%Y-%m-%d')
                due_date_str = due_date.strftime('%Y-%m-%d')

                if fake.boolean(chance_of_getting_true=80):
                    return_date = fake.date_between_dates(date_start=loan_date, date_end=due_date)
                    return_date_str = return_date.strftime('%Y-%m-%d')
                else:
                    return_date_str = None

                cur.execute("""
                    INSERT INTO loan (user_id, book_id, loan_date, due_date, return_date)
                    VALUES (%s, %s, %s, %s, %s);
                """, (user_id, book_id, loan_date_str, due_date_str, return_date_str))
                loans_per_user[user_id] += 1
                loan_entries -= 1

        conn.commit()
        print("Loan data inserted successfully")

    except Exception as e:
        conn.rollback()
        print("An error occurred while inserting loan data:", e)

    finally:
        cur.close()
        conn.close()

insert_dummy_data()
