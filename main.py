import mysql.connector
from queryClass import *
from validate import *


def main():
    user = input("Username: ")
    password = input("Password: ")
    valid_credentials = validateCredentials(user, password)

    while not valid_credentials:
        user = input("Username: ")
        password = input("Password: ")
        valid_credentials = validateCredentials(user, password)


if __name__ == "__main__":
    main()
