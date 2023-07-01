# https://docs.python.org/3/library/json.html

import json


example_dict = {
    # dictionary of data to be converted to json file
    'Teams': [{
        'Name': 'Man Utd',
        'Place': 3,
        'Players': 23
        },
        {
        'Name': 'Man City',
        'Place': 1,
        'Players': 25
        },
        {
        'Name': 'Arsenal',
        'Place': 2,
        'Players': 22
        },
        {
        'Name': 'Newcastle',
        'Place': 4,
        'Players': 26
        }
    ]
}

# json_string set equal to json file containing data
# indent keyword for formatting, see doc for more info
json_string = json.dumps(example_dict, indent=2)

# open file in write only mode and write json data
with open('soccerData.json', 'w') as file:
    file.write(json_string)
