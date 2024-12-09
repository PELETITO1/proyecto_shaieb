from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context
from django.template import loader


def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")



def probando_template(request):
    nombre = "fede"
    apellido = "Holovay"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}
    # Abrimos el archivo html
    mi_html = open('./plantillas/index.html')
    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())
    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()
    # Creamos un contexto con los datos del diccionario
    mi_contexto = Context(diccionario)
    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
    

def usando_loader(request):
    nombre = "Leandro"
    apellido = "Romero"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
