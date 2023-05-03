from googletrans import Translator
translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(translation.text)

from model import sqlite_flashcard

class Controller:
    #interaction entre frontend et backend
    def add_question(self,question,paquet)

        question = sqlite_flashcard.QuestionTable()
        question_add = question.add_data(question, paquet)
        return question_add.fetchall()
    def create_table(self):
        question = sqlite_flashcard.QuestionTable()
        question_create = question.create_table()
        return question_create.fetchall()
    def show_table(self):
        question = sqlite_flashcard.QuestionTable()
        question_show_t = question.show_table()
        return question_show_t.fetchall()
    def show_data(self, paquet):
        question = sqlite_flashcard.QuestionTable()
        question_show = question.show_data(paquet)
        returnquestion_show.fetchall()
    def
    question_update = question.update_data(question, paquet)
    res = question_update.fetchall()
    question_delete = question.delete_data(question)
    res = question_delete.fetchall()
    question_delete_t = question.delete_table()
    res = question_delete_t.fetchall()
    question_close = question.close_sqlite()
    res = question_delete_t.fetchall()
    answer = sqlite_flashcard.AnswerTable()
    answer_add = answer.add_data(answer, paquet)
    res = answer_add.fetchall()
    answer_create = answer.create_table()
    res = answer_create.fetchall()
    answer_show_t = answer.show_table()
    answer_show = answer.show_data(paquet)
    answer_update = answer.update_data(answer, paquet)
    answer_delete = answer.delete_data(paquet)
    answer_delete_t = answer.delete_table()
    answer_close = answer.close_sqlite()
    user = sqlite_flashcard.UserTable()
    user_add = user.add_data(name)
    user_create = user.create_table()
    user_show_t = user.show_table()
    user_show = user.show_data(i)
    user_update = user.update_data(name, i)
    user_delete = user.delete_data(name)
    user_delete_t = user.delete_table()
    user_close = user.close_sqlite()
    answeruser = sqlite_flashcard.AnswerUserTable()
    answeruser_add = answeruser.add_data(result)
    answeruser_create = answeruser.create_table()
    answeruser_show_t = answeruser.show_table()
    answeruser_show = answeruser.show_data(i)
    answeruser_update = answeruser.update_data(result, i)
    answeruser_delete = answeruser.delete_data(i)
    answeruser_delete_t = answeruser.delete_table()
    answeruser_close = answeruser.close_sqlite()

if __name__ == "__main__":
    main()

    for tuples in res:
        for ele in tuples:
            pass