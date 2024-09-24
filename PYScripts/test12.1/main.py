import unittest
import runner
import threading

class RunnerTest(unittest.TestCase):
    def test_Walk(self):
        run1 = runner.Runner("Bolt")
        for _ in range(10):
           run1.walk()
        self.assertEqual(run1.distance,50)


    def test_Run(self):
        run2 = runner.Runner("Phil")
        for _ in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100)


    def test_Challenge(self):
        run3 = runner.Runner("Blontie")
        run4 = runner.Runner("Sonic")
        for _ in range(10):
            run3.walk()
            run4.run()
        self.assertNotEqual(run3.distance,run4.distance)




if __name__ =="__main__":
    unittest.main()