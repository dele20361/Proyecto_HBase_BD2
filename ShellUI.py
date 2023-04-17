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
            [sg.Output(size=(80,20))]
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

            # 
        # Cerrar la ventana
        window.Close()

if __name__ == '__main__':
    shell = ShellUI()
    shell.run()
