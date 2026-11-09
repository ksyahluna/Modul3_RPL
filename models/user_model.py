import hashlib

from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Mengubah plain text password menjadi hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register_user(self, username, password, role):
      if self.conn:
        cursor = self.conn.cursor()

        # Mengubah password menjadi hash SHA-256
        password_hash = self.hash_password(password)

        try:
            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """

            cursor.execute(query, (username, password_hash, role))
            self.conn.commit()
            return True

        except Exception as e:
            print("Gagal mendaftarkan pengguna:", e)
            self.conn.rollback()
            return False

        finally:
            cursor.close()

      return False

    def autentikasi(self, username, password):
     if self.conn:
        cursor = self.conn.cursor(dictionary=True)
        password_hash = self.hash_password(password)

        query = f"SELECT username, role FROM {self.table_name} WHERE username = %s AND password = %s"

        cursor.execute(query, (username, password_hash))
        user = cursor.fetchone()
        cursor.close()
        return user

     return None