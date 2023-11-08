"""TestModul for class Fetcher"""

import unittest
from unittest import mock
import aiounittest
import aioresponses

import fetcher


class TestFetcher(unittest.TestCase):
    """TestClass from unittest"""

    def test_crash_server_initial_with_value(self):
        with self.assertRaises(ValueError):
            fetcher.Fetcher(0, "random_urls.txt", k_top=2)

        with self.assertRaises(FileNotFoundError):
            fetcher.Fetcher(10, "not_found_file.txt", k_top=2)

    def test_init_without_errors(self):
        n_workers = 10
        filename = "random_urls.txt"
        fetch = fetcher.Fetcher(n_workers, filename)
        self.assertEqual(fetch.n_workers, n_workers)
        self.assertEqual(fetch.file_name, filename)

    def test_most_common_words(self):
        data1 = 'hello world world world hello peace'
        fetch = fetcher.Fetcher(10, "random_urls.txt", k_top=2)
        result = fetch._find_frequent_words(data1)
        true_result = [('world', 3), ('hello', 2)]
        self.assertEqual(result, true_result)

    def test_most_common_words_less_k_top(self):
        data1 = 'hello world world world hello peace'
        fetch = fetcher.Fetcher(10, "random_urls.txt", k_top=5)
        result = fetch._find_frequent_words(data1)
        true_result = [('world', 3), ('hello', 2), ('peace', 1)]
        self.assertEqual(result, true_result)


class TestFetcherAio(aiounittest.AsyncTestCase):
    """TestClass from aiounittest"""

    async def test_get_url_info(self):
        async def text():
            return '<html><body>hello world world ' \
                   'world hello peace</body></html>'

        response = mock.Mock()
        response.text = text
        fetch = fetcher.Fetcher(10, "random_urls.txt", k_top=5)
        result = await fetch._get_url_info(response)
        true_result = [('world', 3), ('hello', 2), ('peace', 1)]
        self.assertEqual(result, true_result)

    async def test_fetch_url_failed_connect(self):
        fetch = fetcher.Fetcher(10, "random_urls.txt", k_top=5)
        with aioresponses.aioresponses() as mock_url:
            mock_url.get('http://example.com',
                         status=404,
                         body='<html><body>hello world world'
                              'world hello peace</body></html>')

            with self.assertRaises(Exception):
                await fetch.fetch_url('http://example.com')


if __name__ == "__main__":
    unittest.main()
