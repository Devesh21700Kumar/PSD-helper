import json
import csv

# Opening JSON file
data = {}
students = list()
head = ["Company", "Domain", "Seats", "Skills", "More Tech"]
students.append(head)
with open("strings.json") as json_file:
    data = json.load(json_file)

for i in data:
    temp = list()
    temp.append(i["CompanyName"])
    if(i["IndustryDomain"]):
        temp.append(i["IndustryDomain"])
    else:
        temp.append('-')
    seat = 0
    for j in i["projs"]:
        skill = list()
        skill1 = list()
        if(j["BatchName"] == "2020-2021 / SEM-I"):
            for proj in j["details"]:
                try:
                    seat += proj['TotalReqdStudents']
                except:
                    pass
                try:
                    skill.append(proj["SKills"])
                except:
                    pass
                try:
                    skill1.append(proj["Broad"])
                except:
                    pass
        temp.append(seat)
        if(len(skill)):
            temp.append(skill)
        else:
            temp.append("-")
        if(len(skill1)):
            temp.append(skill1)
        else:
            temp.append("-")
    if(len(temp) > 2):
        students.append(temp)
print(students)

with open("skills.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
