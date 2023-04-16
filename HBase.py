

from HFile import HFile


class HBase:
    def __init__(self):
        self.tables = {}
        # key = Nombre de tabla
        # value = Objeto tabla

    def list(self):
        pass
        # TODO


    def deleteall(self):
        pass
        #TODO


    def dropall(self):
        pass
        #TODO


    def drop(self):
        pass
        #TODO


    def deleteTable(self):
        # Conectar con HFile
        pass
        # TODO

    
    def createTable(self):
        # Conectar con HFile
        pass
        # TODO

    
    def listTable(self):
        # Conectar con HFile
        pass
        # TODO


    def disableTable(self):
        # Conectar con HFile
        pass
        # TODO


    def table_is_enabled(self):
        # Conectar con HFile
        pass
        # TODO


    def alterTable(self):
        # Conectar con HFile
        pass
        # TODO


    def dropTable(self):
        # Conectar con HFile
        pass
        # TODO


    def describeTable(self):
        # Conectar con HFile
        pass
        # TODO


    def scanTable(self):
        # Conectar con HFile
        pass
        # TODO
        

    def createTable(self, table_name:str, *args:str):
        if table_name not in self.tables.keys():
            hfile = HFile()
            hfile.create(table_name, args)
            self.tables[table_name] = hfile
        else:
            print("@! El nombre indicado ya existe.\n   Details: \n     Duplicated table names can not be accepted.\n")

if __name__ == "__main__":
    hbase = HBase()
    hbase.createTable('Ejemplo', 'fam1')
    print(hbase.tables)

