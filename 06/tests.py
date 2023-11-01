"""TestModul for connecting Server and Client"""

import unittest
from unittest import mock

import server
import client


class TestCustomList(unittest.TestCase):
    """TestClass"""

    def test_crash_server_initial_with_value(self):
        with self.assertRaises(ValueError):
            server.Server(0, 1)

        with self.assertRaises(ValueError):
            server.Server(10, -2)

    def test_crash_server_initial_with_type(self):
        with self.assertRaises(TypeError):
            server.Server(10, "7")

        with self.assertRaises(TypeError):
            server.Server("10", 7)

    def test_most_common_words_short(self):
        data = 'hello world world world hello'
        test_server = server.Server(10, 7)
        result = test_server._find_frequent_words(data)
        true_result = {"world": 3, "hello": 2}
        true_result = server.json.dumps(true_result, ensure_ascii=False).encode()
        self.assertEqual(result, true_result)

    @mock.patch.object(server.socket.socket, 'accept')
    @mock.patch.object(server.socket.socket, 'recv')
    @mock.patch.object(server.ThreadPoolExecutor, 'submit')
    def test_server_connection(self, mock_submit, mock_recv, mock_accept):
        mock_recv.return_value = b'http://www.example.com/'
        mock_accept.return_value = server.socket.socket(), None
        serv = server.Server(3, 7)
        serv.run(infinity=False)
        self.assertEqual(mock_submit.call_count, 1)

    def test_crash_client_initial_with_value(self):
        with self.assertRaises(ValueError):
            client.Client("3a", "random_urls.txt")

        with self.assertRaises(ValueError):
            client.Client("0", "random_urls.txt")


if __name__ == "__main__":
    unittest.main()
