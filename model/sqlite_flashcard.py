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
        """

        Returns:

        """
        self.i = 1
        self.query = 'CREATE TABLE question_table (' \
                     'idquestion INT PRIMARY KEY NOT NULL,' \
                     'question VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idanswer_fk INT,  ' \
                     'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        return self.execute_query(self.query)

    # Add a question's card to the questions table...
    def add_data(self, question, paquet):
        """
        Add a question's card to the questions table...
        Args:
            question:
            paquet:

        Returns:

        """
        if self.i == int():
            self.query = f'INSERT INTO question_table VALUES ({self.i}, "{question}", "{paquet}", {self.i});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO question_table VALUES ({self.i}, "{question}", "{paquet}", {self.i});'
            self.i += 1

        return self.execute_query(self.query)

    # View questions table...
    def show_table(self):
        """
        View questions table...
        Returns:

        """
        self.query = 'SELECT * FROM question_table;'
        return self.cur.execute(self.query)

    # View the question's cards in a selected pack...
    def show_data(self, paquet):
        """

        Args:
            paquet:

        Returns:

        """
        self.query = f'SELECT * FROM question_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # View a user's saved packages...
    def show_pack(self, iduser_fk):
        """

        :param iduser_fk:
        :return:
        """
        self.query = f'SELECT paquet FROM question_user_table INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion WHERE iduser_fk = {iduser_fk};'
        return self.cur.execute(self.query)

    # View a user's questions for a selected pack...
    def show_questions(self, iduser_fk, paquet):
        """

        :param iduser_fk:
        :param paquet:
        :return:
        """
        self.query = f'SELECT iduser_fk, question FROM question_user_table INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion WHERE iduser_fk = {iduser_fk} AND paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # Change the value of a question's card...
    def update_data(self, question, idquestion):
        """
        Change the value of a question's card...
        Args:
            question:
            idquestion:

        Returns:

        """
        self.query = f'UPDATE question_table SET question = "{question}" WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    # Remove a card from the questions table...
    def delete_data(self, idquestion):
        """
        Remove a card from the questions table...
        Args:
            idquestion:

        Returns:

        """
        self.query = f'DELETE FROM question_table WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    # Delete the questions table...
    def delete_table(self):
        """
        Delete the questions table...
        Returns:

        """
        self.query = 'DROP TABLE question_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):
        """
        Run the query...
        Args:
            query:

        Returns:

        """

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
        """
        Create the answers table...

        Returns:

        """
        self.i = 1
        self.query = 'CREATE TABLE answer_table (' \
                     'idanswer INTEGER PRIMARY KEY NOT NULL,' \
                     'answer VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idquestion_fk  INTEGER NOT NULL ,' \
                     'FOREIGN KEY (idquestion_fk)' \
                     'REFERENCES question_table(idquestion));'
        return self.execute_query(self.query)

    # Add an answer's card to the answers table...
    def add_data(self, answer, paquet):
        """
        Add an answer's card to the answers table...
        Args:
            answer:
            paquet:

        Returns:

        """
        if self.i == int():
            self.query = f'INSERT INTO answer_table VALUES ({self.i}, "{answer}", "{paquet}", {self.i});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO answer_table VALUES ({self.i}, "{answer}", "{paquet}", {self.i});'
            self.i += 1

        return self.execute_query(self.query)

    # View answers table...
    def show_table(self):
        """
        View answers table...
        Returns:

        """
        self.query = 'SELECT * FROM answer_table;'
        return self.cur.execute(self.query)

    # View the answer's cards in a selected pack...
    def show_data(self, paquet):
        """
        View the answer's cards in a selected pack...
        Args:
            paquet:

        Returns:

        """
        self.query = f'SELECT * FROM answer_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # View the answer's cards of a selected question...
    def show_answer(self, idquestion):
        """

        :param idquestion:
        :return:
        """
        self.query = f'SELECT answer FROM answer_table INNER JOIN question_table aut on answer_table.idanswer = aut.idquestion WHERE idquestion = {idquestion};'
        return self.cur.execute(self.query)

    # Change the value of an answer's card...
    def update_data(self, answer, idanswer):
        """
        Change the value of an answer's card...
        Args:
            answer:
            idanswer:

        Returns:

        """
        self.query = f'UPDATE answer_table SET answer = "{answer}" WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    # Remove a card from the answers table...
    def delete_data(self, idanswer):
        """
        Remove a card from the answers table...
        Args:
            idanswer:

        Returns:

        """
        self.query = f'DELETE FROM answer_table WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    # Delete the answers table...
    def delete_table(self):
        self.query = 'DROP TABLE answer_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):

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
        """

        Returns:

        """
        self.i = 1
        self.query = 'CREATE TABLE user_table (' \
                     'iduser INT PRIMARY KEY NOT NULL,' \
                     'name VARCHAR(40));'
        return self.execute_query(self.query)

    # Add a user to the users table...
    def add_data(self, name):
        """
        Add a user to the users table...
        Args:
            name:

        Returns:

        """
        if self.i == int():
            self.query = f'INSERT INTO user_table VALUES ({self.i}, "{name}");'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO user_table VALUES ({self.i}, "{name}");'
            self.i += 1

        return self.execute_query(self.query)

    # View users table...
    def show_table(self):
        """
        View users table...
        Returns:

        """
        self.query = 'SELECT * FROM user_table;'
        return self.cur.execute(self.query)

    # View a user's name...
    def show_data(self, i):
        """
        View a user's name...
        Args:
            i:

        Returns:

        """
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        return self.cur.execute(self.query)

    # Change a user's name...
    def update_data(self, name, iduser):
        """
        Change a user's name...
        Args:
            name:
            iduser:

        Returns:

        """
        self.query = f'UPDATE user_table SET name = "{name}" WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    # Remove a user from the users table...
    def delete_data(self, iduser):
        """
        Remove a user from the users table...
        Args:
            iduser:

        Returns:

        """
        self.query = f'DELETE FROM user_table WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    # Delete the users table...
    def delete_table(self):
        """
        Delete the users table...
        Returns:

        """
        self.query = 'DROP TABLE user_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):

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
            self.i = int()
        except Exception as e:
            print(e)

    # Create the answers-users table...
    def create_table(self):
        """
        Create the answers-users table...
        Returns:

        """
        self.i = 1
        self.query = 'CREATE TABLE answer_user_table (' \
                     'idanswer_user INT PRIMARY KEY NOT NULL, ' \
                     'idanswer_fk INT,' \
                     'iduser_fk INT,' \
                     'score INT,'\
                     'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer),' \
                     'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        return self.execute_query(self.query)

    # Add a result to the answers-users table...
    def add_data(self, idanswer_fk, iduser_fk, score):
        """
        Add a result to the answers-users table
        :param idanswer_fk:
        :param iduser_fk:
        :param score:
        :return:
        """
        if self.i == int():
            self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {idanswer_fk}, {iduser_fk}, {score});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {idanswer_fk}, {iduser_fk}, {score});'
            self.i += 1

        return self.execute_query(self.query)

    # View answers-users table...
    def show_table(self):
        """
        View answers-users table...
        Returns:

        """
        self.query = 'SELECT * FROM answer_user_table;'
        return self.cur.execute(self.query)

    # View a user's result to a selected answer...
    def show_data(self, idanswer_user):
        """
        View a user's result to a selected answer...
        Args:
            idanswer_user:

        Returns:

        """
        self.query = f'SELECT * FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.cur.execute(self.query)

    # View a user's results to a selected answer...
    def show_result(self, name, idanswer_fk):
        """

        :param name:
        :param idanswer_fk:
        :return:
        """
        self.query = f'SELECT score FROM answer_user_table INNER JOIN user_table aut on answer_user_table.iduser_fk = aut.iduser WHERE name = "{name}" AND idanswer_fk = {idanswer_fk};'
        return self.cur.execute(self.query)

    # Change a user's result to an answer...
    def update_data(self, score, idanswer_user):
        """

        :param score:
        :param idanswer_user:
        :return:
        """
        self.query = f'UPDATE answer_user_table SET score = {score} WHERE idanswer_user = {idanswer_user};'
        return self.execute_query(self.query)

    # Remove a result from the answers-users table...
    def delete_data(self, idanswer_user):
        """
        Remove a result from the answers-users table...
        Args:
            idanswer_user:

        Returns:

        """
        self.query = f'DELETE FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.execute_query(self.query)

    # Delete the answers-users table...
    def delete_table(self):
        """
        Delete the answers-users table...
        Returns:

        """
        self.query = 'DROP TABLE answer_user_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        return self.flashcards_db.close()


