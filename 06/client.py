import socket
import sys
import threading


class Client:
    """Class Client for Server connecting"""

    def __init__(self, m_threads, file_name):
        try:
            self.m_threads = int(m_threads)
        except Exception as error:
            raise ValueError from error

        if self.m_threads < 1:
            raise ValueError("Threads number must be greater than 1")

        self.file_name = file_name

        with open(self.file_name, 'r', encoding='UTF-8') as file:
            self.urls = file.read().split()
            self.size = len(self.urls) // self.m_threads

    @staticmethod
    def fetch_url(url, host="127.0.0.1", port=65432):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.connect((host, port))
            server_socket.send(url.encode())
            answer = server_socket.recv(1024).decode()
        return answer

    def fetch_batch_urls(self, urls):

        for url in urls:
            print(f'{str(url)}: {self.fetch_url(url)}')

    def run(self):
        threads = [
            threading.Thread(
                target=self.fetch_batch_urls,
                name=f"fetch-{i}",
                args=(self.urls[i * self.size: (i + 1) * self.size],),
            )
            for i in range(self.m_threads)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    args = sys.argv[1:]

    client = Client(args[0], args[1])

    # start = time.time()
    client.run()
    # print(f"TIME: {round(time.time() - start, 3)}")
