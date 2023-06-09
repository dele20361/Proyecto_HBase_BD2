from HBase import HBase
import PySimpleGUI as sg
from Making_tables import *

class ShellUI:
    def __init__(self):
        self.hbase = HBase()
        Music_table(self.hbase)
        Users_table(self.hbase)
        sg.theme('DarkGrey14')   # Tema de la interfaz
        # Definir los elementos de la interfaz
        self.layout = [
            [sg.Text('Ingrese un comando:')],
            [sg.InputText(key='-IN-')],
            [sg.Button('Ejecutar'), sg.Button('Salir')],
            [sg.Output(size=(80,20),key='-OUTPUT-')]
        ]
    
    def run(self):
        # Crear la ventana
        # window = sg.Window('Shell').Layout(self.layout)
        window = sg.Window('Shell', layout=self.layout)
        while True:
            # Leer los eventos de la ventana
            event, values = window.Read()
            if event == sg.WIN_CLOSED or event == 'Salir':
                break
            # Obtener el comando ingresado por el usuario
            command = values['-IN-']

            # Ejecutar el comando y mostrar el resultado en la ventana de salida

            # dropall
            if command.strip()[:len('dropall')].lower() == 'dropall':
                self.hbase.dropall()
            
            #delete all data 
            elif command.strip()[:len('deleteall')].lower() == 'deleteall':
                self.hbase.deleteall()

            # deleteTable
            elif command.strip()[:len('delete')].lower() == 'delete':
                params = [param.strip() for param in command[len('delete'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.deleteTable(params[0][1:-1]) # Quitar commilas del parámetro
            
            # disableTable
            elif command.strip()[:len('disable')].lower() == 'disable':
                params = [param.strip() for param in command[len('disable'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.disableTable(params[0][1:-1]) # Quitar commilas del parámetro
            
            # Is_enabled
            elif command.strip()[:len('is_enabled')].lower() == 'is_enabled':
                params = [param.strip() for param in command[len('is_enabled'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.table_is_enabled(params[0][1:-1]) # Quitar commilas del parámetro
            
            # alterTable
            elif command.strip()[:len('alter')].lower() == 'alter':
                # EJEMPLOS
                # Cambiar nombre de column family
                # ALTER 'Ejemplo', {NAME => 'family_column', NEW_NAME => 'new_fam1}

                # Eliminar column family
                # ALTER 'Ejemplo', {NAME => 'fam1', METHOD => 'delete' }

                params = [param.strip() for param in command[len('alter'):].split(',') if param.strip() != '']
                params = [param.replace(" ", "") for param in params]
                if len(params) != 3 or (len(params) == 3 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 3 parámetros necesario.\n")
                else:
                    # Procesar params
                    table_name = params[0][1:-1] # Quitar commilas
                    # Column family name
                    name_fc = params[1]
                    column_family = name_fc[name_fc.index('=>')+len("=>")+1:-1]
                    # Segundo paramatero de función
                    method = params[2]
                    getMethod = method[:method.index('=>')]
                    getMethodValue = method[method.index('=>')+len("=>")+1:-2]

                    # Dependiendo de method llamar a función con distintos parámetros
                    if getMethod.upper() == 'METHOD' and getMethodValue.lower() == 'delete':
                        self.hbase.alterTable(table_name, column_family, delete=True)
                    elif getMethod.upper() == 'NEW_NAME':
                        self.hbase.alterTable(table_name, column_family, new_name=getMethodValue)
                    else:
                        print(f"@! Error.\n   Details: \n     Funcionalidad de ALTER: Modifica una tabla existente para eliminar o modificar nombre de la column family.\n")

            # dropTable
            elif command.strip()[:len('drop')].lower() == 'drop':
                params = [param.strip() for param in command[len('drop'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.dropTable(params[0][1:-1]) # Quitar comillas
            
            # describeTable
            elif command.strip()[:len('describe')].lower() == 'describe':
                params = [param.strip() for param in command[len('describe'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.describeTable(params[0][1:-1]) # Quitar comillas
            
            # countTable
            elif command.strip()[:len('count')].lower() == 'count':
                params = [param.strip() for param in command[len('count'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.countTable(params[0][1:-1]) # Quitar comillas
            
            # trucateTable
            elif command.strip()[:len('truncate')].lower() == 'truncate':
                params = [param.strip() for param in command[len('truncate'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    self.hbase.truncateTable(params[0][1:-1]) # Quitar comillas

            # create table
            elif command.strip()[:len('create')].lower() == 'create':
                params = [param.strip().strip('\'\"') for param in command[len('create'):].split(',') if param.strip() != '']
                if len(params) < 2 and params[0] == '':
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros.\n")
                else:
                    self.hbase.createTable(*params) # Pasar argumentos sin comillas

            # list tables 
            elif command.strip()[:len('list')].lower() == 'list':
                self.hbase.list()

            #Put data in table
            elif command.strip()[:len('put')].lower() == 'put':
                params = [param.strip() for param in command[len('put'):].split(',') if param.strip() != '']
                
                if len(params) != 5 or (len(params) == 5 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")

                else:   
                    self.hbase.putTable(params[0][1:-1], params[1][1:-1],params[2][1:-1],params[3][1:-1],params[4][1:-1]) # Quitar comillas

            # scan table
            elif command.strip()[:len('scan')].lower() == 'scan':
                params = [param.strip() for param in command[len('scan'):].split(',') if param.strip() != '']
                
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")

                else:   
                    self.hbase.scanTable(params[0][1:-1]) # Quitar comillas

            #get table 
            elif command.strip()[:len('get')].lower() == 'get':
                params = [param.strip() for param in command[len('get'):].split(',') if param.strip() != '']
                params = [param.replace(" ", "") for param in params]

                if len(params) != 2 and len(params) != 3:
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 2 a 3 parámetros necesario.\n")
                elif len(params) == 2:
                    self.hbase.getTable(params[0][1:-1], params[1][1:-1]) # Quitar comillas
                elif len(params) == 3:
                    name_fc = params[2]
                    columnParts = name_fc.split(':')
                    table_name = params[0][1:-1]
                    row_key = params[1][1:-1]
                    column_family = columnParts[0][1:]
                    column_qualifier = columnParts[1][:-1]
                    print(table_name, row_key,column_family, column_qualifier)
                    self.hbase.getTable(table_name, row_key, column_family, column_qualifier)

            elif command.strip()[:len('hfile')].lower() == 'hfile':
                params = [param.strip() for param in command[len('delete'):].split(',') if param.strip() != '']
                if len(params) == 1:
                    print(params[0][1:-1])
                    self.hbase.HFile(params[0][1:-1])
                elif len(params) == 0:
                    self.hbase.HFile()

#-------------------------------------------------------------------------------------------------------------------
            elif command == 'Clear' or command == 'clear' or command == 'clr':
                window['-OUTPUT-'].update('')
        # Cerrar la ventana
        window.Close()

if __name__ == '__main__':
    shell = ShellUI()
    shell.run()
