import unittest
from unittest.mock import patch

from some_model import SomeModel, predict_message_mood


class TestModel(unittest.TestCase):

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_called(self, mock_predict):
        mock_predict.return_value = 0.2

        msg = "Вулкан"
        model = SomeModel()

        predict_message_mood(msg, model)

        self.assertTrue(mock_predict.called)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_called_once(self, mock_predict):
        mock_predict.return_value = 0.2

        msg = "Вулкан"
        model = SomeModel()

        predict_message_mood(msg, model)

        self.assertEqual(mock_predict.call_count, 1)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_neud(self, mock_predict):
        mock_predict.return_value = 0.2

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)
        expected_value = "неуд"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_norm(self, mock_predict):
        mock_predict.return_value = 0.567

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)
        expected_value = "норм"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_otl(self, mock_predict):
        mock_predict.return_value = 0.91

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)
        expected_value = "отл"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_type_of_predict_message_mood(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)

        self.assertTrue(isinstance(result, str))

    @patch.object(SomeModel, 'predict')
    def test_incorrect_type_message(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = 123
        model = SomeModel()

        with self.assertRaises(TypeError):
            predict_message_mood(msg, model)

    @patch.object(SomeModel, 'predict')
    def test_incorrect_type_model(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = "Вулкан"
        model = "model"

        with self.assertRaises(TypeError):
            predict_message_mood(msg, model)


if __name__ == "__main__":
    unittest.main()
