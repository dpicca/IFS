


# Import the database methods file
from model import sqlite_flashcard


class Controller:
    """
    A controller class that interacts with the flashcard database.
    """
    def add_question_c(self, question, paquet):
        """
        Adds a question to a specific packet.

        Args:
            param question: The content of the question.
            type question: str
            param paquet: The packet to which the question belongs.
            type paquet: str

        Returns:
            None

        """
        questionClass = sqlite_flashcard.QuestionTable()
        question_add = questionClass.add_data(question, paquet)
        return question_add

    def show_all_packs_c(self):
        """
        Retrieves all the available packets.

        Returns:
            list: All the packs.
        """
        question = sqlite_flashcard.QuestionTable()
        paquets_list = question.show_all_packs()
        return paquets_list

    def show_question_c(self, paquet):
        """
        Retrieves the questions from a specific packet.

        Args:
            param paquet: The name of the packet.
            type paquet: str

        Returns:
            cursor: The questions from the specified packet.

        """
        question = sqlite_flashcard.QuestionTable()
        question_show = question.show_question(paquet)
        return question_show

    # class AnswerTable:

    def add_answer_c(self, answer, paquet):
        """
        Adds an answer to a specific packet.

        Args:
            param answer: The content of the answer.
            type answer: str
            param paquet: The packet to which the answer belongs.
            type answer: str

        Returns:
            list: The added answer.
        """
        answerClass = sqlite_flashcard.AnswerTable()
        answer_add = answerClass.add_data(answer, paquet)
        return answer_add.fetchall()

    def show_answer_c(self, paquet):
        """
        Retrieves the answers from a specific packet.

        Args:
            param paquet: The name of the packet.
            type paquet: str

        Returns:
            cursor: The answers from the specified packet.
        """

        answer = sqlite_flashcard.AnswerTable()
        answer_show = answer.show_answer(paquet)
        return answer_show


    def answeruser_add_data_c(self, idanswer_fk, iduser_fk, score):
        """
        Adds user's answer data.

        Args:
            param idanswer_fk: The foreign key reference to the answer.
            type idanswer_fk: int
            param iduser_fk: The foreign key reference to the user.
            type iduser_fk: int
            param score: The score of the user's answer.
            type score: int

        Returns:
            cursor: The added user's answer data.
        """
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_add = answeruser.add_data(idanswer_fk, iduser_fk, score)
        return answeruser_add

