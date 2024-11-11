class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        national_players = list(filter(
            lambda p: p.nationality == nationality, self.players))

        national_players.sort(
            key=lambda p: p.goals + p.assists, reverse=True)

        return national_players

    def get_nationalities(self):
        nationalities = list(set([p.nationality for p in self.players]))
        return nationalities
