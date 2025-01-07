import unittest
from unittest.mock import patch, MagicMock
from project import fetch_quiz_data, run_quiz, display_score

class TestQuizApp(unittest.TestCase):

    @patch('project.input', side_effect=["1", "10"])
    @patch('project.requests.get')
    def test_fetch_quiz_data(self, mock_get, mock_input):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "question": "What is the capital of France?",
                    "correct_answer": "Paris",
                    "incorrect_answers": ["London", "Berlin", "Rome"]
                }
            ]
        }
        mock_get.return_value = mock_response

        questions = fetch_quiz_data()
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]['question'], "What is the capital of France?")
        self.assertEqual(questions[0]['correct_answer'], "Paris")

    @patch('project.random.shuffle', side_effect=lambda x: x)  # Keep answer order consistent
    @patch('project.input', side_effect=["4"])  # User selects "4" as the answer
    def test_run_quiz(self, mock_input, mock_shuffle):
        # Mock questions
        questions = [
            {
                "question": "What is 2+2?",
                "correct_answer": "4",
                "incorrect_answers": ["3", "5", "6"]
            }
        ]

        score = run_quiz(questions)
        self.assertEqual(score, 1)

    @patch('builtins.print')
    def test_display_score(self, mock_print):
        display_score(3, 5)
        # Verify the feedback is displayed
        mock_print.assert_any_call("\nQuiz Completed!")
        mock_print.assert_any_call("You answered 3 out of 5 questions correctly.")
        mock_print.assert_any_call("Your score: 60.00%")
        mock_print.assert_any_call("Good effort! Keep practicing.")

if __name__ == "__main__":
    unittest.main()
