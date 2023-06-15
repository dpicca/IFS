"""
This file is an implementation of a SQLite database with five tables: 
question_table, answer_table, user_table, answer_user_table and question_user_table. 
Each table is represented by a corresponding class: 
- QuestionTable, AnswerTable and UserTable :These classes provide the necessary functionalities to interact 
with the database and perform operations such as insertion, updating, deletion, and retrieval of data.
- AnswerUserTable and QuestionUserTable : These classes represent tables in an SQLite database for managing 
the relationship between answers and users, and questions and users, respectively.
"""""

# Import packages.
import sqlite3


# Create and initialize the questions table...
class QuestionTable:
    """
    Class representing the questions table in an SQLite database.
    """
    def __init__(self):
        """
        Initializes the QuestionTable class.
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.
        """
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

    def create_table(self):
        """
        Creates the "question_table" in the database.

        Returns:
            The result of executing the SQL query.
            rtype: sqlite3.Cursor
        """
        self.i = 1
        self.query = 'CREATE TABLE question_table (' \
                     'idquestion INT PRIMARY KEY NOT NULL,' \
                     'question VARCHAR(40),' \
                     'paquet VARCHAR(50),' \
                     'idanswer_fk INT,  ' \
                     'FOREIGN KEY (idanswer_fk) REFERENCES answer_table(idanswer));'
        return self.execute_query(self.query)

    def add_data(self, question, paquet):
        """
        Adds a question card to the question table.

        Args:
            param question: The content of the question.
            type question: str
            param paquet: The packet to which the question belongs.
            type paquet: str

        Returns:
            True if the data is successfully added, False otherwise.
        """
        if self.i > 1:
            self.query = f'INSERT INTO question_table VALUES ({self.i}, "{question}", "{paquet}", {self.i});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO question_table VALUES ({self.i}, "{question}", "{paquet}", {self.i});'
            self.i += 1

        return self.execute_query(self.query)

    def show_table(self):
       """
        Displays the complete contents of the question table.

        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor
        """
       self.query = 'SELECT * FROM question_table;'
       return self.cur.execute(self.query)

    def show_question(self, paquet):
        """
        Displays the question cards of a specific packet.

        Args:
            param paquet: The name of the question packet.
            type paquet: str

        Returns:
            The result of the SQL query containing the questions from the packet.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT question FROM question_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    def show_all_packs(self):
        """
        Displays all question packets available in the table.

        Returns:
            The result of the SQL query containing distinct values of the "paquet" column.
            rtype: sqlite3.Cursor
        """
        self.query = 'SELECT paquet FROM question_table'
        print(self.query)
        return self.cur.execute(self.query)

    def show_pack(self, iduser_fk):
        """
        Displays all question packets saved for a given user.

        Args:
            param iduser_fk: The user identifier.
            type iduser_fk: int

        Returns:
            The result of the SQL query containing the question packets for the user.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT paquet FROM question_user_table ' \
                     f'INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion ' \
                     f'WHERE iduser_fk = {iduser_fk};'
        return self.cur.execute(self.query)

    def user_show_questions(self, iduser_fk, paquet):
        """
        Displays the questions from a specific packet for a given user.

        Args:
            param iduser_fk: The user identifier.
            type iduser_fk: int
            param paquet: The name of the question packet.
            type paquet: str

        Returns:
            The result of the SQL query containing the questions from the packet for the user.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT iduser_fk, question FROM question_user_table ' \
                     f'INNER JOIN question_table aut on question_user_table.idquestion_fk = aut.idquestion ' \
                     f'WHERE iduser_fk = {iduser_fk} AND paquet = "{paquet}";'
        return self.cur.execute(self.query)

    def update_data(self, question, idquestion):
        """
        Updates the data of an existing question.

        Args:
            param question: The new question.
            type question: str
            param idquestion: The identifier of the question to update.
            type idquestion: int

        Returns:
             None
        """
        self.query = f'UPDATE question_table SET question = "{question}" WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    def delete_data(self, idquestion):
        """
        Deletes a question from the table using its identifier.

        Args:
            param idquestion: The identifier of the question to delete.
            type idquestion: int

        Returns:
            The result of executing the SQL query.
            rtype: sqlite3.Cursor
        """
        self.query = f'DELETE FROM question_table WHERE idquestion = {idquestion};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Delete the whole questions table.

        Returns:
             None
        """
        self.query = 'DROP TABLE question_table;'
        return self.execute_query(self.query)

    def execute_query(self, query):
        """
        Run the query by applying it to the database.

        Args:
            param query: SQL Statement
            type query: str
        Returns:
             None
        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Close the database.

        Returns:
             None
        """
        return self.flashcards_db.close()


