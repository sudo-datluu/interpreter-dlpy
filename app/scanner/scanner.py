from ..recognizer import Recognizer
from ..streamer import StdErrStream, Streamer

class Scanner:
    def __init__(self, file_contents: str):
        self.file_contents = file_contents
        self.regconizer = Recognizer()
    
    def scan(self, stderr_stream: StdErrStream, std_stream: Streamer):
        for line_number, line in enumerate(self.file_contents.splitlines()):
            offset = 0
            while offset < len(line):
                # Handle two character tokens
                token = None
                # comment
                if line[offset:offset+2] == "//":
                    break
                # Tab
                if line[offset:offset+7] == '<|TAB|>':
                    offset += 7
                    continue
                # Space
                if line[offset:offset+9] == '<|SPACE|>':
                    offset += 9
                    continue
                if offset + 1 < len(line) and self.regconizer.is_regconized(line[offset:offset+2]):
                    token = line[offset:offset+2]
                    offset += 2
                # Handle single character token
                else:
                    token = line[offset]
                    offset += 1
                self.regconizer.recognize(
                    token = token,
                    line_number = line_number,
                    stderr_stream = stderr_stream,
                    std_stream=std_stream
                )
            self.regconizer.process_last_line(
                line_number=line_number,
                stderr_stream=stderr_stream, 
                std_stream=std_stream
            )
    def print_eof(self):
        print("EOF  null")
        return