import unittest
from Password import Password as p

class TestPassword(unittest.TestCase):
    def test_check_complexity(self):
        self.assertTrue(p.check_complexity(True, "1Pp4ssw0rdD"))
        self.assertNotEqual(p.check_complexity(False, "password"), True)    

if __name__ == '__main__':
    unittest.main()