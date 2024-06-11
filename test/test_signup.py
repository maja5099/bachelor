import unittest
from unittest.mock import patch, MagicMock
from routers.signup import signup
from master import validate_email, validate_phone, validate_password, validate_username
 # Importer din signup-funktion fra din signup.py-fil

# Mock dependencies (erstat med dine faktiske implementeringer)
def mock_validate_email(email):
  return None  # Ingen valideringsfejl

def mock_validate_phone(phone):
  return None  # Ingen valideringsfejl

def mock_validate_username(username):
  return None  # Ingen valideringsfejl

def mock_validate_password(password):
  return None  # Ingen valideringsfejl

class TestSignup(unittest.TestCase):

  @patch('master.validate_email', side_effect=mock_validate_email)
  @patch('master.validate_phone', side_effect=mock_validate_phone)
  @patch('master.validate_username', side_effect=mock_validate_username)
  @patch('master.validate_password', side_effect=mock_validate_password)
  def test_signup_success(self, mock_validate_password, mock_validate_username, mock_validate_phone, mock_validate_email):
    # Mock request object
    mock_request = MagicMock()
    mock_request.forms.get.side_effect = {
      "email": "test@mail.com",
      "phone": "12345678",
      "username": "test_user",
      "password": "password123",
      "first_name": "John",
      "last_name": "Doe",
    }

    # Mock database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.execute.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None  # Ingen eksisterende bruger

    # Patch database related functions
    with patch('signup.master.db', return_value=mock_db):
      with patch('signup.request', mock_request):
        response = signup()

    # Bekræft succesfuld respons
    self.assertEqual(response.get('message'), 'signup successful')
    self.assertEqual(response.get('error'), None)
    self.assertEqual(mock_db.execute.call_count, 2)  # Én til brugerindtastning, én til potentielt personale

  def test_signup_existing_email(self):
    # Mock eksisterende bruger med samme e-mail
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.execute.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'email': 'test@mail.com'}

    with patch('signup.master.db', return_value=mock_db):
      response = signup()

    # Bekræft fejl for eksisterende e-mail
    self.assertEqual(response.get('message'), None)
    self.assertEqual(response.get('error'), 'Den indtastede email eksisterer allerede.')

  # Tilføj lignende testtilfælde for eksisterende telefonnummer og brugernavn

if __name__ == '__main__':
  unittest.main()
