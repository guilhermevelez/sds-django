import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/members.csv')


def run_csv():
    members = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                members.append({
                    'name': row[0].strip(),
                    'email': row[1].strip(),
                    'phone': row[2].strip(),
                    'department_name': row[3].strip()
                })

    csv_file.close()
    return members
