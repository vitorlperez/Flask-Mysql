#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_list(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_hello(self):
        rv = self.app.get('/create/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