# Create and initialize the answers table...
class AnswerTable:
    """
    Class representing the answers table in an SQLite database.

    """
    def __init__(self):
        """
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.
        """
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
        Creates the "answer_table" in the database.

        Returns:
             The result of executing the SQL query.
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

    def add_data(self, answer, paquet):
        """
        Add an answer card to the answer table.

        Args:
            param answer: The content of the answer.
            type answer: str
            param paquet: The packet to which the answer belongs.
            type paquet: str

        Returns:
             None

        Notes:
            This method executes the SQL query to insert a new answer card into the answer table.
        """
        if self.i > 1:
            self.query = f'INSERT INTO answer_table VALUES ({self.i}, "{answer}", "{paquet}", {self.i});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO answer_table VALUES ({self.i}, "{answer}", "{paquet}", {self.i});'
            self.i += 1

        return self.execute_query(self.query)

    def show_table(self):
        """
        Displays the complete contents of the answer table.

        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor
        """
        self.query = 'SELECT * FROM answer_table;'
        return self.cur.execute(self.query)

    def show_answer(self, paquet):
        """
        Displays the answer cards of a specific packet.

        Args:
            param paquet: The name of the answer packet.
            type paquet:str

        Returns:
            The result of the SQL query containing the answers from the packet.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT answer FROM answer_table WHERE paquet = "{paquet}";'
        return self.cur.execute(self.query)

    def show_answer_by_question(self, idquestion):
        """
        Retrieves the answer corresponding to a given question ID from the answer table.

        Args:
            param idquestion: The identifier of the question.
            type idquestion: int

        Returns:
            The result of the SQL query containing the corresponding answer.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT answer FROM answer_table ' \
                     f'INNER JOIN question_table aut on answer_table.idanswer = aut.idquestion ' \
                     f'WHERE idquestion = {idquestion};'
        return self.cur.execute(self.query)

    def update_data(self, answer, idanswer):
        """
        Updates the data of an existing answer.

        Args:
            param answer: The new answer.
            type answer: str
            param idanswer: The identifier of the answer to update.
            type idanswer: int

        Returns:
             None

        Notes:
            This method executes the SQL query to update the data of an existing answer.
        """
        self.query = f'UPDATE answer_table SET answer = "{answer}" WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    def delete_data(self, idanswer):
        """
        Removes a card from the answer table.

        Args:
            param idanswer: The identifier of the answer to remove.
            type idanswer: int

        Returns:
             None

         Notes:
            This method executes the SQL query to delete a card from the answer table.
        """
        self.query = f'DELETE FROM answer_table WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Delete the whole answers table.

        Returns:
             None

        Notes:
            This method executes the SQL query to delete the entire answer table.
        """
        self.query = 'DROP TABLE answer_table;'
        return self.execute_query(self.query)

    def execute_query(self, query):
        """
         Executes an SQL query by applying it to the database.

         Args:
            param query: The SQL statement to execute.
            type query: str

         Returns:
             None

        Notes:
            This method executes the provided SQL query and commits the changes to the database.
        """

        self.cur.execute(query)
        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
             None

        Notes:
            This method closes the connection to the SQLite database and releases any associated resources.
        """
        return self.flashcards_db.close()


