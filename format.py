import json
import csv

# Opening JSON file
data = {}
students = list()
head = ["Company", "City", "IndustryDomain", "stipend", "Tags",
        "Proj1", "Proj2", "Proj3", "Proj4", "Proj5", "Proj6", "Proj7"]
students.append(head)
FILE_PATH = "strings.json"
with open(FILE_PATH) as json_file:
    data = json.load(json_file)

for i in data:
    temp = list()
    temp.append(i["CompanyName"])
    temp.append(i["City"])
    if(i["IndustryDomain"]):
        temp.append(i["IndustryDomain"])
    else:
        temp.append('-')
    for j in i["projs"]:
        if(j["BatchName"] == "2020-2021 / SEM-I"):
            try:
                temp.append(j["stipend"])
            except:
                temp.append("-")
            try:
                temp.append(j["Tags"])
            except:
                temp.append("-")

            for proj in j["details"]:
                try:
                    temp.append(
                        proj["projectTitle"]+" -> "+proj["PBDescription"] + " >>>SKILLS<<< = " + proj["SKills"])
                except:
                    try:
                        temp.append(proj["projectTitle"])
                    except:
                        temp.append("-")
    students.append(temp)
print(students)

with open("DropTopBoy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
