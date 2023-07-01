import json

# open json file in read only mode, save into json_object
with open('soccerData.json', 'r') as file:
    json_object = json.loads(file.read())

# Now json file converted to dictionary, we cna work with the data
print(json_object['Teams'][0])