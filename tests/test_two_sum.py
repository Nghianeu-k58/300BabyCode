"""
Test two sum problems.
"""

from unittest import TestCase
from problems.two_sum import Solution


class TestTwoSum(TestCase):
    """Test problem two sum."""

    def test_two_sum_successful(self):
        """Test return as expected."""
        input_list = [2, 7, 11, 15]
        input_target = 9

        expected_output = [0, 1]
        expected_msg = "OK"

        func_out, msg = Solution.solution(input_list, target=input_target)

        self.assertEqual(expected_output, func_out)
        self.assertEqual(expected_msg, msg)

    def test_two_sum_failed(self):
        """Test return None and msg."""

        input_list = [2, 7, 11, 15]
        input_target = 100

        expected_msg = "Cannot find 2 numbers with input target"

        func_out, msg = Solution.solution(input_list, target=input_target)

        self.assertIsNone(func_out)
        self.assertEqual(expected_msg, msg)
