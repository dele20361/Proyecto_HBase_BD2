

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


    def deleteTable(self, table_name:str):
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            #TODO
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    
    def listTable(self):
        # Conectar con HFile
        pass
        # TODO



    def disableTable(self, table_name:str):
        '''
            Deshabilitar tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la estructura de HBase.

        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.disable()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")



    def table_is_enabled(self, table_name:str):
        '''
            Obtener bandera para conocer si la tabla se encuentra deshabilitada o no.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la estructura de HBase.

            Retorna:
            --------
            - enabled (bool): Bandera en donde True indica que la tabla está habilitada y False indica que está deshabilitada.
        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.Is_enabled()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def alterTable(self, table_name:str, column_family:str, new_name: str = None, delete:bool = False):
        '''
        Modifica una tabla existente para agregar o eliminar columnas o modificar propiedades de las columnas.

        Parámetros:
        -----------
        - table_name (str): Nombre de la tabla.
        - column_family_name (str): Nombre de la familia de columnas a modificar.
        - new_name (str, opcional): Nuevo nombre de la familia de columnas a asignar. Por defecto es None.
        - delete (bool, opcional): Bandera que indica si se debe eliminar la familia de columnas indicada. Por defecto es False.

        Excepciones:
        ------------
        - Si no existe la tabla en la estructura de HBase.
        - Si la tabla se encuentra deshabilitada.
        - Si se especifica un nuevo nombre de familia de columnas que ya existe.
        - Si se intenta eliminar una familia de columnas que no existe.

        Ejemplos:
        ---------
        >>> # Modificar el nombre de la familia de columnas 'familia1' a 'nueva_familia1'
        >>> alterTable('table', 'familia1', new_name='nueva_familia1')

        >>> # Eliminar la familia de columnas 'familia'
        >>> alterTable('table', 'familia', delete=True)
        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            #TODO
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def dropTable(self, table_name:str):
        '''
            Eliminar tabla de estructura de HBase.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la estructura de HBase.

        '''
        if table_name in self.tables.keys():
            self.tables.pop(table_name)
            print(f"> Drop de la tabla '{table_name}' realizado exitosamente!")
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")



    def describeTable(self, table_name:str):
        '''
            Información de estructura de tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la estructura de HBase.
            - Si la tabla se encuentra deshabilitada.

        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.describe()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def scanTable(self):
        # Conectar con HFile
        pass
        # TODO


    def createTable(self, table_name:str, *args:str):
        '''
            Crea tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.
            - args (str): Nombres de family columns por añadir a tabla.

            Excepciones:
            ------------
            - Si el nombre de la tabla ya existe en la estructura de HBase.

            Ejemplos:
            ---------
            >>> # Crear tabla 'Hola' con family column 'Saludos'
            >>> createTable('Hola', 'Saludos')

            >>> # Crear tabla 'Ejemplo' con family columns 'fam1', 'fam2', 'fam3'
            >>> createTable('Ejemplo', 'fam1', 'fam2', 'fam3')
        '''
        if table_name not in self.tables.keys():
            hfile = HFile()
            hfile.create(table_name, args)
            self.tables[table_name] = hfile
        else:
            print("@! El nombre indicado ya existe.\n   Details: \n     Duplicated table names can not be accepted.\n")

if __name__ == "__main__":
    hbase = HBase()
    hbase.createTable('Ejemplo', 'fam1')

