class DLToken:
    def __init__(self, token: str, desc: str):
        self.token = token
        self.desc = desc

    def __str__(self):
        return f"{self.desc} {self.token} null"