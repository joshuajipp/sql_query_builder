import mysql.connector
from queryClass import *
from validate import *
from getpass import getpass


def main():
    user = input("Username: ")
    password = getpass("Password: ")
    valid_credentials = True

    while not valid_credentials:
        user = input("Username: ")
        password = getpass("Password: ")
        valid_credentials = validateCredentials(user, password)

    option = input(
        "a.\tInsert\nb.\tDelete\nc.\tUpdate\nd.\tCreate Table\ne.\t Create view\nf.\tAlter\ng.\tQuery\nEnter letter to choose operation: ")


if __name__ == "__main__":
    main()
