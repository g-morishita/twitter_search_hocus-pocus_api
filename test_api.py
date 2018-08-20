import unittest, requests
from api import api
from flask.json import loads

class TestSearchAPI(unittest.TestCase):
    def test_getByHashtags(self):
        res = requests.get('http://localhost:5000/hashtags/Avengers')
        self.assertEqual(type(loads(res.text)), list)

    def test_getByUser(self):
        res = requests.get('http://localhost:5000/users/__konankun')
        self.assertEqual(type(loads(res.text)), list)

if __name__ == '__main__':
   unittest.main()
