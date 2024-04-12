import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/activities.csv')


def run_csv():
    activities = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                activities.append({
                    'title': row[0].strip(),
                    'date_num': row[1].strip(),
                    'hour_start': row[2].strip(),
                    'hour_end': row[3].strip(),
                    'space_name': row[4].strip()
                })

    csv_file.close()
    return activities
