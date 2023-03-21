# Importer les packages...
import sqlite3

# Execution du code...
def __init__():
    pass

# Creation et connection a la base de donnees...
def create_sqlite():
    #flashcards_db = sqlite3.connect('ifc.db')
    test = sqlite3.connect('sql.db')


    # Permettre les requetes...
    # -> Apres chaque requete ?
    cursor = test.cursor()
    print('The database is open')

    # Preciser et executer les requetes...
    # Exemple :
    query = 'select sqlite_version();'
    cursor.execute(query)

    # Recuperer le resultat...
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Fermer la permission de requetes
    cursor.close()



    # Test creation table :
    # Creer table
    test.execute(''' CREATE TABLE testcartes
         (FIND INT PRIMARY KEY     NOT NULL,
         COLOR           TEXT    NOT NULL,
         VALUE            INT);
         ''')
    # Ajouter valeurs a la table
    test.execute("INSERT INTO testcartes VALUES (1, 'rouge',3 )")
    test.execute("INSERT INTO testcartes VALUES (2, 'rouge',5 )")
    test.execute("INSERT INTO testcartes VALUES (3, 'noir',9 )")
    cursor2 = test.execute("SELECT * from testcartes ")
    print("Cards : \n")
    # Imprimer valeurs lignes
    for row in cursor2:
        print(row)
    cursor2.close()



# Appeler la fonction.
create_sqlite()

# Permettre les requetes...
def open_sqlite():
    #cursor = flashcards_db.cursor()
    pass

# Peciser et executer les requetes...
def query_sqlite():
    pass



