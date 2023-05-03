from googletrans import Translator
translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(translation.text)

import sqlite_flashcard #?
#interaction entre frontend et backend
#il faut les argument du frontend
def main():

    question = sqlite_flachcard.QuestionTable()
    question_add = question.add_data(arg1, arg2)
    question_create = question.create_table()
    question_show_t = question.show_table()
    question_show = question.show_data(arg1)
    question_update = question.update_data(arg1, arg2)
    question_delete = question.delete_data(arg1)
    question_delete_t = question.delete_table(arg1)
    question_close = question.close_sqlite()
    answer = sqlite_flashcard.AnswerTable()
    answer_add = answer.add_data(arg1, arg2)
    answer_create = answer.create_table()
    answer_show_t = answer.show_table()
    answer_show = answer.show_data(arg1)
    answer_update = answer.update_data(arg1, arg2)
    answer_delete = answer.delete_data(arg1)
    answer_delete_t = answer.delete_table(arg1)
    answer_close = answer.close_sqlite()
    user = sqlite_flashcard.UserTable()
    user_add = user.add_data(arg1, arg2)
    user_create = user.create_table()
    user_show_t = user.show_table()
    user_show = user.show_data(arg1)
    user_update = user.update_data(arg1, arg2)
    user_delete = user.delete_data(arg1)
    user_delete_t = user.delete_table(arg1)
    user_close = user.close_sqlite()
    answeruser = sqlite_flashcard.AnswerUserTable()
    answeruser_add = answeruser.add_data(arg1, arg2)
    answeruser_create = answeruser.create_table()
    answeruser_show_t = answeruser.show_table()
    answeruser_show = answeruser.show_data(arg1)
    answeruser_update = answeruser.update_data(arg1, arg2)
    answeruser_delete = answeruser.delete_data(arg1)
    answeruser_delete_t = answeruser.delete_table(arg1)
    answeruser_close = answeruser.close_sqlite()

if __name__ == "__main__":
    __main__ #?

