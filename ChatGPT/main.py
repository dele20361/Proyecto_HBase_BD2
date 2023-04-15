from HBase import HBase

# Crear una instancia de HBase
hbase = HBase()

# Crear una tabla
hbase.create_table('mi_tabla', ['familia1', 'familia2'])

# Verificar que la tabla existe
assert 'mi_tabla' in hbase.list_tables()

# Agregar datos a la tabla
tabla = hbase.get_table('mi_tabla')
tabla.put('row1', {'familia1:columna1': 'valor1', 'familia1:columna2': 'valor2'})
tabla.put('row2', {'familia2:columna3': 'valor3'})

# Obtener un registro de la tabla
assert tabla.get('row1') == {'familia1:columna1': 'valor1', 'familia1:columna2': 'valor2'}

# Hacer una consulta por rango
result = tabla.scan('row1', 'row2')
assert list(result) == [('row1', {'familia1:columna1': 'valor1', 'familia1:columna2': 'valor2'}),
                        ('row2', {'familia2:columna3': 'valor3'})]

# Eliminar una columna
tabla.delete('row1', 'familia1:columna1')
assert tabla.get('row1') == {'familia1:columna2': 'valor2'}

# Eliminar un registro completo
tabla.delete('row2')
assert tabla.get('row2') == {}

# Eliminar una tabla
hbase.drop_table('mi_tabla')
assert 'mi_tabla' not in hbase.list_tables()
