# Importer les packages...
import sqlite3


# Creation de la table des questions.
class QuestionTable:

    # Initialisation de la classe...
    def __init__(self):
        # Creation et connection a la base de donnees.
        try:
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Permettre les requetes.
            self.cur = self.flashcards_db.cursor()
            print('The database is open')
            self.query = ''
            self.i = 1
        except Exception as e:
            print(e)

    # Creer un paquet de cartes...
    def create_table(self):
        self.query = 'CREATE TABLE question_table (' \
                          'idquestion INT PRIMARY KEY NOT NULL,' \
                          'question VARCHAR(40),' \
                          'paquet VARCHAR(50),' \
                          'idanswer_fk INT,  ' \
                          'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        return self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet...
    def add_data(self, question, paquet):
        self.query = f'INSERT INTO question_table VALUES ({self.i}, {question}, {paquet});'
        self.i += 1
        return self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        return self.execute(self.query)

    # Afficher les cartes d'un paquet...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM question_table WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Modifier des cartes d'un paquet...
    def update_data(self, question, paquet):
        self.query = f'UPDATE question_table SET question = {question} WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self, question):
        self.query = f'DELETE FROM question_table WHERE question = {question};'
        return self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE question_table;'
        return self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Creation de la table des reponses.
class AnswerTable:

    # Initialisation de la classe...
    def __init__(self):
        try:
            # Creation et connection a la base de donnees.
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Permettre les requetes.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = 1
        except Exception as e:
            print(e)

    # Creer un paquet de cartes...
    def create_table(self):
        self.query = 'CREATE TABLE answer_table (' \
                     'idanswer INTEGER PRIMARY KEY NOT NULL,' \
                     'answer VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idquestion_fk  INTEGER NOT NULL ,' \
                     'FOREIGN KEY (idquestion_fk)' \
                     'REFERENCES question_table(idquestion));'
        return self.execute(self.query)

    # Ajouter des donnes/cartes dans un paquet...
    def add_data(self, answer, paquet):
        self.query = f'INSERT INTO answer_table VALUES ({self.i}, {answer}, {paquet});'
        self.i += 1
        return self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM answer_table;'
        return self.execute(self.query)

    # Afficher les cartes d'un paquet...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM answer_table WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Modifier des cartes d'un paquet...
    def update_data(self, answer, paquet):
        self.query = f'UPDATE answer_table SET answer = {answer} WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Supprimer des cartes d'un paquet...
    def delete_data(self, answer):
        self.query = f'DELETE FROM answer_table WHERE answer = {answer};'
        return self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_table;'
        return self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Creation de la table des utilisateurs.
class UserTable:

    # Initialisation de la classe...
    def __init__(self):
        try:
            # Creation et connection a la base de donnees.
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Permettre les requetes.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = 1
        except Exception as e:
            print(e)

    # Creer un nouvel utilisateur...
    # AUTOINCREMENT pour id ?
    def create_table(self):
        self.query = 'CREATE TABLE user_table (' \
                      'iduser INT PRIMARY KEY NOT NULL,' \
                      'name VARCHAR(40));'
        return self.execute(self.query)

    # Ajouter un nom pour un utilisateur...
    def add_data(self, name):
        self.query = f'INSERT INTO user_table VALUES ({self.i}, {name});'
        self.i += 1
        return self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM user_table;'
        return self.execute(self.query)

    # Afficher le nom d'un utilisateur...
    def show_data(self, i):
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        return self.execute(self.query)

    # Modifier le nom d'un utilisateur...
    def update_data(self, name, i):
        self.query = f'UPDATE user_table SET name = {name} WHERE iduser = {i};'
        return self.execute(self.query)

    # Supprimer le nom d'un utilisateur...
    def delete_data(self, name):
        self.query = f'DELETE FROM user_table WHERE name = {name};'
        return self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE user_table;'
        return self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Creation de la table des reponses-utilisateurs.
class AnswerUserTable:

    # Initialisation de la classe...
    def __init__(self):
        try:
            # Creation et connection a la base de donnees.
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Permettre les requetes.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = 1
        except Exception as e:
            print(e)

    # Creer la table answer_user_table...
    def create_table(self):
        self.query = 'CREATE TABLE answer_user_table (' \
                        'idanswer_user INT PRIMARY KEY NOT NULL, ' \
                        'idanswer_fk INT,' \
                        'iduser_fk INT,' \
                        'result INT,'\
                        'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer),' \
                        'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        return self.execute(self.query)

    # Ajouter des resultats...
    def add_data(self, result):
        self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {result});'
        self.i += 1
        return self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM answer_user_table;'
        return self.execute(self.query)

    # Afficher le resultat d'un utilisateur a une question...
    def show_data(self, i):
        self.query = f'SELECT * FROM answer_user_table WHERE idanswer_user = {i};'
        return self.execute(self.query)

    # Modifier le resultat d'un utilisateur a une question...
    def update_data(self, result, i):
        self.query = f'UPDATE answer_user_table SET result = {result} WHERE idanswer_user = {i};'
        return self.execute(self.query)

    # Supprimer un resultat...
    def delete_data(self, i):
        self.query = f'DELETE FROM answer_user_table WHERE idanswer_user = {i};'
        return self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_user_table;'
        return self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Creation de la table des questions-utilisateurs.
class QuestionUserTable:

    # Initialisation de la classe...
    def __init__(self):
        try:
            # Creation et connection a la base de donnees.
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Permettre les requetes.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = 1
        except Exception as e:
            print(e)

    # Creer la table question_user_table...
    def create_table(self):
        self.query = 'CREATE TABLE question_user_table (' \
                        'idquestion_user INT PRIMARY KEY NOT NULL, ' \
                        'idquestion_fk INT,' \
                        'iduser_fk INT,' \
                        'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion),' \
                        'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        return self.execute(self.query)

    # Ajouter des liens...
    def add_data(self):
        self.query = f'INSERT INTO question_user_table VALUES ({self.i});'
        self.i += 1
        return self.execute(self.query)

    # Afficher la table...
    def show_table(self):
        self.query = 'SELECT * FROM question_user_table;'
        return self.execute(self.query)

    # Afficher les informations relatives a un element de la table...
    def show_data(self, i):
        self.query = f'SELECT * FROM question_user_table WHERE idquestion_user = {i};'
        return self.execute(self.query)

    # A MODIFIER
    # Modifier le resultat d'un utilisateur a une question...
    def update_data(self, result, i):
        self.query = f'UPDATE question_user_table SET result = {result} WHERE idanswer_user = {i};'
        return self.execute(self.query)

    # Supprimer un lien...
    def delete_data(self, i):
        self.query = f'DELETE FROM question_user_table WHERE idquestion_user = {i};'
        return self.execute(self.query)

    # Supprimer la table...
    def delete_table(self):
        self.query = 'DROP TABLE question_user_table;'
        return self.execute(self.query)

    # Executer les requetes...
    def execute(self, query):

        self.cur.execute(query)

        # Sauvegarder le changement.
        self.flashcards_db.commit()

    # Fermer la base de donnees...
    def close_sqlite(self):
        return self.flashcards_db.close()