# Create and initialize the questions-users table...
class QuestionUserTable:

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

    # Create the questions-users table...
    def create_table(self):
        """

        Returns:

        """
        self.i = 1
        self.query = 'CREATE TABLE question_user_table (' \
                     'idquestion_user INT PRIMARY KEY NOT NULL, ' \
                     'idquestion_fk INT,' \
                     'iduser_fk INT,' \
                     'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion),' \
                     'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        return self.execute_query(self.query)

    # Add a question's card to a user...
    def add_data(self, idquestion_fk, iduser_fk):
        """

        Args:
            idquestion_fk:
            iduser_fk:

        Returns:

        """
        if self.i == int():
            self.query = f'INSERT INTO question_user_table VALUES ({self.i}, {idquestion_fk}, {iduser_fk});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO question_user_table VALUES ({self.i}, {idquestion_fk}, {iduser_fk});'
            self.i += 1

        return self.execute_query(self.query)

    # View questions-users table...
    def show_table(self):
        """

        Returns:

        """
        self.query = 'SELECT * FROM question_user_table;'
        return self.cur.execute(self.query)

# ----------
# A MODIFIER
    # Afficher les informations relatives a un element de la table...
    def show_data(self, i):
        """

        Args:
            i:

        Returns:

        """
        self.query = f'SELECT * FROM question_user_table WHERE idquestion_user = {i};'
        return self.cur.execute(self.query)

    # Modifier le resultat d'un utilisateur a une question...
    def update_data(self, result, i):
        """
        Modifier le resultat d'un utilisateur a une question...
        Args:
            result:
            i:

        Returns:

        """
        self.query = f'UPDATE question_user_table SET result = {result} WHERE idanswer_user = {i};'
        return self.execute_query(self.query)
# ----------

    # Remove a link from the questions-users table...
    def delete_data(self, idquestion_user):
        """
        Remove a link from the questions-users table...
        Args:
            idquestion_user:

        Returns:

        """
        self.query = f'DELETE FROM question_user_table WHERE idquestion_user = {idquestion_user};'
        return self.execute_query(self.query)

    # Delete the questions-users table...
    def delete_table(self):
        """
        Delete the questions-users table...
        Returns:

        """
        self.query = 'DROP TABLE question_user_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):
        """

        Args:
            query:

        Returns:

        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        return self.flashcards_db.close()
