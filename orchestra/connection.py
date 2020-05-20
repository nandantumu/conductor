"""
This module contains all code pertaining to creating and maintaining a connection
"""
import zmq

class ServerConnection():
    """This class defines a zmq connection"""
    def __init__(self, type=zmq.REP):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*.5555")

    def send_start_signal(self):
        pass