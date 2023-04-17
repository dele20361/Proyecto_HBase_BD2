from HBase import HBase
import json

def Music_table():
    with open('TablesInfo/Musica.json', 'r') as f:
        contenido = json.loads(f.read())

    hb = HBase()
    hb.createTable("Musica","information","interacction")
    table_name = "Musica"
    family_name1 = "information"
    family_name2 = "interacction"

    for item in contenido:
        row_key = (item['artista'])
        titulo = (item['titulo'])
        genero = (item['genero'])
        duracion = (item['duracion'])
        fecha_de_publicacion = (item['fecha_de_publicacion'])
        likes = (item['likes'])


        hb.putTable(table_name,row_key,family_name1,'titulo',titulo)
        hb.putTable(table_name,row_key,family_name1,'genero',genero)
        hb.putTable(table_name,row_key,family_name1,'duracion',duracion)
        hb.putTable(table_name,row_key,family_name1,'fecha_de_publicacion',fecha_de_publicacion)

        hb.putTable(table_name,row_key,family_name2,'likes',likes)


    #print(row_key)

def Users_table():
    with open('TablesInfo/Usuarios.json', 'r',encoding='utf-8') as f:
            contenido = json.loads(f.read())

    hb = HBase()
    hb.createTable("Usuarios","personal_data","account")
    table_name = "Usuarios"
    family_name1 = "personal_data"
    family_name2 = "account"

    for item in contenido:
        row_key = (item['username'])
        nombre = (item['nombre'])
        apellido = (item['apellido'])
        sexo = (item['sexo'])
        region = (item['region'])

        
        contraseña = (item['contraseña'])
        email = (item['email'])
        Seguidores = (item['Seguidores'])

        hb.putTable(table_name,row_key,family_name1,'nombre',nombre)
        hb.putTable(table_name,row_key,family_name1,'apellido',apellido)
        hb.putTable(table_name,row_key,family_name1,'sexo',sexo)
        hb.putTable(table_name,row_key,family_name1,'region',region)

    
        hb.putTable(table_name,row_key,family_name2,'contraseña',contraseña)
        hb.putTable(table_name,row_key,family_name2,'email',email)
        hb.putTable(table_name,row_key,family_name2,'Seguidores',Seguidores)


Music_table()
Users_table()

