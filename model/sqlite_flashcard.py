# Importer les packages...
import sqlite3


# Creation de la table des questions.
class QuestionTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('ifc.db')
        # Permettre les requetes.
        self.cur = self.flashcards_db.cursor()
        print('The database is open')
        self.query = ''
        self.i = 1

    # Creer un paquet de cartes...
    def create_table(self):
        self.query = 'CREATE TABLE question_table (' \
                          'idquestion INT PRIMARY KEY NOT NULL,' \
                          'question VARCHAR(40),' \
                          'paquet VARCHAR(20),' \
                          'idanswer_fk INT,  ' \
                          'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet...
    def add_data(self, question, paquet):
        self.query = f'INSERT INTO question_table VALUES ({self.i}, {question}, {paquet});'
        self.i += 1
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM question_table WHERE paquet = {paquet};'
        self.execute(self.query)

    # Modifier des cartes d'un paquet...
    def update_data(self, question, paquet):
        self.query = f'UPDATE question_table SET question = {question} WHERE paquet = {paquet};'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self, question):
        self.query = f'DELETE FROM question_table WHERE question = {question};'
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

    # Fermer la base de donnees...
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des reponses.
class AnswerTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('ifc.db')
        # Permettre les requetes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''
        self.i = 1

    # Creer un paquet de cartes...
    def create_table(self):
        self.query = 'CREATE TABLE answer_table (' \
                        'idanswer INT PRIMARY KEY NOT NULL,' \
                        'answer VARCHAR(40),' \
                        'paquet VARCHAR(20),' \
                        'idquestion_fk = INT,' \
                        'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion));'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet...
    def add_data(self, answer, paquet):
        self.query = f'INSERT INTO answer_table VALUES ({self.i}, {answer}, {paquet});'
        self.i += 1
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM answer_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM answer_table WHERE paquet = {paquet};'
        self.execute(self.query)

    # Modifier des cartes d'un paquet...
    def update_data(self, answer, paquet):
        self.query = f'UPDATE answer_table SET answer = {answer} WHERE paquet = {paquet};'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self, answer):
        self.query = f'DELETE FROM answer_table WHERE answer = {answer};'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des utilisateurs.
class UserTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('ifc.db')
        # Permettre les requetes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''
        self.i = 1

    # Creer un nouvel utilisateur...
    def create_table(self):
        self.query = 'CREATE TABLE user_table (' \
                      'iduser INT PRIMARY KEY NOT NULL AUTOINCREMENT,' \
                      'name VARCHAR(40));'
        self.execute(self.query)

    # Ajouter un nom pour un utilisateur...
    def add_data(self, name):
        self.query = f'INSERT INTO user_table VALUES ({self.i}, {name});'
        self.i += 1
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM user_table;'
        self.execute(self.query)

    # Afficher les noms des utilisateurs...
    def show_data(self, i):
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        self.execute(self.query)

    # Modifier le nom d'un utilisateur...
    def update_data(self, name, i):
        self.query = f'UPDATE user_table SET name = {name} WHERE iduser = {i};'
        self.execute(self.query)

    # Supprimer le nom d'un utilisateur...
    def delete_data(self, name):
        self.query = f'DELETE FROM user_table WHERE name = {name};'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE user_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        self.flashcards_db.close()


# Creation de la table des reponses-utilisateurs.
class AnswerUserTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        self.flashcards_db = sqlite3.connect('ifc.db')
        # Permettre les requetes.
        self.cur = self.flashcards_db.cursor()
        self.query = ''
        self.i = 1

    # Creer la table answer_user_table...
    def create_table(self):
        self.query = 'CREATE TABLE answer_user_table (' \
                        'idanswer_user INT PRIMARY KEY NOT NULL, ' \
                        'idanswer_fk INT,' \
                        'iduser_fk INT,' \
                        'result INT,'\
                        'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer),' \
                        'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet...
    def add_data(self, ):
        self.query = 'INSERT INTO answer_user_table VALUES (1, "cuisinier", "metiers");'
        self.i += 1
        self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM answer_user_table;'
        self.execute(self.query)

    # Afficher les cartes d'un paquet...
    def show_data(self):
        self.query = 'SELECT * FROM answer_user_table WHERE paquet = "metiers";'
        self.execute(self.query)

    # Modifier des cartes d'un paquet...
    def update_data(self):
        self.query = 'UPDATE answer_user_table SET question = "classe" WHERE paquet = "ecole";'
        self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self):
        self.query = 'DELETE FROM answer_user_table WHERE question = "cuisinier";'
        self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_user_table;'
        self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        self.flashcards_db.close()
