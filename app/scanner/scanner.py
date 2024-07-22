from ..recognizer import Recognizer
from ..streamer import StdErrStream, Streamer

class Scanner:
    def __init__(self, file_contents: str):
        self.file_contents = file_contents
        self.regconizer = Recognizer()
    
    def scan(self, stderr_stream: StdErrStream, std_stream: Streamer):
        for line_number, line in enumerate(self.file_contents.splitlines()):
            for token in line:
                self.regconizer.recognize(
                    token = token,
                    line_number = line_number,
                    stderr_stream = stderr_stream,
                    std_stream=std_stream
                )
    
    def print_eof(self):
        print("EOF  null")
        return