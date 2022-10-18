import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# type your code here
def parse_user(output_file, *input_files):
    unique_names = []
    unique_users = []
    for file in input_files:
        try:
            with open(file) as fil:
                data = json.load(fil)
                for dict in data:
                    if 'name' in dict.keys() and dict.get('name') not in unique_names:
                        unique_names.append(dict['name'])
                        unique_users.append(dict)
        except OSError:
            logging.error(f"File {file} doesn't exist")
    with open(output_file, 'w') as f:
        json.dump(unique_users, f, indent=4)
       
