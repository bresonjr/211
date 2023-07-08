from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import threading

SERVER = "0.0.0.0"  # Use "0.0.0.0" for all available interfaces
PORT = 2121

def ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "/path/to/shared/folder", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((SERVER, PORT), handler)
    server.serve_forever()

def setup_thread():
    ftp()

if __name__ == "__main__":
    setup_thread()
