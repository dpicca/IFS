# Importer les packages...
import sqlite3


# Creation de la table des questions.
class QuestionTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('sql.db')
        # Permettre les requêtes.
        self.cur = self.flashcards_db.cursor()
        print('The database is open')
        self.query = ''

    # Creer un paquet de cartes
    def create_table(self):
        self.query = 'CREATE TABLE question_table (' \
                          'idquestion INT PRIMARY KEY NOT NULL,' \
                          'question VARCHAR(40),' \
                          'paquet VARCHAR(20),' \
                          'idanswer_fk INT,  ' \
                          'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        self.query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        self.query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        self.execute(self.query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        self.query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        self.query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE question_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()


    # Fermer la base de donnees
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des reponses.
class AnswerTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('sql.db')
        # Permettre les requêtes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        self.query = 'CREATE TABLE answer_table (' \
                        'idanswer INT PRIMARY KEY NOT NULL,' \
                        'answer VARCHAR(40),' \
                        'paquet VARCHAR(20),' \
                        'idquestion_fk = INT,' \
                        'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion));'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        self.query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        self.query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        self.execute(self.query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        self.query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        self.query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE question_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des utilisateurs.
class UserTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('sql.db')
        # Permettre les requêtes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''

    # Peciser et executer les requetes...
    def query_sqlite(self):
        pass

    # Creer un paquet de cartes
    def create_table(self):
        self.query = 'CREATE TABLE user_table (' \
                      'iduser INT PRIMARY KEY NOT NULL,' \
                      'result INT );'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        self.query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        self.query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        self.execute(self.query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        self.query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        self.query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE question_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des reponses-utilisateurs.
class AnswerUserTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('sql.db')
        # Permettre les requêtes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''

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
        self.execute(query)

    # Ajouter des donnes/cartes dans un paquet
    def add_data(self):
        query = 'INSERT INTO question_table VALUES (1, "cuisinier", "metiers");'
        self.execute(query)

    # Afficher la table...
    def show_table(self):
        query = 'SELECT * FROM question_table;'
        self.execute(query)

    # Afficher les cartes d'un paquet
    def show_data(self):
        query = 'SELECT * FROM question_table WHERE paquet = "metiers";'
        self.execute(query)

    # Modifier des cartes d'un paquet
    def update_data(self):
        query = 'UPDATE question_table SET question = "classe" WHERE paquet = "ecole";'
        self.execute(query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        query = 'DELETE FROM question_table WHERE question = "cuisinier";'
        self.execute(query)

    # Supprimer la table...
    def delete_table(self):
        query = 'DROP TABLE question_table;'
        self.execute(query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees
    def close_sqlite(self):
        self.flashcards_db.close()
