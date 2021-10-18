class Team:
    def __init__(self, team_name, players_names, coach_name):
        self.name = team_name
        self.players = players_names
        self.coach = coach_name

    def add_player(self, new_player):
        self.players.append(new_player)
