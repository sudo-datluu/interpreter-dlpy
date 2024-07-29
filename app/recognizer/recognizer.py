from .singlecharacters import SINGLE_CHARACTERS_MAPPER
from .brackets import BRACKETS_MAPPER
from .operators import *

from ..streamer import StdErrStream, Streamer
from app.dltoken import DLToken, DLOperators, DLBrackets

import sys

class DLBuffer:
    def __init__(self, trigger_char: str = "\""):
        self.buffer = ""
        self.flag = False
    
    
    def _reset(self):
        res = self.buffer
        self.buffer = ""
        self.flag = False
        return res

    def handle(self):
        if not self.flag: self.flag = True
        else: return self._reset()

class Recognizer:
    def __init__(self):
        self.modes = [0, 1, 2]
        self.tbl = dict()

        # String buffer
        self.string_buffer = DLBuffer()

        self.tokenize(SINGLE_CHARACTERS_MAPPER, mode=0)
        self.tokenize(ASSIGN_OPERATORS_MAPPER, mode=1, optype="ASSIGN")
        self.tokenize(RELATIONAL_OPERATORS_MAPPER, mode=1, optype="RELATIONAL")
        self.tokenize(ARITHMETIC_OPERATORS_MAPPER, mode=1, optype="ARITHMETIC")
        self.tokenize(BRACKETS_MAPPER, mode=2)

    '''
    Add token to the table
    - mode 0: general/single character token
    - mode 1: operator token
    - mode 2: bracket token
    '''
    def tokenize(
            self, 
            src_tbl: dict, 
            mode: int = 0,
            optype: str = None
        ):
        if mode not in self.modes:
            raise ValueError("Invalid mode")

        for token, desc in src_tbl.items():
            if mode == 0:
                self.tbl[token] = DLToken(token, desc)
            elif mode == 1:
                optype = optype if optype else "ASSIGN"
                self.tbl[token] = DLOperators(token, desc, optype)
            elif mode == 2:
                self.tbl[token] = DLBrackets(token, desc)
    
    def recognize(
            self, 
            token: str, 
            line_number: int, 
            stderr_stream: StdErrStream,
            std_stream: Streamer
        ):

        # Meet the token for string
        if token == "\"": 
            reg_msg = self.string_buffer.handle()
            if reg_msg: 
                reg_msg = f"STRING \"{reg_msg}\" {reg_msg}"
                std_stream.add(reg_msg)

        # Handle other cases
        else:
            # If the string buffer is active, add the token to the buffer
            if self.string_buffer.flag:
                self.string_buffer.buffer += token
                return

            dltoken = self.tbl.get(token, None)
            if not dltoken and token:
                # Space or tab token
                if ord(token) == 9 or ord(token) == 32: return
                err_msg = f"[line {line_number+1}] Error: Unexpected character: {token}"
                stderr_stream.add(err_msg)
                return
            reg_msg = dltoken.__str__()

        std_stream.add(reg_msg)
        return

    def process_last_line(
            self, 
            line_number: int, 
            stderr_stream: StdErrStream,
            std_stream: Streamer
        ):
            if self.string_buffer.flag:
                err_msg = f"[line {line_number+1}] Error: Unterminated string"
                stderr_stream.add(err_msg)

            self.string_buffer._reset()


    def is_regconized(self, token: str) -> bool:
        return token in self.tbl