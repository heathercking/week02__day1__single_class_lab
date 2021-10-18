class Team:
    def __init__(self, team_name, players_names, coach_name):
        self.name = team_name
        self.players = players_names
        self.coach = coach_name
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        # if self.players.count(player_name) > 0:
        #     return True
        # else:
        #     return False

        if player_name in self.players:
            return True
        else:
            return False
   
    def play_game(self, has_won):
        if has_won == True:
            self.points = 3
        else:
            self.points = 0
        

    
