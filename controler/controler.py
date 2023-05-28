

# Import the database methods file
from model import sqlite_flashcard


class Controller:

    # class QuestionTable:

    def add_question_c(self, question, paquet):
        """

                Args:
                    question, paquet

                Returns:
                    add the question to the paquet

                """
        questionClass = sqlite_flashcard.QuestionTable()
        question_add = questionClass.add_data(question, paquet)
        return question_add

    def show_all_packs_c(self):
        """

        Args:
            None

        Returns:
            all the packs

        """
        question = sqlite_flashcard.QuestionTable()
        paquets_list = question.show_all_packs()
        return paquets_list

    def show_question_c(self, paquet):
        """

        Args:
            paquet

        Returns:
            the questions from the paquet

        """
        question = sqlite_flashcard.QuestionTable()
        question_show = question.show_question(paquet)
        return question_show

    # class AnswerTable:

    def add_answer_c(self, answer, paquet):
        """

                Args:
                    answer, paquet

                Returns:
                    add the answer to the paquet

                """
        answerClass = sqlite_flashcard.AnswerTable()
        answer_add = answerClass.add_data(answer, paquet)
        return answer_add.fetchall()

    def show_answer_c(self, paquet):
        """

        Args:
            paquet

        Returns:
            the answers from the paquet

        """

        answer = sqlite_flashcard.AnswerTable()
        answer_show = answer.show_answer(paquet)
        return answer_show


    def answeruser_add_data_c(self, idanswer_fk, iduser_fk, score):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_add = answeruser.add_data(idanswer_fk, iduser_fk, score)
        return answeruser_add
    