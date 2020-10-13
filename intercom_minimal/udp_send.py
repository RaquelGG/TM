import socket

LISTENING_PORT = 8001

class UdpSender():
    def __enter__(self):
        '''Create an UDP socket.'''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("socket created")
        return self

    def send(self, message, destination):
        '''Send data.'''
        self.sock.sendto(message, (destination, LISTENING_PORT))
        print(f"message {message} sent to destination {destination}")

    def __exit__(self,ext_type,exc_value,traceback):
        '''Close the socket.'''
        self.sock.close()
        print("socket closed")