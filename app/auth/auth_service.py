from app.auth.database import AuthDatabase
from app.auth.password import PasswordManager
from app.auth.validators import AuthValidator


class AuthService:

    @staticmethod
    def register(full_name, email, password):

        valid, message = AuthValidator.validate_name(full_name)
        if not valid:
            return False, message

        valid, message = AuthValidator.validate_email(email)
        if not valid:
            return False, message

        valid, message = AuthValidator.validate_password(password)
        if not valid:
            return False, message

        email = email.strip().lower()

        if AuthDatabase.user_exists(email):
            return False, "Email already registered."

        password_hash = PasswordManager.hash_password(password)

        AuthDatabase.create_user(
            full_name=full_name.strip(),
            email=email,
            password_hash=password_hash
        )

        return True, "Registration successful."

    @staticmethod
    def login(email, password):

        email = email.strip().lower()

        user = AuthDatabase.get_user_by_email(email)

        if user is None:
            return False, "User not found."

        if not PasswordManager.verify_password(
            password,
            user["password_hash"]
        ):
            return False, "Incorrect password."

        return True, dict(user)