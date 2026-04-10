import unittest
from age import categorize_by_age

class TestCategorizeByAgeSubtests(unittest.TestCase):

    def test_adult_category(self):
        """Tests all valid ages in the Adult category (19-65)."""
        for age in range(19, 66):  # 19..65 inclusive
            with self.subTest(age=age):
                # print a line for each subtest to match the example output style
                print(f"{age} is considered as an adult.")
                self.assertEqual(categorize_by_age(age), "Adult")

if __name__ == "__main__":
    unittest.main(verbosity=2)
