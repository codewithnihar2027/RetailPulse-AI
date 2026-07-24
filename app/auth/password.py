import bcrypt


class PasswordManager:

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a plain-text password using bcrypt.
        """
        password_bytes = password.encode("utf-8")

        hashed = bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt()
        )

        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(
        password: str,
        password_hash: str
    ) -> bool:
        """
        Verify a plain-text password against its bcrypt hash.
        """
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )