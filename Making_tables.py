from HBase import HBase
import json

with open('TablesInfo/Musica.json', 'r') as f:
    contenido = json.loads(f.read())


hb = HBase()
hb.createTable("Musica","information","interacction")
table_name = "Musica"
family_name1 = "information"
family_name2 = "interacction"

for item in contenido:
    row_key = (item['_id']['$oid'])
    titulo = (item['titulo'])
    artista = (item['artista'])
    genero = (item['genero'])
    duracion = (item['duracion'])
    fecha_de_publicacion = (item['fecha_de_publicacion'])
    likes = (item['likes'])

    if 'comentarios' in item:
            comentarios = item['comentarios']
    else:
        comentarios = []

    hb.putTable(table_name,row_key,family_name1,'titulo',titulo)
    hb.putTable(table_name,row_key,family_name1,'artista',artista)
    hb.putTable(table_name,row_key,family_name1,'genero',genero)
    hb.putTable(table_name,row_key,family_name1,'duracion',duracion)
    hb.putTable(table_name,row_key,family_name1,'fecha_de_publicacion',fecha_de_publicacion)

    hb.putTable(table_name,row_key,family_name2,'likes',likes)
    hb.putTable(table_name,row_key,family_name2,'comentarios',comentarios)

    #print(row_key)
print("\n\n")
hb.scanTable(table_name) 

