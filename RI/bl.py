import mysql.connector

# Demande de termes de recherche à l'utilisateur
terms = input("Entrez les termes de recherche séparés par des espaces : ").split()

# Connexion à la base de données et création d'un curseur
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='a')
cursor = cnx.cursor()

# Construction de la requête de recherche avec des placeholders pour les termes
query = "SELECT * FROM document WHERE"
for term in terms:
    query += " title LIKE '%{}%' OR content LIKE '%{}%' OR".format(term, term)
query = query[:-3]  # Suppression des derniers caractères " OR" de la requête

# Exécution de la requête avec les termes de recherche en utilisant les placeholders
cursor.execute(query, terms)

# Récupération et affichage des résultats de la requête
results = cursor.fetchall()
if not results:  # Si la liste de résultats est vide
    print("Aucun résultat")
else:
    for result in results:
        print(result)

# Validation des modifications et fermeture de la connexion
cnx.commit()
cnx.close()
