import json

class Team:
    """
    Simple class that creates team objects which can then be converted into a json file.
    """

    def __init__(self, name, place, players):
        self.name = 'name'
        self.place = 'place'
        self.players = 'players'

    def print_date(self):
        """
        print object data
        """
        print(self.name, self.place, self.players)

    def dump_to_json(self, filename):
        """
        takes the location to which we will be dumping the data
        """
        # dictionary created to format the object data so it can be dumped
        team_dict = {'name': self.name, 'place': self.place, 'players': self.players}

        # open file in write only mode and dump the data
        with open(filename, 'w') as file:
            file.write(json.dumps(team_dict, indent=2))

    def load_from_json(self, filename):
        """
        takes the location from where the data will be loaded
        """

        # open file in read only mode in order to create new object with data provided
        with open(filename, 'r') as file:
            json_data = json.loads(filename.read())

            # set the object values to the values in from file
            self.name = json_data['name']
            self.place = json_data['place']
            self.players = json_data['players']