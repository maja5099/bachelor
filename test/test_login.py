import unittest
from unittest.mock import patch, MagicMock
from routers.login import login


class TestLogin(unittest.TestCase):

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_successful(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        mock_db.return_value.execute.return_value.fetchone.return_value = {'username': 'testuser', 'password': 'hashedpassword'}
        mock_checkpw.return_value = True

        request_mock = MagicMock()
        request_mock.forms.get.return_value = 'password'
        with patch('routers.login.request', request_mock):
            response = login()

        mock_db.assert_called_once()
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), 'hashedpassword')
        mock_set_cookie_secure.assert_called_once_with("user", {'username': 'testuser'})
        self.assertEqual(response, {'info': 'login successful', 'redirect': '/'})

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_user_not_found(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        mock_db.return_value.execute.return_value.fetchone.return_value = None
        mock_checkpw.return_value = False

        request_mock = MagicMock()
        request_mock.forms.get.return_value = 'testuser'
        with patch('routers.login.request', request_mock):
            response = login()

        mock_db.assert_called_once()
        mock_set_cookie_secure.assert_not_called()
        mock_checkpw.assert_not_called()
        self.assertEqual(response, {'error': 'Brugernavnet eksisterer ikke'})

    @patch('routers.login.set_cookie_secure')
    @patch('routers.login.master.db')
    @patch('routers.login.bcrypt.checkpw')
    def test_login_wrong_password(self, mock_checkpw, mock_db, mock_set_cookie_secure):
        mock_db.return_value.execute.return_value.fetchone.return_value = {'username': 'testuser', 'password': 'hashedpassword'}
        mock_checkpw.return_value = False

        request_mock = MagicMock()
        request_mock.forms.get.return_value = 'password'
        with patch('routers.login.request', request_mock):
            response = login()

        mock_set_cookie_secure.assert_not_called()
        mock_db.assert_called_once()
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), 'hashedpassword')
        self.assertEqual(response, {'error': 'Adgangskoden er forkert'})

    @patch('routers.login.master.db')
    def test_login_exception(self, mock_db):
        mock_db.return_value.execute.side_effect = Exception('Database error')

        request_mock = MagicMock()
        with patch('routers.login.request', request_mock):
            with self.assertRaises(Exception) as cm:
                response = login()

        self.assertEqual(str(cm.exception), 'Database error')
  

if __name__ == '__main__':
    unittest.main()
