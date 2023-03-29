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
    cursor = test.cursor()
    print('The database is open')

    # Creer table question...
    question_create = 'CREATE TABLE question_table (' \
                      'idquestion INT PRIMARY KEY NOT NULL,' \
                      'question VARCHAR(40),' \
                      'paquet VARCHAR(20),' \
                      'idanswer_fk INT,  ' \
                      'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
    cursor.execute(question_create)

    # Ajouter des valeurs a la table...
    #question_add = ("INSERT INTO question_table VALUES (1.1, 'cuisinier', 'metiers')")
    #cursor.execute(question_add)
    #question_add = ("INSERT INTO question_table VALUES (1.2, 'peintre','metiers' )")
    #cursor.execute(question_add)
    #question_add = ("INSERT INTO question_table VALUES (2.1, 'ecole','ecole')")
    #cursor.execute(question_add)

    # Afficher les valeurs de la table...
    #cursor.execute('SELECT * FROM question_table')
    #cartes = cursor.fetchall()
    #for i in cartes:
    #    print(i)

    # Afficher les valeurs pour un paquet de cartes...
    #cursor.execute('SELECT * FROM question_table WHERE paquet = "metiers"')
    #cartes = cursor.fetchall()
    #for i in cartes:
    #    print(i)

    # Mettre a jour les valeurs de la table...
    #cursor.execute('UPDATE question_table SET question = "classe" WHERE paquet = "ecole";')

    # Supprimer des valeurs de la table...
    #cursor.execute('DELETE FROM question_table WHERE question = "cuisinier";')

    # Supprimer une table...
    #cursor.execute('DROP TABLE question_table;')

    # Creer table reponse...
    answer_create = 'CREATE TABLE answer_table (' \
                    'idanswer INT PRIMARY KEY NOT NULL,' \
                    'answer VARCHAR(40),' \
                    'paquet VARCHAR(20),' \
                    'idquestion_fk = INT,' \
                    'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion));'
    cursor.execute(answer_create)

    # Creer table utilisateur...
    user_create = 'CREATE TABLE user_table (' \
                  'iduser INT PRIMARY KEY NOT NULL,' \
                  'result BOOLEAN );'
    cursor.execute(user_create)

    # Creer table reponse-utilisateur...
    answer_user_create = 'CREATE TABLE answer_user_table (' \
                    'idanswer_user INT PRIMARY KEY NOT NULL, ' \
                    'idanswer_fk INT,' \
                    'iduser_fk INT,' \
                    'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer),' \
                    'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
    cursor.execute(answer_user_create)

    # Sauvegarder le changement.
    test.commit()

    # Fermer la base de donnees
    #test.close()


# Appeler la fonction.
create_sqlite()

# Permettre les requetes...
def open_sqlite():
    #cursor = flashcards_db.cursor()
    pass

# Peciser et executer les requetes...
def query_sqlite():
    pass

# Creer un paquet de cartes
def create_table():
    pass

# Ajouter des donnes/cartes dans un paquet
def add_data():
    pass

# Afficher les cartes d'un paquet
def show_data():
    pass

# Modifier des cartes d'un paquet
def update_data():
    pass

# Supprimer des cartes d'un paquet
def delete_data():
    pass



