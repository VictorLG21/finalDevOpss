import unittest
from main import create_user

class MyTest(unittest.TestCase):

    def test_insert_record(self):
        
        resposta = create_user("Victor","victorgaspar1@hotmail.com")
        self.assertFalse(resposta["id"])