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

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        self.assertTrue(mock_predict.called)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_called_once(self, mock_predict):
        mock_predict.return_value = 0.2

        msg = "Вулкан"
        model = SomeModel()

        predict_message_mood(msg, model)

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        self.assertEqual(mock_predict.call_count, 1)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_neud(self, mock_predict):
        mock_predict.return_value = 0.2

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        expected_value = "неуд"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_norm(self, mock_predict):
        mock_predict.return_value = 0.567

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        expected_value = "норм"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_predict_message_mood_for_otl(self, mock_predict):
        mock_predict.return_value = 0.91

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        expected_value = "отл"

        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_type_of_predict_message_mood(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = "Вулкан"
        model = SomeModel()

        result = predict_message_mood(msg, model)

        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))

        self.assertTrue(isinstance(result, str))

    @patch.object(SomeModel, 'predict')
    def test_incorrect_type_message(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = 123
        model = SomeModel()

        with self.assertRaises(TypeError):
            predict_message_mood(msg, model)

        self.assertFalse(mock_predict.called)

    @patch.object(SomeModel, 'predict')
    def test_incorrect_type_model(self, mock_predict):
        mock_predict.return_value = 0.5

        msg = "Вулкан"
        model = "model"

        with self.assertRaises(TypeError):
            predict_message_mood(msg, model)

        self.assertFalse(mock_predict.called)

    @patch.object(SomeModel, 'predict')
    def test_boundary_values(self, mock_predict):
        mock_predict.return_value = 0.3
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.8
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_around_boundary_values(self, mock_predict):
        mock_predict.return_value = 0.29
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "неуд"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.31
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.79
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.81
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "отл"
        self.assertEqual(result, expected_value)

    @patch.object(SomeModel, 'predict')
    def test_change_thresholds(self, mock_predict):
        mock_predict.return_value = 0.29
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.31
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.19
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "неуд"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.21
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.79
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.81
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.89
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "норм"
        self.assertEqual(result, expected_value)

        mock_predict.return_value = 0.91
        msg = "Вулкан"
        model = SomeModel()
        result = predict_message_mood(msg, model, bad_thresholds=0.2, good_thresholds=0.9)
        args = mock_predict.call_args.args
        self.assertEqual(args, ('Вулкан',))
        expected_value = "отл"
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
