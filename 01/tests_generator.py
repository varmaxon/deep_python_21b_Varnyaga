import unittest
from unittest import mock
import io

from generator import generator


class TestGenerator(unittest.TestCase):

    @mock.patch("builtins.open", create=True)
    def test_example_from_task_found(self, mock_file):
        words = ["роза"]
        fake_file = io.StringIO("а Роза упала на лапу Азора")

        mock_file.return_value = fake_file
        result = list(generator("test.txt", words))

        expected_lines = ['а Роза упала на лапу Азора']

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_example_from_task_not_found(self, mock_file):
        words = ["роз", "розан"]
        fake_file = io.StringIO("а Роза упала на лапу Азора")

        mock_file.return_value = fake_file
        result = list(generator("test.txt", words))

        expected_lines = []

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_file_opened_once(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        list(generator("test.txt", words))

        mock_file.assert_called_once_with('test.txt', 'r', encoding='utf-8')

    @mock.patch("builtins.open", create=True)
    def test_generator_called_once(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        list(generator("test.txt", words))

        self.assertEqual(mock_file.call_count, 1)

    @mock.patch("builtins.open", create=True)
    def test_name_of_string(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator("test.txt", words))

        expected_lines = ['A Chip on Your Shoulder',
                          'A Fool and His Money Are Soon Parted']

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_name_of_file_object(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = ['A Chip on Your Shoulder',
                          'A Fool and His Money Are Soon Parted']

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_incorrect_type(self, mock_file):
        words = ["and", "chip"]
        fake_file = 123

        mock_file.return_value = fake_file

        with self.assertRaises(TypeError):
            list(generator(fake_file, words))

    @mock.patch("builtins.open", create=True)
    def test_empty_list(self, mock_file):
        words = []
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = []

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_empty_file(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO()

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = []

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_caps_words(self, mock_file):
        words = ["AND", "CHIP"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A Chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = ['A Chip on Your Shoulder',
                          'A Fool and His Money Are Soon Parted']

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_caps_words_in_file(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A CHIP on Your Shoulder\n"
                                "A Fool AND His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = ['A CHIP on Your Shoulder',
                          'A Fool AND His Money Are Soon Parted']

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_less_match(self, mock_file):
        words = ["an", "chi"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = []

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_more_match(self, mock_file):
        words = ["andy", "chipy"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A chip on Your Shoulder\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = []

        self.assertEqual(expected_lines, result)

    @mock.patch("builtins.open", create=True)
    def test_more_than_one_mathc(self, mock_file):
        words = ["and", "chip"]
        fake_file = io.StringIO("Needle In a Haystack\n"
                                "A chip on Your chip Shoulder chip\n"
                                "A Fool and His Money Are Soon Parted\n"
                                "No Ifs, Ands, or Buts\n"
                                "Hit Below The Belt")

        mock_file.return_value = fake_file
        result = list(generator(fake_file, words))

        expected_lines = ['A chip on Your chip Shoulder chip',
                          'A Fool and His Money Are Soon Parted']

        self.assertEqual(expected_lines, result)


if __name__ == "__main__":
    unittest.main()
