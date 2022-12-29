import mysql.connector

# créer une connection à la base de données
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='a') 

# créer la table fichier inversé
cursor = cnx.cursor()
cursor.execute("CREATE TABLE inverted_file (id INT PRIMARY KEY AUTO_INCREMENT, word VARCHAR(255), document_id INT)")

# créer la table document
cursor.execute("CREATE TABLE document (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), content TEXT)")

# créer la table vocabulaire
cursor.execute("CREATE TABLE vocabulary (id INT PRIMARY KEY AUTO_INCREMENT, word VARCHAR(255))")

# créer la table collection
cursor.execute("CREATE TABLE collection (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255))")

# valider les changements
cnx.commit()
