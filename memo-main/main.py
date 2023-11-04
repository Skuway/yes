from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication


app = QApplication([])
from main_widnow import*
from menu_window import*


class Questions:
    def __init__(self,question, answer, wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask =+ 1
        self.count_right =+ 1
    def got_wrong(self):
        self.count_ask =+ 1
q1 = Questions("Яблуко","apple","banana","aple","ople")
q2 = Questions("Автобус","bus","troleubas","autobus","boat")
q3 = Questions("Пиво","beer","bear","fox","vine")
q4 = Questions("Ноутбук","laptop","notebook","draw","pelikan")     




radio_buttons = [rb_ans1,rb_ans2,rb_ans3,rb_ans4]
questions = [q1,q2,q3,q4]



def new_questions():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q,questions)
    lb_right_answer.setText(cur_q,gb_answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q,lb_wrong_ans1)
    radio_buttons[1].setText(cur_q,lb_wrong_ans2)
    radio_buttons[2].setText(cur_q,lb_wrong_ans3)
    radio_buttons[3].setText(cur_q.answer)


    new_questions()


def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText("Вірно!")
                answer.setChecked(False)
                break
    else:
        lb_result.setText("Не вірно")
        cur_q.got_wrong     

def click_ok():
    if btn_next.text() =="Відповісти":
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText("Наступне запитання")
    else:
        new_questions()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText("Відповісти")
        

btn_next.clicked.connect(click_ok)


def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show

btn_rest.clicked.connect(rest)


def menu_gen():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_ask/cur_q.count_right) * 100
    text =  f'Разів відповіли: {cur_q.count_ask}\n' \
            f'Вірних відповідей: {cur_q.count_right}\n' \
            f'Успішність:{round(c, 2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    window.hide()


    btn_menu.clicked.connect(menu_gen)



    def back_menu():
        menu_win.hide()
        window.show()

        btn_back.clicked.connect(back_menu)
                                 
                                 
                                 
                                 
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()                                
btn_clear.clicked.connect(clear)
                                 

def add_question():
    new_q = Questions(le_question.text(), le_right_ans.text(),
                    le_wrong_ans1.text(), le_wrong_ans2.text(),
                    le_wrong_ans3.text())


    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)

window.show()
app.exec()                                 