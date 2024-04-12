import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/departments.csv')


def run_csv():
    departments = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                departments.append({
                    'short_name': row[0].strip(),
                    'long_name': row[1].strip()
                })

    csv_file.close()
    return departments
