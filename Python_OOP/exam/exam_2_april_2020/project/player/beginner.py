from project.player.player import Player


class Beginner(Player):
    h_points = 50

    def __init__(self, username: str):
        super().__init__(username, self.h_points)


