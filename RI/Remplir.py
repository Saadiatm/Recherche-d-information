import mysql.connector
from faker import Faker

# Connect to the database
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='a')


# Create a cursor object
cursor = cnx.cursor()

# Create an instance of Faker
fake = Faker()

# gen_text fonction
def gen_text():
    text = ''
    for _ in range(0, 20):
        text = text + fake.sentence()
    return text

# Insert data into the "document" table
for _ in range (0, 20) :
    title = fake.sentence()
    content = gen_text()
    word = fake.word()
    name = fake.word()
    document_id = fake.random_int(1, 10)
    cursor.execute("INSERT INTO inverted_file (word, document_id) VALUES (%s, %s)", (word, document_id))
    cursor.execute("INSERT INTO document (title, content) VALUES (%s, %s)", (title, content))
    cursor.execute("INSERT INTO vocabulary (word) VALUES (%s)", (word,))
    cursor.execute("INSERT INTO collection (name) VALUES (%s)", (name,))

cnx.commit()
