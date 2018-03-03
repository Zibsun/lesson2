import csv

questions = {"как дела?": "хорошо", "что нового?": "ничего", "че там?": "как-то так", "ты как?": "норм"}

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for question, answer in questions.items():
        row = {"question": question, "answer": answer}
        writer.writerow(row)