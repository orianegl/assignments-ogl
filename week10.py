import csv
from collections import Counter

with open('popupdb.csv', newline='') as csvfile:
    scamreader = csv.DictReader(csvfile)
    country_counter = Counter()
    for scam in scamreader:
        p = scam["Number"]
        country = p[:p.find("-")]
        country_counter[country]+=1

print(country_counter.most_common(10))



import json

class student:
    def __init__(self, name, age, activities):
        self.name = name
        self.age = age 
        self.courses = courses
        self.activities = activities
    
student = student(
    name="Emmy",
    age=16,
    courses={"Art History"},
    activities=["One Direction"]
)

student = student(
    name="Amna",
    age=16,
    courses={"Religious Studies"},
    activities=["Poetry"]
)

student = student(
    name="Gramond",
    age=16,
    courses={"History"},
    activities=["Football"]
)

student = student(
    name="Kristin",
    age=16,
    courses={"Music"},
    activities=["Cuddly toys"]
)

student_dict = student.to_dict()

with open("student_data.json", "w") as json_file:
    json.dump(student_dict, json_file, indent=4)

print("Student data has been saved to 'student_data.json'")

