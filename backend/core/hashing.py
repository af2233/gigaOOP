import bcrypt
import hashlib
import uuid


class Hash:
    @staticmethod
    def generate_uuid():
        return uuid.uuid4()

    @staticmethod
    def hash_login(login):
        return hashlib.sha256(login.encode()).hexdigest()

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    @staticmethod
    def hash_email(email):
        return hashlib.md5(email.encode()).hexdigest()

    @staticmethod
    def check_password(hashed_password, password):
        return bcrypt.checkpw(hashed_password.encode(), password)
