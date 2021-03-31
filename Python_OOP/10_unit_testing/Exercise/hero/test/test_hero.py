import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    expected_username = "Test username"
    expected_health = 100.0
    expected_damage = 10.0
    expected_level = 5

    def setUp(self):
        self.test_hero = Hero(self.expected_username, self.expected_level, self.expected_health, self.expected_damage)

    def test_hero_init__when_correct_input__expect_be_initialized(self):
        self.assertEqual(self.expected_username, self.test_hero.username)
        self.assertEqual(self.expected_level, self.test_hero.level)
        self.assertEqual(self.expected_health, self.test_hero.health)
        self.assertEqual(self.expected_damage, self.test_hero.damage)

    def test_hero_username__expect_to_be_str(self):
        self.assertTrue(isinstance(self.test_hero.username, str))

    def test_hero_level__expect_to_be_int(self):
        self.assertTrue(isinstance(self.test_hero.level, int))

    def test_hero_health__expect_to_be_float(self):
        self.assertTrue(isinstance(self.test_hero.health, float))

    def test_hero_damage__expect_to_be_float(self):
        self.assertTrue(isinstance(self.test_hero.damage, float))

    def test_hero_str__expect_info(self):
        username = self.test_hero.username
        level = self.test_hero.level
        health = self.test_hero.health
        damage = self.test_hero.damage

        expect = f"Hero {username}: {level} lvl\n" \
                 f"Health: {health}\n" \
                 f"Damage: {damage}\n"
        current = self.test_hero.__str__()

        self.assertEqual(current, expect)

    def test_hero_battle__when_enemy_hero_is_same_as_hero_name__expect_exception(self):
        enemy_hero = Hero(self.expected_username, 12, 44, 6)
        with self.assertRaises(Exception) as context:
            self.test_hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle__when_health_is_0__expect_ValueError(self):
        enemy_hero = Hero("enemy_hero", 5, 44, 5)
        self.test_hero.health = 0.0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_health_is_below_0__expect_ValueError(self):
        enemy_hero = Hero("enemy_hero", 12, 44, 6)
        self.test_hero.health = -5.0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_enemy_hero_health_is_0__expect_ValueError(self):
        enemy_hero = Hero("enemy_hero", 12, 44, 6)
        enemy_hero.health = 0.0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_enemy_hero_health_is_below_0__expect_ValueError(self):
        enemy_hero = Hero("enemy_hero", 12, 44, 6)
        enemy_hero.health = -5.0
        with self.assertRaises(ValueError) as context:
            self.test_hero.battle(enemy_hero)
        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_hero_health_and_enemy_hero_health_is_zero__expect_to_return_draw(self):
        enemy_hero = Hero("enemy_hero", 20, 50.0, 5.0)
        expect_msg = "Draw"
        self.assertEqual(self.test_hero.battle(enemy_hero), expect_msg)

    def test_hero_battle__when_hero_health_and_enemy_hero_health_is_below_zero__expect_to_return_draw(self):
        enemy_hero = Hero("enemy_hero", 20, 30.0, 10.0)
        expect_msg = "Draw"
        self.assertEqual(self.test_hero.battle(enemy_hero), expect_msg)

    def test_hero_battle__when_enemy_hero_health_is_0__expect_to_return_you_win(self):
        enemy_hero = Hero("enemy_hero", 5, 50.0, 5.0)
        return_msg = self.test_hero.battle(enemy_hero)
        result = [self.test_hero.level, self.test_hero.health, self.test_hero.damage, return_msg]
        expected_result = [6, 80.0, 15.0, "You win"]
        self.assertEqual(expected_result, result)

    def test_hero_battle__when_enemy_hero_health_is_below_0__expect_to_return_you_win(self):
        enemy_hero = Hero("enemy_hero", 5, 40.0, 5.0)
        return_msg = self.test_hero.battle(enemy_hero)
        result = [self.test_hero.level, self.test_hero.health, self.test_hero.damage, return_msg]
        expected_result = [6, 80.0, 15.0, "You win"]
        self.assertEqual(expected_result, result)

    def test_hero_battle__when_test_hero_health_is_0__expect_to_return_you_lose(self):
        enemy_hero = Hero("enemy_hero", 20, 100.0, 10.0)
        return_msg = self.test_hero.battle(enemy_hero)
        result = [enemy_hero.level, enemy_hero.health, enemy_hero.damage, return_msg]
        expected_result = [21, 55.0, 15.0, "You lose"]
        self.assertEqual(expected_result, result)

    def test_hero_battle__when_test_hero_health_is_below_0__expect_to_return_you_lose(self):
        enemy_hero = Hero("enemy_hero", 20, 100.0, 10.0)
        return_msg = self.test_hero.battle(enemy_hero)
        result = [enemy_hero.level, enemy_hero.health, enemy_hero.damage, return_msg]
        expected_result = [21, 55.0, 15.0, "You lose"]
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
