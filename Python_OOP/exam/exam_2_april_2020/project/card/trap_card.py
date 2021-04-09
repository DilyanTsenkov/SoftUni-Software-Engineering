from project.card.card import Card


class TrapCard(Card):
    d_points = 120
    h_points = 5

    def __init__(self, name: str):
        super().__init__(name, self.d_points, self.h_points)
