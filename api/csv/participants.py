import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/participants.csv')


def run_csv():
    participants = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                activities = row[3].strip().split(';')

                participants.append({
                    'name': row[0].strip(),
                    'email': row[1].strip(),
                    'internal_id': row[2].strip(),
                    'activities': [act.strip() for act in activities]
                })

    csv_file.close()
    return participants
