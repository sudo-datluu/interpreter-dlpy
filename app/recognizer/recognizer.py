from .singlecharacters import SINGLE_CHARACTERS_MAPPER
from .brackets import BRACKETS_MAPPER
from .operators import OPERATORS_MAPPER

from ..streamer import StdErrStream, Streamer
from app.dltoken import DLToken, DLOperators, DLBrackets

import sys

class Recognizer:
    def __init__(self):
        self.modes = [0, 1, 2]
        self.tbl = dict()

        self.tokenize(SINGLE_CHARACTERS_MAPPER, mode=0)
        self.tokenize(OPERATORS_MAPPER, mode=1)
        self.tokenize(BRACKETS_MAPPER, mode=2)

    '''
    Add token to the table
    - mode 0: general/single character token
    - mode 1: operator token
    - mode 2: bracket token
    '''
    def tokenize(self, src_tbl: dict, mode: int = 0):
        if mode not in self.modes:
            raise ValueError("Invalid mode")

        for token, desc in src_tbl.items():
            if mode == 0:
                self.tbl[token] = DLToken(token, desc)
            elif mode == 1:
                self.tbl[token] = DLOperators(token, desc)
            elif mode == 2:
                self.tbl[token] = DLBrackets(token, desc)
    
    def recognize(
            self, 
            token: str, 
            line_number: int, 
            stderr_stream: StdErrStream,
            std_stream: Streamer
        ):
        dltoken = self.tbl.get(token, None)
        if dltoken is None:
            err_msg = f"[line {line_number+1}] Error: Unexpected character: {token}"
            stderr_stream.add(err_msg)
            return
        
        reg_msg = dltoken.__str__()
        std_stream.add(reg_msg)
        return

    def is_regconized(self, token: str) -> bool:
        return token in self.tbl