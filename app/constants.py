import os

USERS_TABLE = "users"
SERVICES_TABLE = "user_services"
USERS_PER_PAGE = 5
ENV = os.environ.get("ENV", "testing")
HOST = "http://localhost:8080" if ENV == "testing" else "http://test.by"