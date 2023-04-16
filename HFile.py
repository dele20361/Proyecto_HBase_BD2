from datetime import datetime
import time


class HFile:
    def __init__(self):
        self.name = None
        self.createdAt = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.table = []
        self.column_families = {}
        self.enabled = True

    def create(self, name:str, *args:str):
        '''
            Crear tabla 

            Parámetros:
        -----------
        - name (str): Nombre de la tabla .
        - *args (str): Nombre de las columnas, su cantidad puede variar.
        '''
        self.name = name
        self.column_families = {}
        self.column_families = {cf: [] for cf in args}
        print(f"\n> La tabla '{self.name}' se creó existosamente!.\n")

    def scan(self):
        '''
            Mostrar data de la tabla 
        '''
        if self.enabled:
            for row in self.table:
                rows = row['row_key']
                colum = row['column_key']
                time =  row['cell_data']

                print(f" -> Row = {rows} \n", f"-> Colum = {' '.join(colum)} \n", f"-> Timestamp = {' '.join(time)} \n")
        else:
            print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")

    def disable(self):
        '''
            Deshabilitar una tabla.
        '''
        self.enabled = False
        print(f"> La tabla '{self.name}' ha sido deshabilitada exitosamente!.")

    def Is_enabled(self):
        '''
            Obtener bandera para conocer si la tabla se encuentra deshabilitada o no.

            Retorna:
            --------
            - enabled (bool): Bandera en donde True indica que la tabla está habilitada y False indica que está deshabilitada.
        '''
        state = (f"\n> La tabla '{self.name}' se encuentra ")
        state += 'habilitada.' if self.enabled else 'deshabilitada.'
        print(state)
        return self.enabled

    def alter(self, column_family_name: str, new_name: str = None, delete: bool = False):
        '''
        Modifica una tabla existente para agregar o eliminar columnas o modificar propiedades de las columnas.

        Parámetros:
        -----------
        - column_family_name (str): Nombre de la familia de columnas a modificar.
        - new_name (str, opcional): Nuevo nombre de la familia de columnas a asignar. Por defecto es None.
        - delete (bool, opcional): Bandera que indica si se debe eliminar la familia de columnas indicada. Por defecto es False.

        Excepciones:
        ------------
        - Si la tabla se encuentra deshabilitada.
        - Si se especifica un nuevo nombre de familia de columnas que ya existe.
        - Si se intenta eliminar una familia de columnas que no existe.

        Ejemplos:
        ---------
        >>> # Modificar el nombre de la familia de columnas 'familia1' a 'nueva_familia1'
        >>> alter('familia1', new_name='nueva_familia1')

        >>> # Eliminar la familia de columnas 'familia'
        >>> alter('familia', delete=True)
        '''

        # Verificar que la tabla esté habilitada
        if self.enabled:
            if column_family_name in self.column_families.keys():
                # Cambiar nombre
                if new_name is not None:
                    if new_name not in self.column_families.keys():
                        # Eliminar column_family
                        values = self.column_families.pop(column_family_name)
                        # Añadir con nuevo nombre
                        self.column_families[new_name] = values

                        # Modificar valores en tabla que todavía tienen el nombre anterior.
                        for row in self.table:
                            if row['column_key'][0] == column_family_name:
                                row['column_key'][0] = new_name

                        print(f'\n> Cambio de nombre de column_family realizado exitosamente!.\n  Details: \n     Old value: {column_family_name} -> New value: {new_name}\n')
                    else:
                        print("\n@! El nombre indicado ya existe.\n   Details: \n     Duplicated names can not be accepted.\n")
                # Eliminar column family
                else:
                    if delete:
                        self.column_families.pop(column_family_name)
                        self.table = [row for row in self.table if row['column_key'][0] != column_family_name]
                        print(f'> Eliminación de column_family realizada exitosamente!.\n   Details: \n      Column_family deleted: {column_family_name}\n')
                    else:
                        print("\n@! No se han indicado instrucciones a modificar.\n   Details: \n     Error in ALTER function.\n")
            else:
                print(f"\n@! No se encontró la column family '{column_family_name}' en la tabla '{self.name}'")
        else:
            print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")


    def delete(self):
        '''
            Elimina toda la información de la tabla.
        '''
        print(f"... Eliminando información de tabla '{self.name}'.")
        self.table = []
        self.column_families = {}
        self.enabled = False


    def describe(self):
        '''
            Información de estructura de tabla.
            
            Excepciones:
            ------------
            - Si la tabla se encuentra deshabilitada.
        '''
        if self.enabled:
            print(f"""
        \n
    TABLE: {self.name}.\n
____________________________________________________________________________________________________

> Fecha de creación: {self.createdAt}.\n
> Enabled: {self.enabled}\n.
> Column families: {list(self.column_families.keys())}.\n
> Column families con column qualifiers: {self.column_families}.\n
> Contenido de tabla: \n\n{self.table}.\n
____________________________________________________________________________________________________
\n
""")
        else:
                print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")


    def put(self):
        pass
        # TODO

    
    def get(self):
        pass
        # TODO

    
    def count(self):
        '''
            Cantidad de filas en tabla.
        '''
        cant = len(self.table)
        print(f"\n> La tabla '{self.name}' cuenta con {cant} rows.")
        return cant
    
    def truncate(self):
        pass
        # TODO

    
if __name__ == "__main__":
    table = HFile()
    cell_data = {datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'): "value"}
    cell_data2 = {datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'): "value2"}
    table.create('Ejemplo','fam1','fam2')
    table.table =   [
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
    table.scan()
