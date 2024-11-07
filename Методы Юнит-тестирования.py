import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем трех бегунов с разными скоростями
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов по очереди
        for result in cls.all_results.values():
            print(result)

    def test_tournament_usain_and_nick(self):
        # Создаем объект Tournament с двумя участниками
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        all_results = tournament.start()
        self.__class__.all_results[1] = {place: str(runner) for place, runner in all_results.items()}
        # Проверяем, что Ник финишировал последним
        self.assertTrue(all_results[max(all_results.keys())] == self.runner_nick)

    def test_tournament_andrey_and_nick(self):
        # Создаем объект Tournament с двумя участниками
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        all_results = tournament.start()
        self.__class__.all_results[2] = {place: str(runner) for place, runner in all_results.items()}
        # Проверяем, что Ник финишировал последним
        self.assertTrue(all_results[max(all_results.keys())] == self.runner_nick)

    def test_tournament_usain_andrey_and_nick(self):
        # Создаем объект Tournament с тремя участниками
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        all_results = tournament.start()
        self.__class__.all_results[3] = {place: str(runner) for place, runner in all_results.items()}
        # Проверяем, что Ник финишировал последним
        self.assertTrue(all_results[max(all_results.keys())] == self.runner_nick)


if __name__ == '__main__':
    unittest.main()
