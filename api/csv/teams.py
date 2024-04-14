import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/teams.csv')


def run_csv():
    teams = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                teams.append({
                    'title': row[0].strip(),
                    'description': row[1].strip(),
                    'coordinator_name': row[2].strip(),
                })

    csv_file.close()
    return teams
