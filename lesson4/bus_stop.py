from collections import Counter
import json
data = json.load(open('data-398-2018-02-13.json', encoding="cp1251"))

print("Количество остановок = {}".format(len(data)))


cnt = Counter()

for i in data:
    cnt[i["Street"]] += 1

print ("Улицы с наибольшим числом остановок:")
for street, number in cnt.most_common(10):
    print ('На улице "{}" {} остановок'.format(street,number))