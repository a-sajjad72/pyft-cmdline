from pyft.pyft import Server, FileTransfer
import os

class Reciever(Server):
    def __init__(
        self,
        host: str = None,
        port: int = 9999,
        maxClients: int = 8,
        path: str = None,
    ):
        super().__init__(host, port, maxClients)
        self.path = path
        self.start_server()

    def accept_connections(self) -> None:
        conn, addr = self.serverSocket.accept()
        print(f"[{addr[0]}:{addr[1]}] connected.")
        self.client_handler(conn, addr)
        conn.close()

    def client_handler(self, conn, addr) -> None:
        ft = FileTransfer(conn, 102400)

        # temporary directory to store the received archived files/directories if the path is not provided.
        if self.path is None:
            temp_dir = "recv_data"
            self.path = os.path.join(os.getcwd(), temp_dir)
            if not os.path.isdir(self.path):
                os.mkdir(temp_dir)

        # number of files to recieve
        files_count = int(ft.recv_msg())

        print("total files to receive:", files_count)

        # receiving the files
        for i in range(files_count):
            filename = ft.recv_file(self.path)

if __name__ == "__main__":
    ip = input('enter your public ip address: ')
    recieve = Reciever(ip)
