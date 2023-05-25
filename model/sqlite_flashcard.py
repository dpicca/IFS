# Import packages.
import sqlite3


# Create and initialize the questions table...
class QuestionTable:

    # Initialize the class...
    def __init__(self):
        # Create and connect to the database...
        try:
            self.flashcards_db = sqlite3.connect('./model/ifc.db')
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
        Create the questions table
        Returns: None

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
        Add a question's card to the questions table
        :param question: string
        :param paquet: string (the pack where this question belongs to)
        :return: None
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
        Returns: all the rows from questions table

        """
        self.query = 'SELECT * FROM question_table;'
        return self.cur.execute(self.query)

    # View the question's cards in a selected pack...
    def show_question(self, paquet):
        """

        Args:get all the questions from data base for the given pack
            paquet:

        Returns: list of questions or empty list

        """
        self.query = f'SELECT question FROM question_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # View all the packages...
    def show_all_packs(self):
        """
        Give all the packs from questions table
        :return: list of packs or empty list
        """
        self.query = 'SELECT paquet FROM question_table'
        print(self.query)
        return self.cur.execute(self.query)

    # View a user's saved packages...
    def show_pack(self, iduser_fk):
        """
        For a given user returns all the packs
        :param iduser_fk: int
        :return: list of pack or empty list
        """
        self.query = f'SELECT paquet FROM question_user_table ' \
                     f'INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion ' \
                     f'WHERE iduser_fk = {iduser_fk};'
        return self.cur.execute(self.query)

    # View a user's questions for a selected pack...
    def user_show_questions(self, iduser_fk, paquet):
        """
        Give the users questions for a given pack
        :param iduser_fk: int
        :param paquet: string
        :return:list of pack or empty list
        """
        self.query = f'SELECT iduser_fk, question FROM question_user_table ' \
                     f'INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion ' \
                     f'WHERE iduser_fk = {iduser_fk} AND paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # Change the value of a question's card...
    def update_data(self, question, idquestion):
        """
        Use this fonction when we need to update an existing question
        Args:
            question: string
            idquestion: int

        Returns: updated version of the question

        """
        self.query = f'UPDATE question_table SET question = "{question}" WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    # Remove a card from the questions table...
    def delete_data(self, idquestion):
        """
        Remove a card from the questions table...
        Args:
            idquestion:int

        Returns: None

        """
        self.query = f'DELETE FROM question_table WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    # Delete the questions table...
    def delete_table(self):
        """
        Delete all the questions table
        Returns: None

        """
        self.query = 'DROP TABLE question_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):
        """
        Takes the query and applies it to the database
        Args:
            query:string(SQL Statement)

        Returns: None

        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    # Close the database...
    def close_sqlite(self):
        """
        Close the database
        Returns:

        """
        return self.flashcards_db.close()


