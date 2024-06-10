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


##############################
#   ABOUT_US.PY
class TestAboutUs(TestSetUp):
    def setUp(self):
        import about_us
        self.app = WebTestApp(about_us)


##############################
#   CLIPCARDS.PY
class TestClipcards(TestSetUp):
    def setUp(self):
        import clipcards
        self.app = WebTestApp(clipcards)


##############################
#   CONTACT.PY
class TestContact(TestSetUp):
    def setUp(self):
        import contact
        self.app = WebTestApp(contact)


##############################
#   LOGIN.PY
class TestLogin(TestSetUp):
    def setUp(self):
        import login
        self.app = WebTestApp(login)


##############################
#   LOGOUT.PY
class TestLogout(TestSetUp):
    def setUp(self):
        import logout
        self.app = WebTestApp(logout)


##############################
#   MESSAGES.PY
class TestMessages(TestSetUp):
    def setUp(self):
        import messages
        self.app = WebTestApp(messages)


##############################
#   PAYMENT.PY
class TestPayment(TestSetUp):
    def setUp(self):
        import payment
        self.app = WebTestApp(payment)


##############################
#   PORTFOLIO.PY
class TestPortfolio(TestSetUp):
    def setUp(self):
        import portfolio
        self.app = WebTestApp(portfolio)


##############################
#   PROFILE.PY
class TestProfile(TestSetUp):
    def setUp(self):
        import profile # type: ignore
        self.app = WebTestApp(profile)


##############################
#   SERVICES_AND_PRICES.PY
class TestServicesAndPrices(TestSetUp):
    def setUp(self):
        import services_and_prices
        self.app = WebTestApp(services_and_prices)


##############################
#   SIGNUP.PY
class TestSignup(TestSetUp):
    def setUp(self):
        import signup
        self.app = WebTestApp(signup)


if __name__ == '__main__':
    unittest.main()