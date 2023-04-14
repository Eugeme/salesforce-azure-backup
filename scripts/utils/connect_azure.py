"""pyodbc is an open source Python module that makes accessing ODBC databases simple.
    https://github.com/mkleehammer/pyodbc/wiki"""

import pyodbc
from dotenv import dotenv_values


def connect():
    """Pass an ODBC connection string to the pyodbc connect() function which will return a Connection.
     Once you have a connection you can ask it for a Cursor."""

    config = dotenv_values(".env")  # take environment variables from .env file

    server = config['SERVER']
    database = config['DATABASE']
    username = config['AZURE_USERNAME']
    password = config['AZURE_PASSWORD']

    cnxn = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                          server=server,
                          database=database,
                          uid=username,
                          pwd=password)
    return cnxn.cursor()