# Create and initialize the answers table...
class AnswerTable:

    # Initialize the class...
    def __init__(self):
        try:
            # Create and connect to the database...
            self.flashcards_db = sqlite3.connect('./model/ifc.db')
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

        Returns: list of pack

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
        Add an answers card to the answers table
        Args:
            answer: string
            paquet: string
        Returns: None

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
        Returns: list of answers

        """
        self.query = 'SELECT * FROM answer_table;'
        return self.cur.execute(self.query)

    # View the answer's cards in a selected pack...
    def show_answer(self, paquet):
        """
        View the answer's cards in a selected pack
        Args:
            paquet:string

        Returns:list of answers in a given pack

        """
        self.query = f'SELECT answer FROM answer_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    # View the answer's cards of a selected question...
    def show_answer_by_question(self, idquestion):
        """
        Takes of the id of a question and returns the coresponding answer from the answers table
        :param idquestion: int
        :return: answers
        """
        self.query = f'SELECT answer FROM answer_table ' \
                     f'INNER JOIN question_table aut on answer_table.idanswer = aut.idquestion ' \
                     f'WHERE idquestion = {idquestion};'
        return self.cur.execute(self.query)

    # Change the value of an answer's card...
    def update_data(self, answer, idanswer):
        """
        Change the value of an answer's card
        Args:
            answer: string
            idanswer:int
        Returns: updated answer

        """
        self.query = f'UPDATE answer_table SET answer = "{answer}" WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    # Remove a card from the answers table...
    def delete_data(self, idanswer):
        """
        This fonction remove a card from the answers table
        Args:
            idanswer:int

        Returns:None

        """
        self.query = f'DELETE FROM answer_table WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    # Delete the answers table...
    def delete_table(self):
        """
        Delete all the answers table
        Returns:None

        """
        self.query = 'DROP TABLE answer_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):
        """
        Takes the query and applies it to the database
        Args:
            query: string
        Returns:None

        """

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
            self.flashcards_db = sqlite3.connect('./model/ifc.db')
            # Allow queries.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = int()
        except Exception as e:
            print(e)

    def create_table(self):
        """
        Create the users table
        Returns:None

        """
        self.i = 1
        self.query = 'CREATE TABLE user_table (' \
                     'iduser INT PRIMARY KEY NOT NULL,' \
                     'name VARCHAR(40));'
        return self.execute_query(self.query)

    def add_data(self, name):
        """
        Add a user to the users table
        Args:
            name:string

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
        View users table
        Returns:

        """
        self.query = 'SELECT * FROM user_table;'
        return self.cur.execute(self.query)

    def show_data(self, i):
        """
        View a user's informations from the database
        Args:
            i:int

        Returns:a user

        """
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        return self.cur.execute(self.query)

    def show_iduser(self, name):
        """
        View a user's id
        :param name:string
        :return:integer
        """
        self.query = f'SELECT iduser FROM user_table WHERE name = "{name}";'
        return self.cur.execute(self.query)

    def update_data(self, name, iduser):
        """
        Change a user's name
        Args:
            name:string
            iduser:int
        Returns:updated data

        """
        self.query = f'UPDATE user_table SET name = "{name}" WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    def delete_data(self, iduser):
        """
        Remove a user from the users table
        Args:
            iduser:int

        Returns:None

        """
        self.query = f'DELETE FROM user_table WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    # Delete the users table...
    def delete_table(self):
        """
        Delete all the users
        Returns:None

        """
        self.query = 'DROP TABLE user_table;'
        return self.execute_query(self.query)

    # Run the query...
    def execute_query(self, query):
        """
        Takes the query and applies it to the database
        Args:
            query:string

        Returns:returns whatever database returns

        """

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
            self.flashcards_db = sqlite3.connect('./model/ifc.db')
            # Allow queries.
            self.cur = self.flashcards_db.cursor()
            self.query = ''
            self.i = int()
        except Exception as e:
            print(e)

    # Create the answers-users table...
    def create_table(self):
        """
        Create the answers-users table
        Returns:None

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

    def add_data(self, idanswer_fk, iduser_fk, score):
        """
        Add a result to the answers-users table
        :param idanswer_fk:int
        :param iduser_fk:int
        :param score:int
        :return:None
        """
        if self.i == 0:
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
        View answers-users table
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


    def show_result(self, name, idanswer_fk):
        """
        View a user's results to a selected answer
        :param name:string
        :param idanswer_fk:int
        :return: users results
        """
        self.query = f'SELECT score FROM answer_user_table ' \
                     f'INNER JOIN user_table aut on answer_user_table.iduser_fk = aut.iduser ' \
                     f'WHERE name = "{name}" AND idanswer_fk = {idanswer_fk};'
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
            self.flashcards_db = sqlite3.connect('./model/ifc.db')
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

    def delete_table(self):
        """
        Delete the questions-users table
        Returns:

        """
        self.query = 'DROP TABLE question_user_table;'
        return self.execute_query(self.query)


    def execute_query(self, query):
        """
        Run the query
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
