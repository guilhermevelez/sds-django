import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/buildings.csv')


def run_csv():
    buildings = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                buildings.append({
                    'name': row[0].strip()
                })

    csv_file.close()
    return buildings
