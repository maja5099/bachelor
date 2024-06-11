import unittest
from unittest.mock import patch, MagicMock
from bottle import request
from routers.signup import signup

class TestSignup(unittest.TestCase):

    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    @patch('routers.signup.bcrypt.gensalt')
    @patch('routers.signup.bcrypt.hashpw')
    @patch('routers.signup.uuid.uuid4')
    @patch('routers.signup.time.time')
    def test_signup_successful(self, mock_uuid, mock_time, mock_hashpw, mock_gensalt, mock_db, mock_load_dotenv):
        mock_uuid.hex.return_value = 'user_id'
        mock_time.return_value = 12345
        mock_hashpw.return_value = b'hashedpassword'
        mock_gensalt.return_value = b'salt'

        request_data = {
            "email": "test@example.com",
            "phone": "123456789",
            "username": "testuser",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe",
            "website_name": "My Website",
            "website_url": "https://example.com"
        }

        request_mock = MagicMock()
        request_mock.forms.get.side_effect = request_data.get
        with patch('routers.signup.request', request_mock):
            response = signup()

        mock_db.assert_called()
        mock_db.return_value.execute.assert_called()
        mock_db.return_value.commit.assert_called()
        self.assertEqual(response, {'message': 'signup successful'})

    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    def test_signup_email_exists(self, mock_db, mock_load_dotenv):
        mock_db.return_value.execute.return_value.fetchone.return_value = True

        request_mock = MagicMock()
        request_mock.forms.get.return_value = "test@example.com"
        with patch('routers.signup.request', request_mock):
            response = signup()

        mock_db.assert_called()
        mock_db.return_value.execute.assert_called()
        mock_db.return_value.commit.assert_not_called()
        self.assertEqual(response, {'error': 'Den indtastede email eksisterer allerede.'})

    
    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    def test_signup_phone_exists(self, mock_db, mock_load_dotenv):
        # Simulating a request with a phone number that already exists
        request_mock = MagicMock()
        request_mock.forms.get.return_value = None  # Replace with phone number that already exists in the database
        with patch('routers.signup.request', request_mock):
            # Calling the signup function
            response = signup()

        # Asserting that db.execute() was called to check for existing phone number
        mock_db.assert_called()
        mock_db.return_value.execute.assert_called()
        # Asserting that db.commit() was not called, as no changes were made
        mock_db.return_value.commit.assert_not_called()
        # Asserting the response
        self.assertEqual(response, {'error': 'Det indtastede telefonnummer eksisterer allerede.'})
    
    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    def test_signup_username_exists(self, mock_db, mock_load_dotenv):
        # Simulating a request with a username that already exists
        request_mock = MagicMock()
        request_mock.forms.get.return_value = None  # Replace with username that already exists in the database
        with patch('routers.signup.request', request_mock):
            # Calling the signup function
            response = signup()

        # Asserting that db.execute() was called to check for existing username
        mock_db.assert_called()
        mock_db.return_value.execute.assert_called()
        # Asserting that db.commit() was not called, as no changes were made
        mock_db.return_value.commit.assert_not_called()
        # Asserting the response
        self.assertEqual(response, {'error': 'Det indtastede brugernavn eksisterer allerede.'})

    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    def test_signup_password_invalid(self, mock_db, mock_load_dotenv):
        # Simulating a request with an invalid password (e.g., too short)
        request_mock = MagicMock()
        request_mock.forms.get.return_value = None  # Replace with an invalid password
        with patch('routers.signup.request', request_mock):
            # Calling the signup function
            response = signup()

        # Asserting that db.execute() was not called, as no user creation was attempted
        mock_db.assert_not_called()
        # Asserting the response
        self.assertEqual(response, {'error': 'Adgangskoden skal være på mindst 8 tegn.'})



    @patch('routers.signup.load_dotenv')
    @patch('routers.signup.master.db')
    def test_signup_exception(self, mock_db, mock_load_dotenv):
        mock_db.return_value.execute.side_effect = Exception('Database error')

        request_mock = MagicMock()
        with patch('routers.signup.request', request_mock):
            response = signup()

        mock_db.assert_called()
        mock_db.return_value.execute.assert_called()
        mock_db.return_value.rollback.assert_called()
        self.assertEqual(response, {'error': 'Internal Server Error'})

if __name__ == '__main__':
    unittest.main()