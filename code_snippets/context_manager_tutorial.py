# Link: https://virgool.io/@GreatBahram/once-for-ever-context-manager-qqqbqxgryxk5
#######
# read a file in a pythonic way
with open('names.txt', mode='rt', encoding='utf-8') as myfile:
    for line in myfile:
        print(line)

#######
## Old-fashioned way
try: 
    myfile = open('names.txt', mode='rt', encoding='utf-8')
    for line in myfile:
        print(line)
finally:
    myfile.close()

#######
# How to define a context manager
class File:
    def __init__(self, filename, mode='rt'):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.open_file = open(self.filename, mode=self.mode)
        return self.open_file # as part

    def __exit__(self, *excepts):
        self.open_file.close()

# How to use it?
with File('names.txt', mode='rt') as myfile:
    for line in myfile:
        print(line)

#######
# Compare with and without 'with' statement
## without 'with' statement, how ugly it is, isn't it?
myfile = File('names.txt', mode='rt')
myfile = myfile.__enter__()
try:
    for line in myfile:
        print(line)
finally:
    myfile.__exit__()

## Beyond PEP 8 by using 'with' statement
with File('names.txt', mode='rt') as myfile:
    for line in myfile:
        print(line)

#######
# Compare old and new-fashioned way to work with a databse
# Old-fashioned way
import sqlite3

path = './database.db'

connection = sqlite3.connect(path)
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT unique) ''')
cursor.execute(''' INSERT INTO users(name, email) VALUES('Bahram Aghaei','aghaee.bahram@gmail.com')''')
cursor.execute(''' SELECT * FROM users''')

users = cursor.fetchall()

connection.commit()

# Pythonic way
import sqlite3
from sqlite3 import IntegrityError

path = './database.db'

class DBHelper:
    ''' Simple Database helper which supports context manager as well'''
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exctype, value, traceback):
        if exctype is IntegrityError:
            print('That e-mail is taken, try another one.')
        else:
            self.connection.commit()
            self.connection.close()
        return True

with DBHelper(path) as dbhelper:
    dbhelper.execute(''' CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT unique) ''')
    dbhelper.execute(''' INSERT INTO users(name, email) VALUES('Bahram Aghaei','aghaee.bahram@gmail.com')''')
    dbhelper.execute(''' SELECT * FROM users''')
    users = dbhelper.fetchall()
print(users)

#######
# Timer context manager
import time


class Timer:
    def __init__(self, title):
        self.title = title

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exctype, value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f'{self.title} took {self.elapsed_time}')
        print(f'type is {exctype}')
        print(f'value is {value}')
        print(f'traceback is {traceback}')
        return True

with Timer('Alaki'):
    time.sleep(2)
    raise TypeError('Context manager is a great thing')
    print('After exception')

#######
# Contextlib

## Example1: ope_file context manager by using contextlib decorator
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode='rt'):
    myfile = open(filename, mode=mode)
    yield myfile
    myfile.close()

with open_file('names.txt') as myfile:
    for line in myfile:
        print(line)


## Example2: dbhelper context manager by using contextlib decorator
import sqlite3

from contextlib import contextmanager
from sqlite3 import IntegrityError

path = './database.db'

@contextmanager
def dbhelper(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    try:
        yield cursor
    except IntegrityError as e:
        msg = 'That e-mail is taken, try another one.'
       # raise 
    finally:
        connection.commit()
        connection.close()
        if msg:
            print(msg)

with dbhelper(path) as db:
    db.execute(''' INSERT INTO users(name, email) VALUES('Bahram Aghaei','aghaee.bahram@gmail.com')''')

## Example 3 - How to use contextlib's closing context manager
from contextlib import closing

with closing(open('names.txt', mode='at')) as fp:
    fp.write('contextlib.closing')

fp.write('I cannot write here')

## Example 4: How to use contextlib's suppress context manager
### what is the problem?
import os

from contextlib import suppress

filename = 'alakikhan.png'

try:
    os.remove(filename)
except FileNotFoundError:
    pass

### How to solve it?
import os

from contextlib import suppress

filename = 'alakikhan.png'

with suppress(FileNotFoundError):
    os.remove(filename)
