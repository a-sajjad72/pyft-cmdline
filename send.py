from pyft.pyft import Client, FileTransfer
from typing import List


class Sender(Client):
    def __init__(self, serverHost: str, serverPort: int, items: List[str]):
        super().__init__(serverHost, serverPort)
        self.items = items
        self.start_client()

    def response_server(self, conn) -> None:
        ft = FileTransfer(conn, 102400)

        # send the files in the list
        ft.send_msg(str(len(self.items)))
        for item in self.items:
            print("file to send", item)
            ft.send_file(str(item))


if __name__ == "__main__":
    host, port = input("provide the address shown on the reciever's screen-> ").split(":")
    send = Sender(host, int(port))