# Create and initialize the users table...
class UserTable:
    """
    Class representing the users table in an SQLite database.
    """
    def __init__(self):
        """
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.
        """
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
        Creates the "user_table" in the database.

        Returns:
             The result of executing the SQL query.
        """
        self.i = 1
        self.query = 'CREATE TABLE user_table (' \
                     'iduser INT PRIMARY KEY NOT NULL,' \
                     'name VARCHAR(40));'
        return self.execute_query(self.query)

    def add_data(self, name):
        """
        Adds a user to the users table.

        Args:
            param name: The name of the user.
            type name: str

        Returns:
             None
        Notes:
            This method executes the SQL query to insert a new user into the user table.
        """
        if self.i > 1:
            self.query = f'INSERT INTO user_table VALUES ({self.i}, "{name}");'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO user_table VALUES ({self.i}, "{name}");'
            self.i += 1

        return self.execute_query(self.query)

    def show_table(self):
        """
        Displays the complete contents of the users table.

        Returns:
            The result of the SQL query containing all users of the table.
            rtype: sqlite3.Cursor
        """
        self.query = 'SELECT * FROM user_table;'
        return self.cur.execute(self.query)

    def show_data(self, i):
        """
        Displays the information of a specific user from the database.

        Args:
            param i: The identifier of the user.
            typa i: int

        Returns:
            The result of the SQL query containing the user's information.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT * FROM user_table WHERE iduser = {i};'
        return self.cur.execute(self.query)

    def show_iduser(self, name):
        """
        Retrieves the ID of a specific user.

        Args:
            param name: The name of the user.
            type name: str

        Returns:
            The result of the SQL query containing the user's ID.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT iduser FROM user_table WHERE name = "{name}";'
        return self.cur.execute(self.query)

    def update_data(self, name, iduser):
        """
        Changes a user's name.

        Args:
            param name: The new name of the user.
            type name: str
            param iduser: The identifier of the user to update.
            type iduser: int

        Returns:
             None

        Notes:
            This method executes the SQL query to update the name of a specific user.
        """
        self.query = f'UPDATE user_table SET name = "{name}" WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    def delete_data(self, iduser):
        """
        Removes x a user from the user table

        Args:
            param iduser:The identifier of the user to remove.
            type iduser: int

        Returns:
             None

        Notes:
            This method executes the SQL query to delete a specific user from the user table.
        """
        self.query = f'DELETE FROM user_table WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Delete the whole users table.

        Returns:
             None

        Notes:
            This method executes the SQL query to delete the entire user table.
        """
        self.query = 'DROP TABLE user_table;'
        return self.execute_query(self.query)

    def execute_query(self, query):
        """
        Executes an SQL query by applying it to the database.

        Args:
            param query: The SQL statement to execute.
            type query: str

        Returns:
             None

        Notes:
            This method executes the provided SQL query and commits the changes to the database.
        """

        self.cur.execute(query)
        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
             None

        Notes:
            This method closes the connection to the SQLite database and releases any associated resources.
        """
        return self.flashcards_db.close()


# Create and initialize the answers-users table...
class AnswerUserTable:
    """
    Class representing the answers-users table in an SQLite database
    """
    def __init__(self):
        """
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.
        """
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
        Create the answers-users table.

        Returns:
             The result of executing the SQL query.
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

        Args:
            param idanswer_fk: The ID of the answer.
            type idanswer: int
            param iduser_fk: The ID of the user.
            type iduser: int
            param score: The score of the user's result.
            type score: int

        Returns:
             None

        Notes:
            This method executes an SQL query to insert a new row with the provided data into the "answer_user_table".
        """
        if self.i > 1:
            self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {idanswer_fk}, {iduser_fk}, {score});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO answer_user_table VALUES ({self.i}, {idanswer_fk}, {iduser_fk}, {score});'
            self.i += 1

        return self.execute_query(self.query)

    def show_table(self):
        """
        Displays the complete contents of the answers-users table.

        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor
        """
        self.query = 'SELECT * FROM answer_user_table;'
        return self.cur.execute(self.query)

    def show_data(self, idanswer_user):
        """
        Displays the information of a specific row in the answers-users table.

        Args:
            param idanswer_user: The identifier of the answer-user result.
            type idanswer_user: int

        Returns:
            The result of the SQL query containing the row's information.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT * FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.cur.execute(self.query)


    def show_result(self, name, idanswer_fk):
        """
        Displays the result of a specific user to a selected answer.

        Args:
            param name: The name of the user.
            type name: str
            param idanswer_fk: The ID of the answer.
            type idanswer: int

        Returns
            The result of the SQL query containing the user's results.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT score FROM answer_user_table ' \
                     f'INNER JOIN user_table aut on answer_user_table.iduser_fk = aut.iduser ' \
                     f'WHERE name = "{name}" AND idanswer_fk = {idanswer_fk};'
        return self.cur.execute(self.query)

    def update_data(self, score, idanswer_user):
        """
        Change a user's result to an answer.

        Args:
            param score: The new score for the user's result.
            type score: int
            param idanswer_user: The ID of the answer-user result to update.
            type idanswer: int

        Returns:
             update operation
        """
        self.query = f'UPDATE answer_user_table SET score = {score} WHERE idanswer_user = {idanswer_user};'
        return self.execute_query(self.query)

    def delete_data(self, idanswer_user):
        """
        Remove a result from the answers-users table

        Args:
            param idanswer_user: The ID of the answer-user result to delete.
            type idanswer_user: int

        Returns:
            None

        Notes:
            This method deletes the row from the "answer_user_table" that matches the provided ID by executing an SQL query.
        """
        self.query = f'DELETE FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Deletes the answers-users table from the database.

        Returns:
            None

        Notes:
            This method drops the "answer_user_table" from the database by executing an SQL query.
        """
        self.query = 'DROP TABLE answer_user_table;'
        return self.execute_query(self.query)

    def execute_query(self, query):
        """
         Executes an SQL query by applying it to the database.

         Args:
            param query: The SQL statement to execute.
            type query: str

         Returns:
              None

        Notes:
            This method executes the provided SQL query by applying it to the connected database.
        """

        self.cur.execute(query)
        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
            None

        Notes:
            This method closes the connection to the connected SQLite database.
        """
        return self.flashcards_db.close()


