from .parentheses import PARENTHESES_MAPPER
from .braces import BRACES_MAPPER

class Recognizer:
    def __init__(self):
        self.tbl = dict()
        self.tbl.update(PARENTHESES_MAPPER)
        self.tbl.update(BRACES_MAPPER)
    
    def recognize(self, token):
        desc = self.tbl.get(token, None)
        if desc is None:
            return "UNKNOWN"
        
        print(f"{desc} {token} null")
        return