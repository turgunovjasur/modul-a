import sqlite3
from sqlite3 import Error


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    table_query = """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        username TEXT NOT NULL UNIQUE,
                        balance REAL NOT NULL
                        );"""
    try:
        conn.execute(table_query)
    except Error as e:
        print(e)


def add_user(conn, user):
    query = """INSERT INTO users(username, balance) VALUES (?, ?)"""
    conn.execute(query, user)
    conn.commit()


def update_balance(conn, user_id, amount):
    query = """UPDATE users SET balance = balance + ? WHERE id = ?"""
    conn.execute(query, (amount, user_id))
    conn.commit()


def transfer(conn, sender_id, receiver_id, amount):
    if sender_id == receiver_id:
        print("O'zingizga pul o'tkazishingiz mumkin emas!")
        return

    query = """SELECT balance FROM users WHERE id = ?"""
    sender_balance = conn.execute(query, (sender_id,)).fetchone()[0]

    if sender_balance < amount:
        print("Hisobingizda mablag' yetarli emas!")
        return

    update_balance(conn, sender_id, -amount)
    update_balance(conn, receiver_id, amount)
    print("O'tkazma muvaffiqiyatli!")


def display_users(conn):
    query = """SELECT * FROM users"""
    users = conn.execute(query).fetchall()
    for user in users:
        print(user)


def main():
    databace = "payment_system.db"
    conn = create_connection(databace)
    create_table(conn)

    while True:
        print("\nMini Payment System Menu")
        print("1. Foydalanuvchini qo'shish")
        print("2. Hisobni to'ldirish")
        print("3. Hisobdan pul yechish")
        print("4. Pul o'tkazish")
        print("5. Foydalanuvchilarni ko'rsatish")
        print("6. Dasturdan chiqish")

        choice = int(input("Tanlovni kiriting: "))

        if choice == 1:
            username = input("Foydalanuvchi nomini kiriting: ")
            balance = float(input("Boshlang'ich balansni kiriting: "))
            user = (username, balance)
            add_user(conn, user)
        elif choice == 2:
            user_id = int(input("Foydalanuvchi ID raqamini kiriting: "))
            amount = float(input("Depozit miqdorini kiriting: "))
            update_balance(conn, user_id, amount)
        elif choice == 3:
            user_id = int(input("Foydalanuvchi ID raqamini kiriting: "))
            amount = float(input("Yechib olish miqdorini kiriting: "))
            update_balance(conn, user_id, -amount)
        elif choice == 4:
            sender_id = int(input("Jo'natuvchi foydalanuvchi ID raqamini kiriting: "))
            receiver_id = int(input("Qabul qiluvchi foydalanuvchi ID raqamini kiriting: "))
            amount = float(input("O'tkaziladigan summani kiriting: "))
            transfer(conn, sender_id, receiver_id, amount)
        elif choice == 5:
            display_users(conn)
        elif choice == 6:
            break
        else:
            print("Noto'g'ri kiritish. Iltimos, qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()
