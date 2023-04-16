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
            try:
                #TODO: Procesar los input llamando a las funciones hechas.
                if command == 'hola':
                    result = 'adiós'
                print(result)
            except Exception as e:
                print(f"Error: {e}")
        
        # Cerrar la ventana
        window.Close()

if __name__ == '__main__':
    shell = ShellUI()
    shell.run()
