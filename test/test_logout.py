import unittest
from unittest.mock import MagicMock, patch
from routers.logout import logout
import os

class TestLogout(unittest.TestCase):
    @patch("routers.logout.request")
    @patch("routers.logout.master.db")
    @patch("routers.logout.redirect")
    def test_logout_success(self, mock_redirect, mock_db, mock_request):
        # Mocking request.get_cookie() return value
        mock_request.get_cookie.return_value = {'username': 'test_user'}
        
        # Mocking db.execute().fetchone() return value
        mock_db.return_value.execute.return_value.fetchone.return_value = {'username': 'test_user'}
        
        # Mocking response.delete_cookie()
        mock_response = MagicMock()
        mock_redirect.return_value = mock_response
        
        # Call the logout function
        logout()
        
        # Assertions
        mock_redirect.assert_called_once_with("/")
        mock_response.delete_cookie.assert_called_once_with("user")
        mock_db.assert_called_once()
        mock_db.return_value.execute.assert_called_once_with("SELECT * FROM users WHERE username = ?", ('test_user',))
        mock_request.get_cookie.assert_called_once_with("user", secret=os.getenv("MY_SECRET"))





    
    @patch("routers.logout.request")
    @patch("routers.logout.master.db")
    @patch("routers.logout.logger")
    @patch("routers.logout.redirect")
    def test_logout_no_cookie(self, mock_redirect, mock_logger, mock_db, mock_request):
        # Mocking request.get_cookie() return value
        mock_request.get_cookie.return_value = None
        
        # Call the logout function
        logout()
        
        # Assertions
        mock_logger.info.assert_any_call("No user cookie found, no user to logout")
        mock_redirect.assert_called_once_with("/")
        mock_db.assert_not_called()


