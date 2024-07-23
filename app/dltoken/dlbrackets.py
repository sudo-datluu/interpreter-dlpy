from .dltoken import DLToken

class DLBrackets(DLToken):
    def __init__(self, chr_val: str, desc: str):
        super().__init__(chr_val, desc)