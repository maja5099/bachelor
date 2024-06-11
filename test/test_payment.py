import unittest
from unittest.mock import patch, MagicMock
from bottle import template

# Import the function from the correct module
from routers.payment import process_payment

class TestProcessPayment(unittest.TestCase):

    @patch('routers.payment.global_content', {'decorative_header_text': 'Test Header'})
    @patch('routers.payment.request')
    @patch('routers.payment.logger')
    @patch('routers.payment.get_current_user')
    @patch('routers.payment.master')
    def test_process_payment_success(self, mock_master, mock_get_current_user, mock_logger, mock_request, mock_global_content):
        # Mock the get_current_user to return a valid user
        mock_get_current_user.return_value = {'user_id': 'test_user_id'}

        # Mock the request forms
        mock_request.forms.get.side_effect = lambda key: {
            'clipcard_price': '100',
            'clipcard_type': 'test_clipcard_type'
        }[key]

        # Mock the database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_master.db.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Mock the database query results
        mock_cursor.fetchone.return_value = {'clipcard_type_id': 'test_clipcard_type_id', 'clipcard_type_time': 60}

        # Mock the template function to return a success message
        with patch('bottle.template', return_value="Payment confirmation") as mock_template:
            response = process_payment()

            # Check the template call
            mock_template.assert_called_with(
                "confirmation", 
                title="Confirmation", 
                amount_paid='100', 
                clipcard_type_title='test_clipcard_type', 
                created_at=unittest.mock.ANY,
                global_content=mock_global_content, 
                payment_id=unittest.mock.ANY
            )

        # Check the response
        self.assertEqual(response, "Payment confirmation")

        # Ensure database operations were called correctly
        mock_cursor.execute.assert_any_call(
            "SELECT clipcard_type_id, clipcard_type_time FROM card_types WHERE clipcard_type_title = ?",
            ('test_clipcard_type',)
        )
        mock_cursor.execute.assert_any_call(
            "INSERT INTO payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
            (unittest.mock.ANY, 'test_user_id', unittest.mock.ANY, '100', unittest.mock.ANY)
        )
        mock_cursor.execute.assert_any_call(
            "INSERT INTO clipcards (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (unittest.mock.ANY, 'test_clipcard_type_id', 0, 60, unittest.mock.ANY, unittest.mock.ANY, 1)
        )

        # Ensure the database commit and close were called
        mock_db.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

    @patch('routers.payment.request')
    @patch('routers.payment.logger')
    @patch('routers.payment.get_current_user')
    @patch('routers.payment.master')
    def test_process_payment_no_user(self, mock_master, mock_get_current_user, mock_logger, mock_request):
        # Mock the get_current_user to return None
        mock_get_current_user.return_value = None

        # Mock the request forms
        mock_request.forms.get.return_value = 'test_value'

        with self.assertRaises(Exception) as context:
            process_payment()

        self.assertTrue('User information not found in session.' in str(context.exception))

    @patch('routers.payment.request')
    @patch('routers.payment.logger')
    @patch('routers.payment.get_current_user')
    @patch('routers.payment.master')
    def test_process_payment_no_clipcard_type(self, mock_master, mock_get_current_user, mock_logger, mock_request):
        # Mock the get_current_user to return a valid user
        mock_get_current_user.return_value = {'user_id': 'test_user_id'}

        # Mock the request forms
        mock_request.forms.get.side_effect = lambda key: {
            'clipcard_price': '100',
            'clipcard_type': 'non_existent_clipcard_type'
        }[key]

        # Mock the database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_master.db.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Mock the database query results to return None for clipcard type
        mock_cursor.fetchone.return_value = None

        with self.assertRaises(Exception) as context:
            process_payment()

        self.assertTrue('Clipcard type not found' in str(context.exception))

        # Ensure database rollback and close were called
        mock_db.rollback.assert_called_once()
        mock_db.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
