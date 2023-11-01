import socket
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import json
import argparse
import requests
from bs4 import BeautifulSoup


class Server:
    """Class Server"""

    statistics_urls = 0
    mas = []

    def __init__(self, arg_w, arg_k, host="127.0.0.1", port=65432):
        if not isinstance(arg_w, int) or not isinstance(arg_k, int):
            raise TypeError("Type of params must be INT")

        if arg_w < 1:
            raise ValueError("Workers number must be greater than 1")

        if arg_k < 0:
            raise ValueError("K_top must be greater than 0")

        self.host = host
        self.port = port
        self.n_workers = arg_w
        self.k_top = arg_k

    def _find_frequent_words(self, str_words):
        list_words = Counter(str_words.split()).most_common(self.k_top)
        return json.dumps(dict(list_words), ensure_ascii=False).encode()

    def _send_to_client(self, url, client_socket):
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            str_words = BeautifulSoup(response.text, 'html.parser').get_text()
            self.statistics_urls += 1
            print("URLS Statistics:", self.statistics_urls)
            client_socket.send(self._find_frequent_words(str_words))
        else:
            raise Warning(f"URL {url} is not valid")

    def run(self, infinity=True):
        with ThreadPoolExecutor(max_workers=self.n_workers) as worker:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_:
                socket_.bind((self.host, self.port))
                socket_.listen(self.n_workers)
                while True:
                    client_socket, _ = socket_.accept()
                    url = client_socket.recv(1024).decode().strip()
                    worker.submit(self._send_to_client, url, client_socket)
                    if not infinity:
                        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse input string')
    parser.add_argument("-w", type=int, default=10)
    parser.add_argument("-k", type=int, default=7)
    args = parser.parse_args()
    server = Server(args.w, args.k)
    server.run()
