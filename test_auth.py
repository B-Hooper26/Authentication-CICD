#UNIT TEST
import unittest
from auth_right import authentication

class TestAUth(unittest.TestCase):

    def test_valid_credentials(self):
        self.assertTrue(authentication("Admin", "Password123"))
        
    def test_invalid_credentials(self):
        self.assertFalse(authentication("user", "123"))

