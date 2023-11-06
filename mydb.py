from mysql import connector;

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
)

# prepare a curser object
cursorObject = dataBase.cursor()

# createa database
cursorObject.execute('CREATE DATABASE MUNI');

print("all done");