import unittest
from unittest.mock import patch, MagicMock
from routers.login import login

class TestLogin(unittest.TestCase):

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_successful(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        # Stubbing the database to return a user with a hashed password
        mock_db.return_value.execute.return_value.fetchone.return_value = {'username': 'testuser', 'password': 'hashedpassword'}
        # Stubbing checkpw to return True to simulate successful password verification
        mock_checkpw.return_value = True  

        # Create a MagicMock object to mimic the request
        request_mock = MagicMock()
        # Stubbing the forms.get method to return 'password' when called
        request_mock.forms.get.return_value = 'password'

        # Patching the request object so it returns our MagicMock object
        with patch('routers.login.request', request_mock):
            response = login()  # Calling login without passing request_mock explicitly

        mock_db.assert_called_once()
        # Check that checkpw was called with the expected arguments
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), 'hashedpassword')
        mock_set_cookie_secure.assert_called_once_with("user", {'username': 'testuser'})
        self.assertEqual(response, {'info': 'login successful', 'redirect': '/'})

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_user_not_found(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        mock_db.return_value.execute.return_value.fetchone.return_value = None
        mock_checkpw.return_value = False
        
        # Create a MagicMock object to mimic the request
        request_mock = MagicMock()
        # Stubbing the forms.get method to return 'testuser' when called
        request_mock.forms.get.return_value = 'testuser'

        # Patching the request object so it returns our MagicMock object
        with patch('routers.login.request', request_mock):
            response = login()  # Calling login without passing request_mock explicitly
        
        mock_db.assert_called_once()
        mock_set_cookie_secure.assert_not_called()
        mock_checkpw.assert_not_called()
        self.assertEqual(response, {'error': 'Brugernavnet eksisterer ikke'})

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_wrong_password(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        # Stubbing the database to return a user with a hashed password
        mock_db.return_value.execute.return_value.fetchone.return_value = {'username': 'testuser', 'password': 'hashedpassword'}
        # Stubbing checkpw to return False to simulate incorrect password
        mock_checkpw.return_value = False  
        
        # Create a MagicMock object to mimic the request
        request_mock = MagicMock()
        # Stubbing the forms.get method to return 'password' when called
        request_mock.forms.get.return_value = 'password'

        # Patching the request object so it returns our MagicMock object
        with patch('routers.login.request', request_mock):
            response = login()  # Calling login without passing request_mock explicitly

        mock_set_cookie_secure.assert_not_called()
        mock_db.assert_called_once()
        # Check that checkpw was called with the expected arguments
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), 'hashedpassword')
        self.assertEqual(response, {'error': 'Adgangskoden er forkert'})


    @patch('routers.login.master.db')
    def test_login_exception(self, mock_db):
        # Stubbing the database to raise an exception to simulate a database error
        mock_db.return_value.execute.side_effect = Exception('Database error')
        
        # Create a MagicMock object to mimic the request
        request_mock = MagicMock()

        # Patching the request object so it returns our MagicMock object
        with patch('routers.login.request', request_mock):
            # Passing the mock request object to the login function
            with self.assertRaises(Exception) as cm:
                response = login()
        
        # Asserting that the exception was raised with the expected message
        self.assertEqual(str(cm.exception), 'Database error')

if __name__ == '__main__':
    unittest.main()
