# Importer les packages...
import sqlite3


# Creation de la table des questions.
class QuestionTable:

    # Execution du code...
    def __init__(self):
        pass

    # Creation et connection a la base de donnees...
    def create_sqlite(self):
        #flashcards_db = sqlite3.connect('ifc.db')
        test = sqlite3.connect('sql.db')


        # Permettre les requetes...
        cursor = test.cursor()
        print('The database is open')

        # Sauvegarder le changement.
        test.commit()

        # Fermer la base de donnees
        #test.close()

    # Permettre les requetes...
    def open_sqlite(self):
        #cursor = flashcards_db.cursor()
        pass

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        query = 'CREATE TABLE question_table (' \
                          'idquestion INT PRIMARY KEY NOT NULL,' \
                          'question VARCHAR(40),' \
                          'paquet VARCHAR(20),' \
                          'idanswer_fk INT,  ' \
                          'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        execute(query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        execute(query)

    # Afficher la table...
    def show_table(self):
        query = 'SELECT * FROM question_table;'
        execute(query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        execute(query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        execute(query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        execute(query)

    # Supprimer la table...
    def delete_table(self):
        query = 'DROP TABLE question_table;'
        execute(query)

    def execute(query):

        conn = sqlite3.connect('sql.db')

        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)


# Creation de la table des reponses.
class AnswerTable:

    # Execution du code...
    def __init__(self):
        pass

    # Creation et connection a la base de donnees...
    def create_sqlite(self):
        #flashcards_db = sqlite3.connect('ifc.db')
        test = sqlite3.connect('sql.db')


        # Permettre les requetes...
        cursor = test.cursor()
        print('The database is open')

        # Sauvegarder le changement.
        test.commit()

        # Fermer la base de donnees
        #test.close()

    # Permettre les requetes...
    def open_sqlite(self):
        #cursor = flashcards_db.cursor()
        pass

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        query = 'CREATE TABLE answer_table (' \
                        'idanswer INT PRIMARY KEY NOT NULL,' \
                        'answer VARCHAR(40),' \
                        'paquet VARCHAR(20),' \
                        'idquestion_fk = INT,' \
                        'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion));'
        execute(query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        execute(query)

    # Afficher la table...
    def show_table(self):
        query = 'SELECT * FROM question_table;'
        execute(query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        execute(query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        execute(query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        execute(query)

    # Supprimer la table...
    def delete_table(self):
        query = 'DROP TABLE question_table;'
        execute(query)

    def execute(query):

        conn = sqlite3.connect('sql.db')

        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)


# Creation de la table des utilisateurs.
class UserTable:

    # Execution du code...
    def __init__(self):
        pass

    # Creation et connection a la base de donnees...
    def create_sqlite(self):
        #flashcards_db = sqlite3.connect('ifc.db')
        test = sqlite3.connect('sql.db')


        # Permettre les requetes...
        cursor = test.cursor()
        print('The database is open')

        # Sauvegarder le changement.
        test.commit()

        # Fermer la base de donnees
        #test.close()

    # Permettre les requetes...
    def open_sqlite(self):
        #cursor = flashcards_db.cursor()
        pass

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        query = 'CREATE TABLE user_table (' \
                      'iduser INT PRIMARY KEY NOT NULL,' \
                      'result INT );'
        execute(query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        execute(query)

    # Afficher la table...
    def show_table(self):
        query = 'SELECT * FROM question_table;'
        execute(query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        execute(query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        execute(query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        execute(query)

    # Supprimer la table...
    def delete_table(self):
        query = 'DROP TABLE question_table;'
        execute(query)

    def execute(query):

        conn = sqlite3.connect('sql.db')

        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)


# Creation de la table des reponses-utilisateurs.
class AnswerUserTable:

    # Execution du code...
    def __init__(self):
        pass

    # Creation et connection a la base de donnees...
    def create_sqlite(self):
        #flashcards_db = sqlite3.connect('ifc.db')
        test = sqlite3.connect('sql.db')


        # Permettre les requetes...
        cursor = test.cursor()
        print('The database is open')

        # Sauvegarder le changement.
        test.commit()

        # Fermer la base de donnees
        #test.close()

    # Permettre les requetes...
    def open_sqlite(self):
        #cursor = flashcards_db.cursor()
        pass

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        query = 'CREATE TABLE answer_user_table (' \
                        'idanswer_user INT PRIMARY KEY NOT NULL, ' \
                        'idanswer_fk INT,' \
                        'iduser_fk INT,' \
                        'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer),' \
                        'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        execute(query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        execute(query)

    # Afficher la table...
    def show_table(self):
        query = 'SELECT * FROM question_table;'
        execute(query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        execute(query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        execute(query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        execute(query)

    # Supprimer la table...
    def delete_table(self):
        query = 'DROP TABLE question_table;'
        execute(query)

    def execute(query):

        conn = sqlite3.connect('sql.db')

        cur = conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)
