from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError('Player cannot be an empty string!')
        remove = self.find(player)
        self.players.remove(remove)
        self.count -= 1

    def find(self, username: str):
        return [p for p in self.players if p.username == username][0]
