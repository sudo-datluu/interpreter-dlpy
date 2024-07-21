from ..recognizer import Recognizer

class Scanner:
    def __init__(self, file_contents: str):
        self.file_contents = file_contents
        self.regconizer = Recognizer()
    
    def scan(self):
        for line in self.file_contents.splitlines():
            for token in line:
                self.regconizer.recognize(token)
    
    def print_eof(self):
        print("EOF  null")
        return