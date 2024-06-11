import unittest
from webtest import TestApp as WebTestApp
from app import application


##############################
#   SET UP
class TestSetUp(unittest.TestCase):
    def setUp(self):
        self.app = WebTestApp(application)


##############################
#   TEST APP ROUTES
class TestAppRoutes(TestSetUp):
    
    # Index
    def test_index_route(self):
        self.assert_route('/', 'UNID Studio')

    # About us
    def test_about_us_route(self):
        self.assert_route('/about_us', 'Om UNID Studio')

    # Contact
    def test_contact_route(self):
        self.assert_route('/contact', 'Kontakt')

    # Login
    def test_login_route(self):
        self.assert_route('/login', 'Log ind')

    # Portfolio
    def test_portfolio_route(self):
        self.assert_route('/portfolio', 'Case portfolio')

    # Services and prices
    def test_services_and_prices_route(self):
        self.assert_route('/services_and_prices', 'Services og priser')

    # Signup
    def test_signup_route(self):
        self.assert_route('/signup', 'Opret bruger')

    # Check routes
    def assert_route(self, route, content):
        response = self.app.get(route)
        self.assertEqual(response.status_code, 200)
        self.assertIn(content, response.text)