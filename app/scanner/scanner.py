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
                # String handle
                if line[offset] == "\"":
                    res_msg = self.regconizer.string_buffer.handle()
                    if res_msg:
                        res_msg = f"STRING \"{res_msg}\" {res_msg}"
                        std_stream.add(res_msg)
                    offset += 1
                    continue
                # Add token to the buffer
                else:
                    if self.regconizer.string_buffer.flag:
                        self.regconizer.string_buffer.buffer += line[offset]
                        offset += 1
                        continue
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