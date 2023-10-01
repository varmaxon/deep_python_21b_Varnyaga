import unittest
from unittest import mock

from parse_json import parse_json


class TestParser(unittest.TestCase):

    def test_parse_json_all_arguments(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            required_fields=["key1"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(result, 0)

    def test_parse_json_empty_callback(self):

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            required_fields=["key1"],
                            keywords=["word2"])

        self.assertEqual(result, -1)

    def test_parse_json_empty_keywords(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            required_fields=["key1"],
                            keyword_callback=foo_mock)

        self.assertEqual(result, -1)

    def test_parse_json_empty_fields(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(result, -1)

    def test_parse_json_incorrect_json_type(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str={"key1": "Word1 word2",
                                      "key2": "word2 word3"},
                            required_fields=["key1"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(result, -1)

    def test_parse_json_call_count_1(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            required_fields=["key1"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 1)
        self.assertEqual(result, 0)

    def test_parse_json_result_of_calling(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2", '
                                     '"key2": "word2 word3"}',
                            required_fields=["key1"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        foo_mock.assert_called_with('key1', 'word2')
        self.assertEqual(result, 0)

    def test_parse_json_call_count_more(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2 word3", '
                                     '"key2": "word2 word3 word4"}',
                            required_fields=["key1", "key2"],
                            keywords=["word2", "word3"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 4)
        self.assertEqual(result, 0)

    def test_parse_json_not_found_fields(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2 word3", '
                                     '"key2": "word2 word3 word4"}',
                            required_fields=["key_1", "key_2"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 0)
        self.assertEqual(result, 0)

    def test_parse_json_not_found_keywords(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2 word3", '
                                     '"key2": "word2 word3 word4"}',
                            required_fields=["key1"],
                            keywords=["word_2"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 0)
        self.assertEqual(result, 0)

    def test_parse_json_same_fields(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2 word3", '
                                     '"key2": "word2 word3 word4"}',
                            required_fields=["key1", "key1", "key1"],
                            keywords=["word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 1)
        self.assertEqual(result, 0)

    def test_parse_json_same_keywords(self):

        foo_mock = mock.Mock(return_value=None)

        result = parse_json(json_str='{"key1": "Word1 word2 word3", '
                                     '"key2": "word2 word3 word4"}',
                            required_fields=["key1"],
                            keywords=["word2", "word2", "word2"],
                            keyword_callback=foo_mock)

        self.assertEqual(foo_mock.call_count, 1)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
