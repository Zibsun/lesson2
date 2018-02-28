import csv

questions = {"как дела?": "хорошо", "что нового?": "ничего", "че там?": "как-то так", "ты как?": "норм"}

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for question in questions:
        row = {"question": question, "answer": questions[question]}
        writer.writerow(row)