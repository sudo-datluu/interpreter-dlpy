from .dltoken import DLToken

POSSIBLE_TYPES = [
    "ASSIGN",
    "RELATIONAL",
    "ARITHMETIC",
]
class DLOperators(DLToken):
    def __init__(self, chr_val: str, desc: str, optype: str):
        super().__init__(chr_val, desc)
        if optype not in POSSIBLE_TYPES:
            raise ValueError(f"Invalid type: {type}")
        self.optype = optype