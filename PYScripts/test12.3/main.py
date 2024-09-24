import unittest as ut
import runner_and_tournament as tourne

class RunnerTest(ut.TestCase):
    is_frozen = False
    def TestSkipping(flag):
        def deco(f):
            def wrapper(self):
                if flag:
                    self.skipTest('Тесты в этом кейсе заморожены')
                else:
                    f(self)
            return wrapper
        return deco

    @TestSkipping(is_frozen)
    def test_Walk(self):
        run1 = tourne.Runner("Bolt")
        for _ in range(10):
           run1.walk()
        self.assertEqual(run1.distance,50)

    @TestSkipping(is_frozen)
    def test_Run(self):
        run2 = tourne.Runner("Phil")
        for _ in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)

    @TestSkipping(is_frozen)
    def test_Challenge(self):
        run3 = tourne.Runner("Blontie")
        run4 = tourne.Runner("Sonic")
        for _ in range(10):
            run3.walk()
            run4.run()
        self.assertNotEqual(run3.distance,run4.distance)

class TournamentTest(ut.TestCase):
    is_frozen = True
    def TestSkipping(flag):
        def deco(f):
            def wrapper(self):
                if flag:
                    self.skipTest('Тесты в этом кейсе заморожены')
                else:
                    f(self)
            return wrapper
        return deco

    @classmethod
    def setUpClass(cls):
        cls.all_results = []


    def setUp(self):
        self.run1 = tourne.Runner("Usain",10)
        self.run2 = tourne.Runner("Andrei",9)
        self.run3 = tourne.Runner("Nick",3)

    @TestSkipping(is_frozen)
    def test_1(self):
        tour = tourne.Tournament(100,self.run1,self.run3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")

    @TestSkipping(is_frozen)
    def test_2(self):
        tour = tourne.Tournament(100,self.run2,self.run3)
        result = tour.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")

    @TestSkipping(is_frozen)
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
    suite12_3.tsuiterun()