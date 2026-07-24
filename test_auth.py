# from app.auth.database import AuthDatabase
# from app.auth.password import PasswordManager

# AuthDatabase.initialize()

# email = "nihar@test.com"

# if not AuthDatabase.user_exists(email):

#     success = AuthDatabase.create_user(
#         full_name="Nihar Suman",
#         email=email,
#         password_hash=PasswordManager.hash_password("Retail@123")
#     )

#     print("User Created:", success)

# else:

#     print("User already exists")

# user = AuthDatabase.get_user_by_email(email)

# print(user["full_name"])
# print(user["email"])
# print(user["created_at"])

# from app.auth.validators import AuthValidator

# tests = [
#     "abc",
#     "password",
#     "Password",
#     "Password1",
#     "Password@1"
# ]

# for pwd in tests:

#     valid, msg = AuthValidator.validate_password(pwd)

#     print(pwd, "->", valid, msg)
from app.auth.database import AuthDatabase
from app.auth.auth_service import AuthService

AuthDatabase.initialize()

success, result = AuthService.register(
    full_name="Retail User",
    email="retail@example.com",
    password="Retail@123"
)

print(success)
print(result)
success, result = AuthService.login(
    "retail@example.com",
    "Retail@123"
)

print(success)

if success:
    print(result["full_name"])
    print(result["email"])
else:
    print(result)