import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(workpath, 'csv_files/functions.csv')


class FunctionCSV:
    def __init__(self, title, description, spaces, people, vols, obs):
        self.title = title
        self.description = description
        self.spaces = self.filter_spaces(spaces)
        self.vols = int(vols)
        self.obs = obs

        p = self.filter_people(people)
        self.people_min = p[0]
        self.people_max = p[int(len(p) > 1)]

    def filter_people(self, people):
        if " a " in people:
            return [int(p) for p in people.split(' a ')]
        
        return [int(people)]
        

    def filter_spaces(self, spaces_str):
        if "," in spaces_str:
            spaces = [s.strip() for s in spaces_str.split(',')]
            spaces.sort()
            return spaces
        
        if " e " in spaces_str:
            spaces = [s.strip() for s in spaces_str.split(' e ')]
            spaces.sort()
            return spaces
        
        return [spaces_str.strip()]


def run_csv():
    functions = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                title = row[0].strip()
                description = row[1].strip()
                spaces = row[2].strip()
                people = row[3].strip()
                vols = row[4].strip()
                #deps_needed = row[5]
                #deps_pref = row[6]
                obs = row[7].strip()

                function = FunctionCSV(title, description, spaces, people, vols, obs)

                functions.append({
                    'title': function.title,
                    'description': function.description,
                    'spaces': function.spaces,
                    'members_needed_min': function.people_min,
                    'members_needed_max': function.people_max,
                    'vols_needed': function.vols,
                    'obs': function.obs,
                    'spaces': function.spaces
                })

    csv_file.close()
    return functions