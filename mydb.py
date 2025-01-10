# Install Mysql on your computer
# https://dev.Mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'new_password'
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
