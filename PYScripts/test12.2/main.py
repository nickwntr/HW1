import unittest as ut
import runner_and_tournament as tourne

class TournamentTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = tourne.Runner("Usain",10)
        self.run2 = tourne.Runner("Andrei",9)
        self.run3 = tourne.Runner("Nick",3)

    def test_1(self):
        tour = tourne.Tournament(100,self.run1,self.run3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")
    def test_2(self):
        tour = tourne.Tournament(100,self.run2,self.run3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")
    def test_3(self):
        tour = tourne.Tournament(100,self.run1,self.run2, self.run3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(result[3] == "Nick")

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print(res)


if __name__ == "__main__":
    ut.main()
