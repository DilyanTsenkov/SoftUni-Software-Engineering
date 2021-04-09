from project.player.player import Player


class Advanced(Player):
    h_points = 250

    def __init__(self, username: str):
        super().__init__(username, self.h_points)

