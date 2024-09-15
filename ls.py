import tor
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.first = tor.Runner('Усэйн', 10)
        self.second = tor.Runner('Андрей', 9)
        self.third = tor.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for x, all_value in self.all_results.items():
            slovar = {}
            for key, value in all_value.items():
                znach = {key: value.name}
                slovar.update(znach)
            print(slovar)

    def test_1(self):
        dist = tor.Tournament(90, self.first, self.third)
        self.distance = dist.start()
        self.all_results['Первый забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)],'Ник')

    def test_2(self):
        dist = tor.Tournament(90, self.second, self.third)
        self.distance = dist.start()
        self.all_results['Второй забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')
        
    def test_3(self):
        dist = tor.Tournament(90, self.first, self.second, self.third)
        self.distance = dist.start()
        self.all_results['Третий забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)],'Ник')