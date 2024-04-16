"""Tests the login code for all possible outcomes & In addition the tests the query func."""

import unittest
import main
import mysql

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

class QueryTest(unittest.TestCase):

    def test_query_not_implemented(self):
        with self.assertRaises(UserWarning):
            mysql.query("SELECT * FROM users")

if __name__ == "__main__":
    unittest.main()
