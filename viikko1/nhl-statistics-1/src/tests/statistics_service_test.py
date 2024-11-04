import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

        self.players = PlayerReaderStub().get_players()

    def test_search_player(self):
        player = self.stats.search('Kurri')

        self.assertAlmostEqual(str(self.players[2]), str(player))

    def test_search_player_not_found(self):
        player = self.stats.search('Pasi')

        self.assertIsNone(player)

    def test_get_team(self):
        edm = self.stats.team('EDM')
        edm_players = [self.players[0], self.players[2], self.players[4]]

        self.assertAlmostEqual([str(p) for p in edm], [str(p)
                               for p in edm_players])

    def test_top(self):
        top_player = self.stats.top(1)

        self.assertAlmostEqual(str(top_player[0]), str(self.players[4]))
