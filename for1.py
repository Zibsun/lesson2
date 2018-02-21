import random

l = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

irritating_questions = ["как дела?", "что нового?", "че там?", "ты как?", "как жизнь молодая?"]

def find_person(name, names):
    for i in names:
        if i == name:
         print ("Нашлось")


def ask_user():
    try:
        while True:
            answer = input(random.choice(irritating_questions) + " ")
            if answer.lower() == "хорошо":
                break
    except KeyboardInterrupt:
        print ("\nПока")



find_person("Маш", l)

ask_user()