import unittest
from calculate_score import *

class TestCalculateScore(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(score_line("XXXXXXXXXXXX"), 300)
    def test_input_2(self):
        self.assertEqual(score_line("9-9-9-9-9-9-9-9-9-9-"), 90)
    def test_input_3(self):
        self.assertEqual(score_line("5/5/5/5/5/5/5/5/5/5/5"), 150)
    def test_input_4(self):
        self.assertEqual(score_line("X7/9-X-88/-6XXX81"), 167)
    def test_input_5(self):
        self.assertEqual(score_line("X734X-88/-6XX9-"), 133)

if __name__ == '__main__':
    unittest.main()
