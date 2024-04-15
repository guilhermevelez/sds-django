import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))

def run_csv(date_num):
    filename = os.path.join(workpath, 'csv_files/preregisters%d.csv' % date_num)
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
                    'name': row[1].strip(),
                    'email': row[2].strip(),
                    'activity_titles': [act.strip() for act in activities]
                })

    csv_file.close()
    return participants
