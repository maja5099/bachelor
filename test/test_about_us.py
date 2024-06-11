import unittest
from unittest.mock import patch, MagicMock
from webtest import TestApp
from bottle import request
from app import application

##############################
#   SET UP
class TestSetUp(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(application)

##############################
#   ABOUT_US.PY
class AboutUsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(application)
        self.page_name = "about_us"
        self.user_cookie = {"username": "test_user"}
        self.user = {"id": 1, "username": "test_user", "email": "test@example.com"}

    @patch("bottle.request.get_cookie")
    @patch("os.getenv")
    @patch("master.db")
    def test_about_us_with_valid_cookie(self, mock_db, mock_getenv, mock_get_cookie):
        mock_get_cookie.return_value = self.user_cookie
        mock_db.return_value.execute.return_value.fetchone.return_value = self.user
        mock_getenv.return_value = 'MY_SECRET'

        response = self.app.get("/about_us")

        mock_get_cookie.assert_called_once_with("user", secret='MY_SECRET')
        mock_db.assert_called_once()
        mock_db.return_value.execute.assert_called_once_with("SELECT * FROM users WHERE username = ? LIMIT 1", (self.user_cookie.get('username'),))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Om UNID Studio", response.body)
        self.assertIn(b"test_user", response.body)

    @patch("bottle.request.get_cookie")
    @patch("os.getenv")
    @patch("master.db")
    def test_about_us_with_invalid_cookie(self, mock_db, mock_getenv, mock_get_cookie):
        mock_get_cookie.return_value = None
        mock_getenv.return_value = 'MY_SECRET'

        response = self.app.get("/about_us")

        mock_get_cookie.assert_called_once_with("user", secret='MY_SECRET')
        mock_db.assert_not_called()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Om UNID Studio", response.body)
        self.assertNotIn(b"test_user", response.body)

if __name__ == "__main__":
    unittest.main()