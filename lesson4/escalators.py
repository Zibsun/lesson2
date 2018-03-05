import json
import operator
from datetime import datetime

data = json.load(open('data-397-2018-02-27.json', encoding="cp1251"))

now = datetime.today()
for station in data:
    for rep in station["RepairOfEscalators"]:
        if (len(rep))>0:
            rep_dates = rep["RepairOfEscalators"].split('-')
            begin = datetime.strptime(rep_dates[0], "%d.%m.%Y")
            end = datetime.strptime(rep_dates[1], "%d.%m.%Y")
            if now >= begin and now <= end:
                print ("Station {} repairs escalators from {} to {}".format(
                	station["NameOfStation"], begin.strftime("%d.%m.%Y"), end.strftime("%d.%m.%Y")))