# Create and initialize the questions-users table...
class QuestionUserTable:
    """
    Class representing the questions-users table in an SQLite database.
    """

    def __init__(self):
        """
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.
        """
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
        Creates the "question_user_table" in the database.

        Returns:
            The result of executing the SQL query.

        """
        self.i = 1
        self.query = 'CREATE TABLE question_user_table (' \
                     'idquestion_user INT PRIMARY KEY NOT NULL, ' \
                     'idquestion_fk INT,' \
                     'iduser_fk INT,' \
                     'FOREIGN KEY (idquestion_fk) REFERENCES question_table(idquestion),' \
                     'FOREIGN KEY (iduser_fk) REFERENCES user_table(iduser));'
        return self.execute_query(self.query)

    def add_data(self, idquestion_fk, iduser_fk):
        """
        Add a question's card to a user.

        Args:
            param idquestion_fk: The ID of the question.
            type idquestion_fk: int
            param iduser_fk: The ID of the user.
            type iduser_fk: int

        Returns:
            The add operation.

        """
        if self.i > 1:
            self.query = f'INSERT INTO question_user_table VALUES ({self.i}, {idquestion_fk}, {iduser_fk});'
            self.i += 1
        else:
            self.i = 1
            self.query = f'INSERT INTO question_user_table VALUES ({self.i}, {idquestion_fk}, {iduser_fk});'
            self.i += 1

        return self.execute_query(self.query)

    def show_table(self):
        """
        Displays the complete contents of the questions-users table.

        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor

        """
        self.query = 'SELECT * FROM question_user_table;'
        return self.cur.execute(self.query)

    def show_data(self, idquestion_user):
        """
        Displays the information for a specific element in the question_user_table.

        Args:
            param idquestion_user: The ID of the question-user entry.
            type idquestion_user: int

        Returns:
            The result of the SQL query containing the question-user entry.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT * FROM question_user_table WHERE idquestion_user = {idquestion_user};'
        return self.cur.execute(self.query)

    def delete_data(self, idquestion_user):
        """
        Removes a link from the questions-users table.

        Args:
            param idquestion_user: The ID of the question-user entry to delete.
            type idquestion_user: int

        Returns:
            None

        Notes:
            This method deletes a row from the "question_user_table" that matches the provided ID by executing an SQL query.
        """
        self.query = f'DELETE FROM question_user_table WHERE idquestion_user = {idquestion_user};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Deletes the questions-users table from the database.

        Returns:
            None

        Notes:
            This method drops the "question_user_table" from the database by executing an SQL query.
        """
        self.query = 'DROP TABLE question_user_table;'
        return self.execute_query(self.query)


    def execute_query(self, query):
        """
        Executes an SQL query by applying it to the database.

        Args:
            param query: The SQL statement to execute.
            type query: str

        Returns:
            None

        Notes:
            This method executes the provided SQL query by applying it to the connected database.
        """

        self.cur.execute(query)
        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
            None

        Notes:
            This method closes the connection to the connected SQLite database.
        """
        return self.flashcards_db.close()
