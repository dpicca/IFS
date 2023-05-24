

# Interaction entre frontend et backend:
from model import sqlite_flashcard


class Controller:

    # class QuestionTable:
    """
    def add_question(self, question, paquet):
        question = sqlite_flashcard.QuestionTable()
        question_add = question.add_data(question, paquet)
        return question_add.fetchall()

    def create_table(self):
        question = sqlite_flashcard.QuestionTable()
        question_create = question.create_table()
        return question_create.fetchall() """

    def show_all_packs_c(self):
        """retouner tous les paquets"""
        question = sqlite_flashcard.QuestionTable()
        paquets_list = question.show_all_packs()
        return paquets_list

    def show_table_c(self):
        """

        Returns:

        """
        question = sqlite_flashcard.QuestionTable()
        question_show_t = question.show_table()
        return question_show_t.fetchall()

    def show_data_c(self, paquet):
        """

        Args:
            paquet:

        Returns:

        """
        question = sqlite_flashcard.QuestionTable()
        question_show = question.show_data(paquet)
        return question_show.fetchall()

    """ def update_data(self, question, paquet):
        question = sqlite_flashcard.QuestionTable()
        question_update = question.update_data(question, paquet)
        return question_update.fetchall()

    def delete_data(self, question):
        question = sqlite_flashcard.QuestionTable()
        question_delete = question.delete_data(question)
        return question_delete.fetchall()

    def delete_table(self):
        question = sqlite_flashcard.QuestionTable()
        question_delete_t = question.delete_table()
        return question_delete_t.fetchall()

    def close_sqlite(self):
        question = sqlite_flashcard.QuestionTable()
        question_close = question.close_sqlite()
        return question_close.fetchall()

    # class AnswerTable:
    def add_answer(self, answer, paquet):
        answer = sqlite_flashcard.AnswerTable()
        answer_add = answer.add_data(answer, paquet)
        return answer_add.fetchall()

    def answer_create_table(self):
        answer = sqlite_flashcard.AnswerTable()
        answer_create = answer.create_table()
        return answer_create.fetchall() """

    # class AnswerTable:
    def answer_show_table(self):
        answer = sqlite_flashcard.AnswerTable()
        answer_show_t = answer.show_table()
        return answer_show_t.fetchall()

    def answer_show_data(self, paquet):
        answer = sqlite_flashcard.AnswerTable()
        answer_show = answer.show_data(paquet)
        return answer_show.fetchall()

    """def answer_update_data(self, paquet):
        answer = sqlite_flashcard.AnswerTable()
        answer_update = answer.update_data(answer, paquet)
        return answer_update.fetchall()

    def answer_delete_data(self, paquet):
        answer = sqlite_flashcard.AnswerTable()
        answer_delete = answer.delete_data(paquet)
        return answer_delete.fetchall()

    def answer_delete_table(self):
        answer = sqlite_flashcard.AnswerTable()
        answer_delete_t = answer.delete_table()
        return answer_delete_t.fetchall()

    def answer_close_sqlite(self):
        answer = sqlite_flashcard.AnswerTable()
        answer_close = answer.close_sqlite()
        return answer_close.fetchall()

    # class UserTable:
    def add_user(self, name):
        user = sqlite_flashcard.UserTable()
        user_add = user.add_data(name)
        return user_add.fetchall()

    def user_create_table(self):
        user = sqlite_flashcard.UserTable()
        user_create = user.create_table()
        return user_create.fetchall()"""

    # class UserTable:
    def user_show_table(self, name):
        user = sqlite_flashcard.UserTable()
        user_show_t = user.show_table()
        return user_show_t.fetchall()

    def user_show_data(self, i):
        user = sqlite_flashcard.UserTable()
        user_show = user.show_data(i)
        return user_show.fetchall()

    """def user_update_data(self, name, i):
        user = sqlite_flashcard.UserTable()
        user_update = user.update_data(name, i)
        return user_update.fetchall()

    def user_delet_table(self):
        user = sqlite_flashcard.UserTable()
        user_delete = user.delete_data(name)
        return user_delete.fetchall()

    def user_delete_table(self):
        user = sqlite_flashcard.UserTable()
        user_delete_t = user.delete_table()
        return user_delete_t.fetchall()

    def user_close_sqlite(self):
        user = sqlite_flashcard.UserTable()
        user_close = user.close_sqlite()
        return user_close.fetchall()

    # class AnsweruserTable:
    def answeruser_add_data(self, result):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_add = answeruser.add_data(result)
        return answeruser_add.fetchalle()

    def answeruser_create_table(self):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_create = answeruser.create_table()
        return answeruser_create.fetchall() """

    # class AnsweruserTable:
    def answeruser_show_table(self):
        """

        Returns:

        """
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_show_t = answeruser.show_table()
        return answeruser_show_t.fetchall()

    def answeruser_show_data(self, idanswer_user):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_show = answeruser.show_data(i)
        return answeruser_show.fetchall()

    """def answeruser_update_data(self, result, i):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_update = answeruser.update_data(result, i)
        return answeruser_update.fetchall()

    def answeruser_delete_data(self, i):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_delete = answeruser.delete_data(i)
        return answeruser_delete.fetchall()

    def answeruser_delete_table(self):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_delete_t = answeruser.delete_table()
        return answeruser_delete_t.fetchall()

    def answeruser_close_sqlite(self):
        answeruser = sqlite_flashcard.AnswerUserTable()
        answeruser_close = answeruser.close_sqlite()
        return answeruser_close.fetchall() """

    #class QuestionUserTable
    def questionuser_show_data(self, i):
        questionuser = sqlite_flashcard.QuestionUserTable()
        questionuser_show_data = questionuser.show_data()
        return questionuser_show_data.fetchall()

    def questionuser_show_table(self):
        questionuser = sqlite_flashcard.QuestionUserTable()
        questionuser_show_t = questionuser.show_table()
        return questionuser_show_t.fetchall()


    #for tuples in res:
    #    for ele in tuples:
    #       pass