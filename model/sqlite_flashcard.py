# Import packages.
import sqlite3


# Create and initialize the questions table...
class QuestionTable:
    """
    Class representing the questions table in an SQLite database.
    """
    def __init__(self):
        """
        Initializes a connection to the SQLite database and creates a cursor to execute SQL queries.

        Returns:
             None
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

    def add_data(self, question: str, paquet: str):
        """
        Adds a question card to the question table.

        Args:
            param question: The content of the question.
            type question: str
            param paquet: The packet to which the question belongs.
            type paquet: str

        Returns:
            None
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

    def show_question(self, paquet: str):
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

    def show_pack(self, iduser_fk: int):
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

    def user_show_questions(self, iduser_fk: int, paquet: str):
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

    def update_data(self, question: str, idquestion: int):
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

    def delete_data(self, idquestion: int):
        """
        Deletes a question from the table using its identifier.

        Args:
            param idquestion: The identifier of the question to delete.
            type idquestion: int

        Returns:
             None
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

    def execute_query(self, query: str):
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

        Returns:
             None
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

    def add_data(self, answer: str, paquet: str):
        """
        Add an answer card to the answer table.

        Args:
            param answer: The content of the answer.
            type answer: str
            param paquet: The packet to which the answer belongs.
            type paquet: str

        Returns:
             None
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

    def show_answer(self, paquet: str):
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

    def show_answer_by_question(self, idquestion: int):
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

    def update_data(self, answer: str, idanswer: int):
        """
        Updates the data of an existing answer.

        Args:
            param answer: The new answer.
            type answer: str
            param idanswer: The identifier of the answer to update.
            type idanswer: int

        Returns:
             None
        """
        self.query = f'UPDATE answer_table SET answer = "{answer}" WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    def delete_data(self, idanswer: int):
        """
        Removes a card from the answer table.

        Args:
            param idanswer: The identifier of the answer to remove.
            type idanswer: int

        Returns:
             None
        """
        self.query = f'DELETE FROM answer_table WHERE idanswer = {idanswer};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Delete the whole answers table.

        Returns:
             None
        """
        self.query = 'DROP TABLE answer_table;'
        return self.execute_query(self.query)

    def execute_query(self, query: str):
        """
         Executes an SQL query by applying it to the database.

         Args:
            param query: The SQL statement to execute.
            type query: str

         Returns:
             None
        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
             None
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

    def add_data(self, name: str):
        """
        Adds a user to the users table.

        Args:
            param name: The name of the user.
            type name: str

        Returns:
             None
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

    def show_data(self, i: int):
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

    def show_iduser(self, name: str):
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

    def update_data(self, name: str, iduser: int):
        """
        Changes a user's name.

        Args:
            param name: The new name of the user.
            type name: str
            param iduser: The identifier of the user to update.
            type iduser: int

        Returns:
             None
        """
        self.query = f'UPDATE user_table SET name = "{name}" WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    def delete_data(self, iduser: int):
        """
        Removes x a user from the user table

        Args:
            param iduser:The identifier of the user to remove.
            type iduser: int
        Returns:
             None
        """
        self.query = f'DELETE FROM user_table WHERE iduser = {iduser};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Delete the whole users table.

        Returns:
             None
        """
        self.query = 'DROP TABLE user_table;'
        return self.execute_query(self.query)

    # ...
    def execute_query(self, query: str):
        """
        Executes an SQL query by applying it to the database.

        Args:
            param query: The SQL statement to execute.
            type query: str
        Returns:
             None
        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
             None
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

        Returns:
            None
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

    def add_data(self, idanswer_fk: int, iduser_fk: int, score: int):
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
        View answers-users table

        Returns:
             None
        """
        self.query = 'SELECT * FROM answer_user_table;'
        return self.cur.execute(self.query)

    def show_data(self, idanswer_user: int):
        """
        Displays the complete contents of the answers-users table.

        Args:
            param idanswer_user:
            type idanswer_user: int
        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT * FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.cur.execute(self.query)


    def show_result(self, name: str, idanswer_fk: int):
        """
        Displays the result of a specific user to a selected answer.

        Args:
            param name: The name of the user.
            type name: str
            param idanswer_fk:The ID of the answer.
            type idanswer: int
        Returns
            The result of the SQL query containing the user's results.
            rtype: sqlite3.Cursor
        """
        self.query = f'SELECT score FROM answer_user_table ' \
                     f'INNER JOIN user_table aut on answer_user_table.iduser_fk = aut.iduser ' \
                     f'WHERE name = "{name}" AND idanswer_fk = {idanswer_fk};'
        return self.cur.execute(self.query)

    def update_data(self, score: int, idanswer_user: int):
        """
        Change a user's result to an answer

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

    def delete_data(self, idanswer_user: int):
        """
        Remove a result from the answers-users table

        Args:
            param idanswer_user: The ID of the answer-user result to delete.
            type idanswer_user: int

        Returns:
            None
        """
        self.query = f'DELETE FROM answer_user_table WHERE idanswer_user = {idanswer_user};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Deletes the answers-users table from the database.

        Returns:
            None
        """
        self.query = 'DROP TABLE answer_user_table;'
        return self.execute_query(self.query)

    # ...
    def execute_query(self, query: str):
        """
         Executes an SQL query by applying it to the database.

         Args:
            param query: The SQL statement to execute.
            type query: str

         Returns:
              None
        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
            None
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

        Returns:
            None
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

    def add_data(self, idquestion_fk: int, iduser_fk: int):
        """
        Add a question's card to a user

        Args:
            param idquestion_fk: The ID of the question.
            type idquestion_fk: int
            param iduser_fk: The ID of the user.
            type iduser_fk: int

        Returns:
            The add operation

        """
        if self.i > 1:
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
        Displays the complete contents of the questions-users table.

        Returns:
            The result of the SQL query containing all rows of the table.
            rtype: sqlite3.Cursor

        """
        self.query = 'SELECT * FROM question_user_table;'
        return self.cur.execute(self.query)

    def show_data(self, idquestion_user: int):
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

    def delete_data(self, idquestion_user: int):
        """
        Removes a link from the questions-users table.

        Args:
            param idquestion_user: The ID of the question-user entry to delete.
            type idquestion_user: int

        Returns:
            None
        """
        self.query = f'DELETE FROM question_user_table WHERE idquestion_user = {idquestion_user};'
        return self.execute_query(self.query)

    def delete_table(self):
        """
        Deletes the questions-users table from the database.

        Returns:
            None
        """
        self.query = 'DROP TABLE question_user_table;'
        return self.execute_query(self.query)


    def execute_query(self, query: str):
        """
        Executes an SQL query by applying it to the database.

        Args:
            param query: The SQL statement to execute.
            type query: str

        Returns:
            None

        """

        self.cur.execute(query)

        # Save the change.
        self.flashcards_db.commit()

    def close_sqlite(self):
        """
        Closes the connection to the SQLite database.

        Returns:
            None
        """
        return self.flashcards_db.close()
