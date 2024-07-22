from .parentheses import PARENTHESES_MAPPER
from .braces import BRACES_MAPPER
from .singlecharacters import SINGLE_CHARACTERS_MAPPER

class Recognizer:
    def __init__(self):
        self.tbl = dict()
        self.tbl.update(PARENTHESES_MAPPER)
        self.tbl.update(BRACES_MAPPER)
        self.tbl.update(SINGLE_CHARACTERS_MAPPER)
    
    def recognize(self, token):
        desc = self.tbl.get(token, None)
        if desc is None:
            return "UNKNOWN"
        
        print(f"{desc} {token} null")
        return