import csv
import json

data = """id,name,department,salary
1,Олена,IT,3500.0
2,Іван,HR,1800.0
3,Марія,Finance,4200.0
4,Олег,IT,2100.0
5,Анна,Marketing,1500.0"""

with open('employees.csv', 'w', encoding='utf-8') as f:
    f.write(data)

def stream_high_earners(filepath: str, min_salary: float):
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if float(row['salary']) >= min_salary:
                yield row

high_earners = []

for employee in stream_high_earners('employees.csv', 2500.0):
    high_earners.append(employee)

with open('high_earners.json', 'w', encoding='utf-8') as f:
    json.dump(high_earners, f, indent=4, ensure_ascii=False)