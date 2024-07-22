from .parentheses import PARENTHESES_MAPPER
from .braces import BRACES_MAPPER
from .singlecharacters import SINGLE_CHARACTERS_MAPPER

from ..streamer import StdErrStream, Streamer

import sys

class Recognizer:
    def __init__(self):
        self.tbl = dict()
        self.tbl.update(PARENTHESES_MAPPER)
        self.tbl.update(BRACES_MAPPER)
        self.tbl.update(SINGLE_CHARACTERS_MAPPER)
    
    def recognize(
            self, 
            token: str, 
            line_number: int, 
            stderr_stream: StdErrStream,
            std_stream: Streamer
        ):
        desc = self.tbl.get(token, None)
        if desc is None:
            err_msg = f"[line {line_number+1}] Error: Unexpected character: {token}"
            stderr_stream.add(err_msg)
            return
        
        reg_msg = f"{desc} {token} null"
        std_stream.add(reg_msg)
        return