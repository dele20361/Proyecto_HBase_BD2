class HFile:
    def __init__(self, name):
        self.name = name
        self.table = []
        self.column_families = {}

    