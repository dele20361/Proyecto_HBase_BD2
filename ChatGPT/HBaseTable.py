import time


class HBaseTable:
    def __init__(self, name):
        self.name = name
        self.table = []
        self.column_families = {}
        
    def create(self, column_families):
        self.column_families = column_families
        
    def put(self, row_key, column_key, value, timestamp=None):
        family, column = column_key.split(":")
        if family not in self.column_families:
            raise ValueError(f"Column family not found for column {column_key}")
        if column not in self.column_families[family]:
            raise ValueError(f"Column not found in column family {family}: {column}")
        cell = {
            'row_key': row_key,
            'column_key': column_key,
            'cell_data': {
                timestamp or time.time(): value
            }
        }
        self.table.append(cell)
        
    def get(self, row_key, column_key):
        family, column = column_key.split(":")
        if family not in self.column_families:
            raise ValueError(f"Column family not found for column {column_key}")
        if column not in self.column_families[family]:
            raise ValueError(f"Column not found in column family {family}: {column}")
        cells = [cell for cell in self.table if cell['row_key'] == row_key and cell['column_key'] == column_key]
        return cells

    def scan(self, start_row=None, end_row=None, columns=None, timestamp=None):
        data = []
        for row_key, row_data in self.rows.items():
            if start_row is not None and row_key < start_row:
                continue
            if end_row is not None and row_key >= end_row:
                continue
            row = {'row_key': row_key}
            for column_family, options in self.column_families.items():
                for column in options['columns']:
                    if columns is not None and column not in columns:
                        continue
                    if column not in row_data:
                        continue
                    if timestamp is None:
                        value = row_data[column][-1][1]
                    else:
                        for ts, val in reversed(row_data[column]):
                            if ts <= timestamp:
                                value = val
                                break
                    row[column] = value
            if len(row) > 1:
                data.append(row)
        return data

    def delete(self, row_key, columns=None, timestamp=None):
        if row_key not in self.rows:
            return
        for column_family, options in self.column_families.items():
            for column in options['columns']:
                if columns is not None and column not in columns:
                    continue
                if column not in self.rows[row_key]:
                    continue
                if timestamp is None:
                    del self.rows[row_key][column]
                else:
                    new_cells = []
                    for ts, val in self.rows[row_key][column]:
                        if ts <= timestamp:
                            new_cells.append((ts, val))
                    self.rows[row_key][column] = new_cells

    def delete_all(self):
        self.rows = {}

    def count(self):
        return len(self.rows)
