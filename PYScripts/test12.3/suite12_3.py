import main
import unittest


tSuite = unittest.TestSuite()
tSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(main.RunnerTest))
tSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(main.TournamentTest))

TTR = unittest.TextTestRunner(verbosity=2)
TTR.run(tSuite)