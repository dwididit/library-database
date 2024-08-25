# Library App

A PostgreSQL database project for an e-library platform. It includes SQL scripts for table creation, data insertion, and queries that streamline book access across multiple libraries.

# Entity Relationship Diagram (ERD)
![Logo](https://dwidi.com/wp-content/uploads/2024/08/library-app.png)

# Database Schema Overview

### Table: `sellers`
- **Purpose:** Manages information about multiple libraries within the e-library platform.
- **Description:** This table records essential contact details for each library in the system, such as the library's name, phone number, and email address. Each library houses a diverse collection of books with varying quantities available for borrowing, enabling effective management and access to these resources.
- **Key Columns:**
  - `library_id` (SERIAL, PRIMARY KEY): Unique identifier for each library.
  - `name` (VARCHAR(255), NOT NULL): Library's name.
  - `phone_number` (VARCHAR(20), NOT NULL): Contact phone number for the library.
  - `email_address` (VARCHAR(255), NOT NULL): Contact email address for the library.

### Table: `book`
- **Purpose:** Manages information about books available in the e-library.
- **Description:** Each book entry represents a unique book with attributes such as title, author, and available quantity.
- **Key Columns:**
  - `book_id` (SERIAL, PRIMARY KEY): Unique identifier for each book.
  - `title` (VARCHAR(255), NOT NULL): Title of the book.
  - `author` (VARCHAR(255), NOT NULL): Author of the book.
  - `category` (VARCHAR(255), NOT NULL): Category or genre of the book.
  - `stock` (INTEGER, NOT NULL): Number of copies available for borrowing.
  - `borrowed` (INTEGER, NOT NULL, DEFAULT 0): Number of books that are borrowed by users.
  - `library_id` INTEGER, NOT NULL, FOREIGN KEY): References library.library_id.

### Table: `users`
- **Purpose:** Manages information about registered users of the e-library platform.
- **Description:** This table stores essential details for each registered user.
- **Key Columns:**
  - `user_id` (SERIAL, PRIMARY KEY): Unique identifier for each user.
  - `username` (VARCHAR(255), NOT NULL): User's username.
  - `password` (VARCHAR(255), NOT NULL): Encrypted password to ensure security.
  - `email` (VARCHAR(255), NOT NULL): User's email address, used for communications and notifications.
  - `registration_date` (DATE, NOT NULL): Date when the user registered on the platform.

### Table: `loan`
- **Purpose:** Tracks loan transactions between users and books.
- **Description:** This table logs each loan transaction, including the loan date, due date, and return date.
- **Key Columns:**
  - `loan_id` (SERIAL, PRIMARY KEY): Unique identifier for each loan transaction.
  - `user_id` (INTEGER, NOT NULL, FOREIGN KEY): References user.user_id.
  - `book_id` (INTEGER, NOT NULL, FOREIGN KEY): References book.book_id.
  - `loan_date` (DATE, NOT NULL): Date the book was borrowed.
  - `due_date` (DATE, NOT NULL): Due date for returning the book, typically two weeks from the loan date.
  - `return_date` (DATE): Date the book was actually returned.

  
### Table: `hold`
- **Purpose:** Manages hold requests placed by users for books that are currently unavailable.
- **Description:** This table tracks hold requests on unavailable books. Users can hold up to two books simultaneously.
- **Key Columns:**
  - `hold_id` (SERIAL, PRIMARY KEY): Unique identifier for each hold.
  - `user_id` (INTEGER, NOT NULL, FOREIGN KEY): References user.user_id.
  - `book_id` (INTEGER, NOT NULL, FOREIGN KEY): References book.book_id.
  - `hold_date` hold_date (DATE, NOT NULL): Date the hold was placed.
  - `expiry_date` (DATE, NOT NULL): Expiry date for the hold request, typically one week after the book becomes available.

## Database Table Creation Scripts

### Create `library` Table
```sql
CREATE TABLE library (
    library_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email_address VARCHAR(255) NOT NULL
);
```

### Create `book` Table
```sql
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    stock INTEGER NOT NULL,
    borrowed INTEGER NOT NULL DEFAULT 0,
    library_id INTEGER NOT NULL,
    FOREIGN KEY (library_id) REFERENCES library(library_id)
);
```


### Create `users` Table
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    registration_date DATE NOT NULL
);
```

### Create `loan` Table
```sql
CREATE TABLE loan (
    loan_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);
```

### Create `hold` Table
```sql
CREATE TABLE hold (
    hold_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    hold_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);
```

# Database Setup

This guide will walk you through the process of setting up the Car Marketplace database using PostgreSQL.

## Prerequisites
- PostgreSQL 16 installed on your Windows, Linux, or macOS system.
- pgAdmin, DataGrip or any other PostgreSQL client (optional, for a GUI experience).

## Step-by-Step Setup

### Step 1: Clone or Download This Repository
Clone this repository to your local machine or download the source files directly.

```bash
gh repo clone dwididit/library-databse
cd library-databse
```

### Step 2: Clone or Download This Repository
If you haven't already, install PostgreSQL 16. You can download it from [the official PostgreSQL website](https://www.postgresql.org/). Note down the superuser password you set during installation.

### Step 3: Install pgAdmin (Optional)
For a graphical interface, install pgAdmin from [pgAdmin's website](https://www.pgadmin.org/). This step is optional but recommended for easier database management.

### Step 4: Create a Connection in pgAdmin
Open pgAdmin, and create a new connection to your PostgreSQL server:

Host: localhost (or your server's IP address if remote)
Port: 5432 (default)
Username: postgres (or another superuser)
Password: your_password

### Step 5: Create the Database
Create a new database named car_marketplace using pgAdmin or the command line:
```sql
CREATE DATABASE library_app;
```

### Step 6: Run SQL Scripts to Set Up Tables
From pgAdmin or another SQL client, open the SQL script files included in the cloned/downloaded repository. Execute the scripts with sufficient privileges to create tables and populate them with data. Ensure you are connected to the car_marketplace database before running the scripts.


### Step 7: Explore the Database
Now that your database is set up, you are free to execute SELECT queries and explore the data. Use pgAdmin or connect using your preferred PostgreSQL client.
