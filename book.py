from faker import Faker
from database import connection

fake = Faker()

def insert_dummy_books():
    conn = connection()
    cur = conn.cursor()

    try:
        total_libraries = 20
        books_per_library = 30

        for library_id in range(1, total_libraries + 1):
            for _ in range(books_per_library):
                title = fake.sentence(nb_words=5)
                author = fake.name()
                category = fake.word(ext_word_list=["Science Fiction", "Literature", "History", "Biography", "Mystery", "Thriller"])
                stock = fake.random_int(min=1, max=20)
                borrowed = fake.random_int(min=0, max=stock)

                cur.execute("""
                    INSERT INTO book (title, author, category, stock, borrowed, library_id)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (title, author, category, stock, borrowed, library_id))

        conn.commit()
        print("Book data inserted successfully")

    except Exception as e:
        conn.rollback()
        print("An error occurred while inserting book data:", e)

    finally:
        cur.close()
        conn.close()

insert_dummy_books()
