from .dltoken import DLToken

class DLOperators(DLToken):
    def __init__(self, chr_val: str, desc: str):
        super().__init__(chr_val, desc)