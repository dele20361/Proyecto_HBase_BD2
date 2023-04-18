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
            print(f"\t\t-- Mostrando datos de la tabla '{self.name}' --\n")
            for row in self.table:
                rows = row['row_key']
                colum = row['column_key']
                data = row["cell_data"]
                
                timestamp = list(data.keys())[0]
                value = data[timestamp]
                print(f" - Row = {rows} \n", f"- Columns = {colum[0]}:{colum[1]}\n", f"- Timestamp = {timestamp} \n", f"- Value = {value} \n")
        else:
            print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")


    def disable(self):
        '''
            Deshabilitar una tabla.
        '''
        self.enabled = False
        print(f"\n> La tabla '{self.name}' ha sido deshabilitada exitosamente!.")


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
        Modifica una tabla existente para eliminar o modificar nombre de la column family.

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
        print(f"\n> Información de tabla '{self.name}' eliminada.")
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


    def put(self, table_name, row_id, family, clasificator, value):
        if self.enabled:
            for data_dict in self.table:
                if data_dict['row_key'] == row_id and data_dict['column_key'][0] == family and data_dict['column_key'][1] == clasificator:
                    print(list(data_dict['cell_data'].keys()))
                    #data_dict['cell_data'][list(data_dict['cell_data'].keys())[0]] = value
                    old_timestamp = list(data_dict['cell_data'].keys())[0]
                    data_dict['cell_data'][datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')] = value
                    del data_dict['cell_data'][old_timestamp]
                    
                    print(f"-> Valor de celda actualizado en la tabla '{table_name}' para la fila '{row_id}', familia '{family}', clasificator '{clasificator}'.")
                    return
                elif data_dict['row_key'] == row_id and data_dict['column_key'][0] == family and value in data_dict['cell_data'].values():
                    timestamp = [k for k, v in data_dict['cell_data'].items() if v == value][0]
                    del data_dict['cell_data'][timestamp]
                    temp2 = {datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'): value}
                    data_dict['cell_data'].update(temp2)
                    data_dict['column_key'][1] = clasificator
                    print(f"-> Valor de celda actualizado en la tabla '{table_name}' para la fila '{row_id}', familia '{family}', valor '{value}'.")
                    return
            # Si no se encontró una fila existente con el row_id, family y clasificator especificados, agregar una nueva fila
            temp = {}
            temp2 = {datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'): value}
            temp['row_key'] = row_id
            temp['column_key'] = [family, clasificator]
            temp['cell_data'] = temp2
            self.table.append(temp)
            print(f"-> '{row_id}' ha sido agregado a la tabla '{table_name}'.")
        else:
            print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")

    

    def get(self, row_key:str, family_column:str=None, column_qualifier:str=None):
        found = False
        if self.enabled:
            for data_dict in self.table:
                columInfo = data_dict['column_key']
                if family_column is None and column_qualifier is None:
                    if data_dict['row_key'] == row_key:
                        data = data_dict["cell_data"]
                        timestamp = list(data.keys())[0]
                        value = data[timestamp]
                        found = True

                        print(f" - Row = {row_key} \n", f"- Columns = {columInfo[0]}:{columInfo[1]}\n", f"- Timestamp = {timestamp} \n", f"- Value = {value} \n")
                else:
                    if data_dict['row_key'] == row_key and columInfo[0] == family_column and columInfo[1] == column_qualifier:
                        data = data_dict["cell_data"]
                        timestamp = list(data.keys())[0]
                        value = data[timestamp]
                        found = True

                        print(f" - Row = {row_key} \n", f"- Columns = {family_column}:{column_qualifier}\n", f"- Timestamp = {timestamp} \n", f"- Value = {value} \n")

            if not found:
                print(f"\n@! La información dada no se encuentra en la tabla '{self.name}'.\n")
        else:
            print(f"\n@! La tabla '{self.name}' se encuentra deshabilitada.")
    

    def count(self):
        '''
            Cantidad de filas en tabla.
        '''
        cant = len(self.table)
        print(f"\n> La tabla '{self.name}' cuenta con {cant} rows.")
        return cant
    

    def truncate(self):
        '''
            Deshabilita, elimina data manteniendo estructura de column families y column qualifiers 
            y vuelve a habilitar la tabla.
        '''
        print("\nTRUNCATE PROCESS...")
        self.disable()
        self.table = []
        print(f"\n> La información de la tabla {self.name} ha sido eliminada exitosamente!.")
        self.enabled = True        
        print(f"\n> La tabla '{self.name}' ha sido habilitada exitosamente!.")
        print("\nTRUNCATE COMPLETED!")

    
