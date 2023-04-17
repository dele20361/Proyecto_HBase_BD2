import datetime
import time
from HFile import HFile


class HBase:
    def __init__(self):
        self.tables = {}
        # key = Nombre de tabla
        # value = Objeto tabla


    def list(self):
        print("-- Tablas Creadas --")
        for key in self.tables.keys():
            print(">",key)



    def deleteall(self):
        for key in self.tables.keys():
                tableObj = self.tables[key]
                tableObj.delete()


    def dropall(self):
        '''
            Drop de todas las tablas en base de datos.
        '''
        oldSize = len(list(self.tables))
        self.tables = {}
        print(f"Dropall realizado exitosamente!\n  Details: \n     Tables size: before({oldSize}) -> after ({len(list(self.tables))})\n")


    def deleteTable(self, table_name:str):
        '''
            Elimina toda la información de la tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la base de datos.

        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.delete()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def disableTable(self, table_name:str):
        '''
            Deshabilitar tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la base de datos.

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
            - Si el nombre de la tabla no existe en la base de datos.

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
        Modifica una tabla existente para eliminar o modificar nombre de la column family.

        Parámetros:
        -----------
        - table_name (str): Nombre de la tabla.
        - column_family_name (str): Nombre de la familia de columnas a modificar.
        - new_name (str, opcional): Nuevo nombre de la familia de columnas a asignar. Por defecto es None.
        - delete (bool, opcional): Bandera que indica si se debe eliminar la familia de columnas indicada. Por defecto es False.

        Excepciones:
        ------------
        - Si no existe la tabla en la base de datos.
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
            tableObj.alter(column_family, new_name, delete)
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def dropTable(self, table_name:str):
        '''
            Eliminar tabla de base de datos.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la base de datos.

        '''
        if table_name in self.tables.keys():
            self.tables.pop(table_name)
            print(f"> Drop de la tabla '{table_name}' realizado exitosamente!")
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")



    def describeTable(self, table_name:str):
        '''
            Información de base de datos de tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la base de datos.
            - Si la tabla se encuentra deshabilitada.

        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.describe()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def scanTable(self,table_name:str):
        # Conectar con HFile
        for table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.scan()


    def createTable(self, table_name:str, *args:str):
        '''
            Crea tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.
            - args (str): Nombres de family columns por añadir a tabla.

            Excepciones:
            ------------
            - Si el nombre de la tabla ya existe en la base de datos.

            Ejemplos:
            ---------
            >>> # Crear tabla 'Hola' con family column 'Saludos'
            >>> createTable('Hola', 'Saludos')

            >>> # Crear tabla 'Ejemplo' con family columns 'fam1', 'fam2', 'fam3'
            >>> createTable('Ejemplo', 'fam1', 'fam2', 'fam3')
        '''
        if table_name not in self.tables.keys():
            hfile = HFile()
            hfile.create(table_name, *args)
            self.tables[table_name] = hfile
        else:
            print("@! El nombre indicado ya existe.\n   Details: \n     Duplicated table names can not be accepted.\n")


    def countTable(self, table_name:str):
        '''
            Cantidad de filas en tabla.

            Parámetros:
            -----------
            - table_name (str): Nombre de la tabla a crear.

            Retorna:
            --------
            - Cantidad de filas en tabla.

            Excepciones:
            ------------
            - Si el nombre de la tabla no existe en la base de datos.
        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            return tableObj.count()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


    def truncateTable(self, table_name:str):
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.truncate()
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")

    def putTable(self,table_name,row_id,family,clasificator,value):
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            tableObj.put(table_name, row_id,family,clasificator,value)
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")

    
    def getTable(self,table_name:str, row_key:str,family_column:str=None, column_qualifier:str=None):
        '''
        
        Ejemplo:
        --------
        >>> # Obtener información dada un table_name y row_key.
        >>> get "Ejemplo", "row1"
        
        >>> # Obtener información dada un table_name, row_key, family_column y column_qualifier.
        >>> get "Ejemplo", "row1", {COLUMN => "family_column:column_qualifier"}

        '''
        if table_name in self.tables.keys():
            tableObj = self.tables[table_name]
            if family_column is not None and column_qualifier is not None:
                tableObj.get(row_key, family_column, column_qualifier)
            else:
                tableObj.get(row_key)
        else:
            print(f"@! La tabla '{table_name}' no existe.\n   Details: \n     '{table_name}' is not defined in HBase tables.\n")


if __name__ == "__main__":
    hbase = HBase()
    hbase.createTable('Ejemplo', 'family_column', 'family_column2')
    cell_data = {'Monday': "value"}
    cell_data2 = {'Wednesday': "value2"}
    hbase.tables['Ejemplo'].table =   [
                        {
                            'row_key': 'row1',
                            'column_key': ['family_column', 'column_qualifier'],
                            'cell_data': cell_data
                        }, 
                        {
                            'row_key': 'row2',
                            'column_key': ['family_column2', 'column_qualifier2'],
                            'cell_data': cell_data2
                        }
                    ]
    hbase.getTable('Ejemplo','row1', 'family_column', 'column_qualifier')
    # table.get('row1')
