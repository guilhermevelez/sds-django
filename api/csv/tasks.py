import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))


def run_csv(date_num):
    filename = os.path.join(workpath, 'csv_files/tasks%d.csv' % date_num)
    tasks = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                tasks.append({
                    'function_title': row[0].strip(),
                    'hour_start': row[1].strip(),
                    'hour_end': row[2].strip(),
                    'space_name': row[3].strip(),
                    'member_name': row[4].strip(),
                })

    csv_file.close()
    return tasks
