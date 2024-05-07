from faker import Faker
from database import connection

fake = Faker()


def insert_dummy_data():
    conn = connection()
    cur = conn.cursor()

    try:
        for _ in range(20):
            name = f"{fake.company()} Library"
            phone_number = fake.phone_number()
            formatted_phone_number = ''.join(filter(str.isdigit, phone_number))[:20]
            email_address = fake.email()

            cur.execute("""
                INSERT INTO library (name, phone_number, email_address)
                VALUES (%s, %s, %s);
            """, (name, formatted_phone_number, email_address))

        conn.commit()
        print("Data inserted successfully")

    except Exception as e:
        conn.rollback()
        print("An error occurred:", e)

    finally:
        cur.close()
        conn.close()


insert_dummy_data()
