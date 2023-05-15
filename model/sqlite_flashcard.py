# Import packages.
import sqlite3


# Create and initialize the questions table...
class QuestionTable:

    # Initialize the class...
    def __init__(self):
        # Create and connect to the database...
        try:
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Allow queries.
            self.cur = self.flashcards_db.cursor()
            print('The database is open')
            self.query = ''
            self.i = int()
        except Exception as e:
            print(e)

    # Create the questions table...
    def create_table(self):
        self.i = 1
        self.query = 'CREATE TABLE question_table (' \
                     'idquestion INT PRIMARY KEY NOT NULL,' \
                     'question VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idanswer_fk INT,  ' \
                     'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        return self.execute(self.query)

    # Add a question's card to the questions table...
    def add_data(self, question, paquet):
        self.query = f'INSERT INTO question_table VALUES ({self.i}, {question}, {paquet}, {self.i});'
        self.i += 1
        return self.execute(self.query)

    # View questions table...
    def show_table(self):
        self.query = 'SELECT * FROM question_table;'
        return self.execute(self.query)

    # View the question's cards in a selected pack...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM question_table WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Change the value of a question's card...
    def update_data(self, question, idquestion):
        self.query = f'UPDATE question_table SET question = {question} WHERE idquestion = {idquestion};'
        return self.execute(self.query)

    # Remove a card from the questions table...
    def delete_data(self, idquestion):
        self.query = f'DELETE FROM question_table WHERE idquestion = {idquestion};'
        return self.execute(self.query)

    # Delete the questions table...
    def delete_table(self):
        self.query = 'DROP TABLE question_table;'
        return self.execute(self.query)

    # Run the query...
    def execute(self, query):

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Create and initialize the answers table...
class AnswerTable:

    # Initialize the class...
    def __init__(self):
        try:
            # Create and connect to the database...
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Allow queries.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = int()
        except Exception as e:
            print(e)

    # Create the answers table...
    def create_table(self):
        self.i = 1
        self.query = 'CREATE TABLE answer_table (' \
                     'idanswer INTEGER PRIMARY KEY NOT NULL,' \
                     'answer VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idquestion_fk  INTEGER NOT NULL ,' \
                     'FOREIGN KEY (idquestion_fk)' \
                     'REFERENCES question_table(idquestion));'
        return self.execute(self.query)

    # Add an answer's card to the answers table...
    def add_data(self, answer, paquet):
        self.query = f'INSERT INTO answer_table VALUES ({self.i}, {answer}, {paquet}, {self.i});'
        self.i += 1
        return self.execute(self.query)

    # View answers table...
    def show_table(self):
        self.query = 'SELECT * FROM answer_table;'
        return self.execute(self.query)

    # View the answer's cards in a selected pack...
    def show_data(self, paquet):
        self.query = f'SELECT * FROM answer_table WHERE paquet = {paquet};'
        return self.execute(self.query)

    # Change the value of an answer's card...
    def update_data(self, answer, idanswer):
        self.query = f'UPDATE answer_table SET answer = {answer} WHERE idanswer = {idanswer};'
        return self.execute(self.query)

    # Remove a card from the answers table...
    def delete_data(self, idanswer):
        self.query = f'DELETE FROM answer_table WHERE idanswer = {idanswer};'
        return self.execute(self.query)

    # Delete the answers table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_table;'
        return self.execute(self.query)

    # Run the query...
    def execute(self, query):

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Create and initialize the users table...
class UserTable:

    # Initialize the class...
    def __init__(self):
        try:
            # Create and connect to the database...
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Allow queries.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = int()
        except Exception as e:
            print(e)

    # Create the users table...
    def create_table(self):
        self.i = 1
        self.query = 'CREATE TABLE user_table (' \
                     'iduser INT PRIMARY KEY NOT NULL,' \
                     'name VARCHAR(40));'
        return self.execute(self.query)

    # Add a user to the users table...
    def add_data(self, name):
        self.query = f'INSERT INTO user_table VALUES ({self.i}, {name});'
        self.i += 1
        return self.execute(self.query)

    # View users table...
    def show_table(self):
        self.query = 'SELECT * FROM user_table;'
        return self.execute(self.query)

    # View a user's name...
    def show_data(self, i):
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        return self.execute(self.query)

    # Change a user's name...
    def update_data(self, name, iduser):
        self.query = f'UPDATE user_table SET name = {name} WHERE iduser = {iduser};'
        return self.execute(self.query)

    # Remove a user from the users table...
    def delete_data(self, iduser):
        self.query = f'DELETE FROM user_table WHERE iduser = {iduser};'
        return self.execute(self.query)

    # Delete the users table...
    def delete_table(self):
        self.query = 'DROP TABLE user_table;'
        return self.execute(self.query)

    # Run the query...
    def execute(self, query):

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Create and initialize the answers-users table...
class AnswerUserTable:

    # Initialize the class...
    def __init__(self):
        try:
            # Create and connect to the database...
            self.flashcards_db = sqlite3.connect('ifc.db')
            # Allow queries.
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
    def add_data(self, idanswer_fk, iduser_fk, result):
        self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {idanswer_fk}, {iduser_fk}, {result});'
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
    def add_data(self, idquestion_fk, iduser_fk):
        self.query = f'INSERT INTO question_user_table VALUES ({self.i}, {idquestion_fk}, {iduser_fk});'
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

# SELECT answer FROM answer_table INNER JOIN answer_user_table aut on answer_table.idanswer = aut.idanswer_fk
# AUTOINCREMENT pour les id ?
