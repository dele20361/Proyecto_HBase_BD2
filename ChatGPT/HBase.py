from HBaseTable import HBaseTable

class HBase:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, column_families):
        if table_name in self.tables:
            raise ValueError(f"Table {table_name} already exists")
        self.tables[table_name] = HBaseTable(table_name, column_families)

    def list_tables(self):
        return list(self.tables.keys())

    def disable_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table {table_name} does not exist")
        self.tables[table_name] = None

    def is_enabled(self, table_name):
        return table_name in self.tables and self.tables[table_name] is not None

    def alter_table(self, table_name, column_families):
        if table_name not in self.tables:
            raise ValueError(f"Table {table_name} does not exist")
        self.tables[table_name].column_families = column_families

    def drop_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table {table_name} does not exist")
        del self.tables[table_name]

    def drop_all_tables(self):
        self.tables = {}

    def describe_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table {table_name} does not exist")
        return self.tables[table_name].column_families

    def get_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"Table {table_name} does not exist")
        return self.tables[table_name]
