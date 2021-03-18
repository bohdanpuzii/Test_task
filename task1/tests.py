import unittest
from main import slice_less

test_cases_raising_errors = [([1.2, 2.3, 3.3, 4.2, 4], 1),
                             ([1.2, 2.3, 3.3, 4.2, 4], 1.1),
                             ((1, 2, 3, 4, 5), 1)]
correct_test_cases = [([10, 15, 20, 30, -5], 15, [30, 20]),
                      ([10, 15, 20, 30, -5], -100, [30, 20, 15, 10, -5]),
                      ([10, 15, 20, 30, -5], 100, [])]


class TestSliceLess(unittest.TestCase):
    def test_error_catching(self):
        for input_list, less_value in test_cases_raising_errors:
            with self.assertRaises(TypeError):
                slice_less(input_list, less_value)

    def test_correct_performance(self):
        for input_list, less_value, expected_result in correct_test_cases:
            self.assertEqual(slice_less(input_list, less_value), expected_result)


if __name__ == '__main__':
    unittest.main()
