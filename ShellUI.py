from HBase import HBase
import PySimpleGUI as sg

class ShellUI:
    def __init__(self):
        sg.theme('Dark')   # Tema de la interfaz
        # Definir los elementos de la interfaz
        self.layout = [
            [sg.Text('Ingrese un comando:')],
            [sg.InputText(key='-IN-')],
            [sg.Button('Ejecutar'), sg.Button('Salir')],
            [sg.Output(size=(80,20),key='-OUTPUT-')]
        ]
    
    def run(self):
        # Crear la ventana
        window = sg.Window('Shell').Layout(self.layout)
        while True:
            # Leer los eventos de la ventana
            event, values = window.Read()
            if event == sg.WIN_CLOSED or event == 'Salir':
                break
            # Obtener el comando ingresado por el usuario
            command = values['-IN-']

            # Ejecutar el comando y mostrar el resultado en la ventana de salida
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
            
            # dropall
            if command.strip()[:len('dropall')].lower() == 'dropall':
                hbase.dropall()

            # deleteTable
            elif command.strip()[:len('delete')].lower() == 'delete':
                params = [param.strip() for param in command[len('delete'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.deleteTable(params[0][1:-1]) # Quitar commilas del parámetro
            
            # disableTable
            elif command.strip()[:len('disable')].lower() == 'disable':
                params = [param.strip() for param in command[len('disable'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.disableTable(params[0][1:-1]) # Quitar commilas del parámetro
            
            # Is_enabled
            elif command.strip()[:len('is_enabled')].lower() == 'is_enabled':
                params = [param.strip() for param in command[len('is_enabled'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.table_is_enabled(params[0][1:-1]) # Quitar commilas del parámetro
            
            # alterTable
            elif command.strip()[:len('alter')].lower() == 'alter':
                # EJEMPLOS
                # Cambiar nombre de column family
                # ALTER 'Ejemplo', {NAME => 'fam1', NEW_NAME => 'new_fam1}

                # Eliminar column family
                # ALTER 'Ejemplo', {NAME => 'fam1', METHOD => 'delete' }

                params = [param.strip() for param in command[len('alter'):].split(',') if param.strip() != '']
                params = [param.replace(" ", "") for param in params]
                print(params)
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
                        hbase.alterTable(table_name, column_family, delete=True)
                    elif getMethod.upper() == 'NEW_NAME':
                        hbase.alterTable(table_name, column_family, new_name=getMethodValue)
                    else:
                        print(f"@! Error.\n   Details: \n     Funcionalidad de ALTER: Modifica una tabla existente para eliminar o modificar nombre de la column family.\n")

            # dropTable
            elif command.strip()[:len('drop')].lower() == 'drop':
                params = [param.strip() for param in command[len('drop'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.dropTable(params[0][1:-1]) # Quitar comillas
            
            # describeTable
            elif command.strip()[:len('describe')].lower() == 'describe':
                params = [param.strip() for param in command[len('describe'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.describeTable(params[0][1:-1]) # Quitar comillas
            
            # countTable
            elif command.strip()[:len('count')].lower() == 'count':
                params = [param.strip() for param in command[len('count'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.countTable(params[0][1:-1]) # Quitar comillas
            
            # trucateTable
            elif command.strip()[:len('trucate')].lower() == 'trucate':
                params = [param.strip() for param in command[len('trucate'):].split(',') if param.strip() != '']
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")
                else:
                    hbase.truncateTable(params[0][1:-1]) # Quitar comillas

            # create table
            elif command.strip()[:len('create')].lower() == 'create':
                params = [param.strip().strip('\'\"') for param in command[len('create'):].split(',') if param.strip() != '']
                if len(params) < 2 and params[0] == '':
                    print(f"@! Error.\n   Detacreils: \n     Se pasaron {len(params)} parámetros.\n")
                else:
                    hbase.createTable(*params) # Pasar argumentos sin comillas

            # list tables 
            elif command.strip()[:len('list')].lower() == 'list':
                hbase.list()

            #Put data in table
            elif command.strip()[:len('put')].lower() == 'put':
                params = [param.strip() for param in command[len('put'):].split(',') if param.strip() != '']
                
                if len(params) != 5 or (len(params) == 5 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")

                else:   
                    hbase.putTable(params[0][1:-1], params[1][1:-1],params[2][1:-1],params[3][1:-1],params[4][1:-1]) # Quitar comillas

            # scan table
            elif command.strip()[:len('scan')].lower() == 'scan':
                params = [param.strip() for param in command[len('scan'):].split(',') if param.strip() != '']
                
                if len(params) != 1 or (len(params) == 1 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 1 parámetro necesario.\n")

                else:   
                    hbase.scanTable(params[0][1:-1]) # Quitar comillas

#-------------------------------------------------------------------------------------------------------------------
            #get table 
            elif command.strip()[:len('get')].lower() == 'get':
                params = [param.strip() for param in command[len('get'):].split(',') if param.strip() != '']
                
                if len(params) != 2 or (len(params) == 2 and params[0] == ''):
                    print(f"@! Error.\n   Details: \n     Se pasaron {len(params)} parámetros de 2 parámetro necesario.\n")

                else:   
                    hbase.getTable(params[0][1:-1], params[1][1:-1]) # Quitar comillas
           
            #Delete all 
            elif command == 'deleteall':
                print("addd")
                hbase.deleteall()

            elif command == 'Clear' or command == 'clear' or command == 'clr':
                window['-OUTPUT-'].update('')
        # Cerrar la ventana
        window.Close()

if __name__ == '__main__':
    shell = ShellUI()
    shell.run()
