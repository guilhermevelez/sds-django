import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/spaces.csv')


def run_csv():
    spaces = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                spaces.append({
                    'name': row[0].strip(),
                    'building_name': row[1].strip()
                })

    csv_file.close()
    return spaces
