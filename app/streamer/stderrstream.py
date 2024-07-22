import sys
from .streamer import Streamer

class StdErrStream(Streamer):
    def __init__(self):
        super().__init__()
    
    def print(self):
        for msg in self.buffer:
            print(msg, file=sys.stderr)
        return
    