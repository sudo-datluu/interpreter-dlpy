class Streamer:
    def __init__(self):
        self.buffer = []
    
    def add(self, msg: str):
        self.buffer.append(msg)
    
    def print(self):
        for msg in self.buffer:
            print(msg)
        return