from project.card.card import Card


class MagicCard(Card):
    d_points = 5
    h_points = 80

    def __init__(self, name: str):
        super().__init__(name, self.d_points, self.h_points)
