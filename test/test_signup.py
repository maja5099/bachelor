import unittest
from unittest.mock import patch, MagicMock
from bottle import response
from routers.signup import signup

class TestSignup(unittest.TestCase):

    @patch('routers.signup.master')
    @patch('routers.signup.request')
    @patch('routers.signup.load_dotenv')
    def test_signup_success(self, mock_load_dotenv, mock_request, mock_master):
        mock_load_dotenv.return_value = None
        mock_master.validate_email.return_value = None
        mock_master.validate_phone.return_value = None
        mock_master.validate_username.return_value = None
        mock_master.validate_password.return_value = None

        # Mock form data
        mock_request.forms.get.side_effect = [
            "test@example.com",  # email
            "12345678",           # phone
            "testuser",           # username
            "password",           # password
            "John",               # first_name
            "Doe",                # last_name
            "My Website",         # website_name
            "https://mywebsite.com"  # website_url
        ]

        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None  # Email does not exist

        mock_db = MagicMock()
        mock_db.__enter__.return_value.execute.return_value = mock_cursor

        mock_master.db.return_value = mock_db

        # Call the signup function
        response_data = signup()

        # Assert that the response data contains the expected success message
        self.assertEqual(response_data, {"message": "signup successful"})


    @patch('routers.signup.master')
    @patch('routers.signup.request')
    @patch('routers.signup.load_dotenv')
    def test_signup_existing_email(self, mock_load_dotenv, mock_request, mock_master):
        mock_master.validate_email.return_value = None 
        mock_master.validate_phone.return_value = None 
        mock_master.validate_username.return_value = None 
        mock_master.validate_password.return_value = None 

        mock_request.forms.get.side_effect = [
            "existingemail@example.com", "12345678", "newuser", "password",
            "John", "Doe", "", ""
        ]

        mock_cursor = MagicMock()
        mock_cursor.fetchone.side_effect = [{"email": "existingemail@example.com"}, None, None]  # Email exists

        mock_db = MagicMock()
        mock_db.__enter__.return_value.execute.return_value = mock_cursor

        mock_master.db.return_value = mock_db

        response_data = signup()

        self.assertEqual(response_data, {"error": "Den indtastede email eksisterer allerede."})

    @patch('routers.signup.master')
    @patch('routers.signup.request')
    @patch('routers.signup.load_dotenv')
    def test_signup_validation_errors(self, mock_load_dotenv, mock_request, mock_master):
        mock_master.validate_email.return_value = "Invalid email format"
        mock_master.validate_phone.return_value = "Invalid phone format"
        mock_master.validate_username.return_value = None 
        mock_master.validate_password.return_value = None 

        mock_request.forms.get.side_effect = [
            "invalidemail@", "12345678", "testuser", "securepassword",
            "John", "Doe", "My Website", "https://mywebsite.com"
        ]

        response_data = signup()

        self.assertEqual(response_data, {"error": "Invalid email format"})

    @patch('routers.signup.master')
    @patch('routers.signup.request')
    @patch('routers.signup.load_dotenv')
    def test_signup_exception_handling(self, mock_load_dotenv, mock_request, mock_master):
        mock_master.validate_email.return_value = None
        mock_master.validate_phone.return_value = None
        mock_master.validate_username.return_value = None
        mock_master.validate_password.return_value = None

        mock_master.db.side_effect = Exception("DB Connection Failed")
        mock_master.db.return_value.side_effect = Exception("DB Connection Failed")
        
        # Call the signup function
        response_data = signup()

        # Assert that the response data contains the expected error message
        self.assertEqual(response_data, {"error": "Internal Server Error"})

if __name__ == '__main__':
    unittest.main()
