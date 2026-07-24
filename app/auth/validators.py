import re


class AuthValidator:

    EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    @staticmethod
    def validate_name(name: str):

        name = name.strip()

        if len(name) < 2:
            return False, "Name must contain at least 2 characters."

        return True, ""

    @staticmethod
    def validate_email(email: str):

        email = email.strip().lower()

        if not re.match(AuthValidator.EMAIL_REGEX, email):
            return False, "Please enter a valid email address."

        return True, ""

    @staticmethod
    def validate_password(password: str):

        if len(password) < 8:
            return False, "Password must be at least 8 characters long."

        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."

        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter."

        if not re.search(r"\d", password):
            return False, "Password must contain at least one digit."

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character."

        return True, ""