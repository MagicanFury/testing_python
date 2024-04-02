"""Tests the login code for all possible outcomes."""

import unittest
import main

class LoginTest(unittest.TestCase):

    def test_login_correct(self):
        self.assertIsNotNone(main.login("ivan.auda@hva.nl", "pass123pass"))

    def test_login_correct_2(self):
        self.assertIsNotNone(main.login("ivan.auda@hva.nl", "pass123pass", "sha256"))

    def test_login_incorrect(self):
        self.assertIsNone(main.login("ivan.auda@hva.nl", "QWERTY1234567"))

    def test_login_error(self):
        with self.assertRaises(Exception):
            main.login("ivan.auda@hva.nl", "pass123pass", "sha128")

if __name__ == "__main__":
    unittest.main()