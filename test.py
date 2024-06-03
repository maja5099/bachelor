import unittest
from webtest import TestApp as WebTestApp
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        from app import application
        self.app = WebTestApp(application)


    ##############################
    #   INDEX
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('UNID Studio', response.text)


    ##############################
    #   SIGNUP.PY
    def test_signup_get_route(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn('signup', response.text)


    ##############################
    #   LOGIN.PY
    def test_login_get_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('login', response.text)


    ##############################
    #   ERROR HANDLING TESTING
    #   404
    def test_error_handling_404(self):
        response = app.error404(type('Error', (object,), {'status_code': 404})())
        self.assertTrue(isinstance(response, str))
        self.assertIn('404', response)

    #   500
    def test_error_handling_500(self):
        response = app.error500(type('Error', (object,), {'status_code': 500})())
        self.assertTrue(isinstance(response, str))
        self.assertIn('500', response)


if __name__ == '__main__':
    unittest.main()