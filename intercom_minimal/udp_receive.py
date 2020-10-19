import socket

LISTENING_PORT = 4444

class UdpReceiver():
    # We use a context manager (https://docs.python.org/3/reference/datamodel.html#context-managers).
    def __enter__(self):
        """Create an UDP socket and listen to it."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("socket created")
        self.sock.bind(('', LISTENING_PORT))
        print(f"listening at {self.sock.getsockname()} ... ")
        return self

    def receive(self):
        """Receive a datagram."""
        (message, from_addr) = self.sock.recvfrom(10240) # Blocking operation, 1024 is the maximum expected payload size.
        print(f"received {message} from {from_addr}")
        return message
    
    def __exit__(self,ext_type,exc_value,traceback):
        """Close the socket."""
        self.sock.close()
        print("socket closed")