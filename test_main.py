
import unittest
from unittest.mock import patch
from main import prepare_action, execute_action


class TestApprovalAgent(unittest.TestCase):

    @patch("main.OpenAI")
    def test_prepare_action(self, mock_openai):
        mock_client = mock_openai.return_value
        mock_response = mock_client.chat.completions.create.return_value
        mock_response.choices[0].message.content = (
            "Subject: Leave Request\n\n"
            "Dear [Manager Name],\n\n"
            "I request leave for [Start Date].\n\n"
            "Sincerely,\n[Your Name]"
        )

        draft = prepare_action("I need leave tomorrow")

        self.assertIn("Subject: Leave Request", draft)
        self.assertIn("Dear [Manager Name]", draft)
        self.assertIn("[Start Date]", draft)
        mock_client.chat.completions.create.assert_called_once()

    def test_execute_approved_action(self):
        letter = "Subject: Leave Request"

        result = execute_action(letter)

        self.assertIn("Approved letter is ready", result)
        self.assertIn(letter, result)

    def test_empty_action_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_action("")


if __name__ == "__main__":
    unittest.main()
