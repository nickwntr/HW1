import unittest as ut
import rt_with_exceptions as tourne
import logging
logging.basicConfig(level=logging.DEBUG, filemode="w",filename="info.log",
                        format="%(levelname)s : %(message)s at %(asctime)s", encoding="utf-8",force=True)
class RunnerTest(ut.TestCase):

    def test_Walk(self):
        try:
            logging.info("test_Walk выполнен успешно")
            run1 = tourne.Runner("Bolt",speed=-99)
            for _ in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 140)
        except Exception as ex:
            logging.warning(ex)

    def test_Run(self):
        try:
            logging.info("test_Run выполнен успешно")
            run2 = tourne.Runner(speed=11)
            for _ in range(10):
                run2.run()
            self.assertEqual(run2.distance, 220)
        except Exception as ex:
            logging.warning(ex)

    def test_Challenge(self):
        run3 = tourne.Runner("Blontie")
        run4 = tourne.Runner("Sonic")
        for _ in range(10):
            run3.walk()
            run4.run()
        self.assertNotEqual(run3.distance,run4.distance)


if __name__ == "__main__":
    unittest.main()