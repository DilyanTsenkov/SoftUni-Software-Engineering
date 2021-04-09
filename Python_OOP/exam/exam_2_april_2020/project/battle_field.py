from project.player.player import Player
from project.player.beginner import Beginner


class BattleField:
    @staticmethod
    def if_player_is_beginner(player: Beginner):
        player.health += 40
        for c in player.card_repository.cards:
            c.damage_points += 30

    @staticmethod
    def bonus(player):
        attacker_bonus_health = 0
        for card in player.card_repository.cards:
            attacker_bonus_health += card.health_points
        return attacker_bonus_health

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        if isinstance(attacker, Beginner):
            self.if_player_is_beginner(attacker)
        if isinstance(enemy, Beginner):
            self.if_player_is_beginner(enemy)

        attacker.health += self.bonus(attacker)
        enemy.health += self.bonus(enemy)

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
