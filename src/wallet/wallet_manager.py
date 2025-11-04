
import uuid
import sqlite3

class WalletManager:
    def __init__(self, db_path='wallets.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS wallets (
                wallet_id TEXT PRIMARY KEY,
                balance REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                wallet_id TEXT,
                type TEXT,
                amount REAL,
                FOREIGN KEY (wallet_id) REFERENCES wallets(wallet_id)
            )
        ''')
        self.conn.commit()

    def create_wallet(self):
        wallet_id = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO wallets (wallet_id, balance) VALUES (?, ?)", (wallet_id, 0))
        self.conn.commit()
        return wallet_id

    def get_balance(self, wallet_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM wallets WHERE wallet_id = ?", (wallet_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def deposit(self, wallet_id, amount):
        if amount <= 0:
            return False
        
        cursor = self.conn.cursor()
        cursor.execute("UPDATE wallets SET balance = balance + ? WHERE wallet_id = ?", (amount, wallet_id))
        cursor.execute("INSERT INTO transactions (wallet_id, type, amount) VALUES (?, ?, ?)", (wallet_id, "deposit", amount))
        self.conn.commit()
        return True

    def withdraw(self, wallet_id, amount):
        if amount <= 0:
            return False

        balance = self.get_balance(wallet_id)
        if balance is None or balance < amount:
            return False
        
        cursor = self.conn.cursor()
        cursor.execute("UPDATE wallets SET balance = balance - ? WHERE wallet_id = ?", (amount, wallet_id))
        cursor.execute("INSERT INTO transactions (wallet_id, type, amount) VALUES (?, ?, ?)", (wallet_id, "withdraw", amount))
        self.conn.commit()
        return True

    def get_transactions(self, wallet_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT type, amount FROM transactions WHERE wallet_id = ?", (wallet_id,))
        return [{'type': row[0], 'amount': row[1]} for row in cursor.fetchall()]

    def close_connection(self):
        self.conn.close()
