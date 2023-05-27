"""
Test validate parentheses.
"""

from unittest import TestCase
from problems.validate_parentheses import Solution


class TestValidateParentheses(TestCase):

    def test_1(self):
        """Test 1"""
        input_string = "(){}[]"
        result = Solution.validate_parentheses(input_string)
        self.assertTrue(result)

    def test_2(self):
        """Test 2"""
        input_string = "()"
        result = Solution.validate_parentheses(input_string)
        self.assertTrue(result)

    def test_3(self):
        """Test 2"""
        input_string = "(]"
        result = Solution.validate_parentheses(input_string)
        self.assertFalse(result)
