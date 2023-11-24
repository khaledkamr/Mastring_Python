# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------

import unittest

class testcase(unittest.TestCase):

    def test1(self):
        self.assertTrue(100 > 97, "should be true")

    def test2(self):
        self.assertEqual(40 + 60, 100, "should be 100")

    def test3(self):
        self.assertGreater(100, 80, "should be true")

if __name__ == "__main__":

    unittest.main()