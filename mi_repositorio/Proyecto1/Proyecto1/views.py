from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo")


def dia_de_hoy(request):

    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es el dia : <br> {dia}"

    return HttpResponse(documentoDeTexto)

def anionac(request,tuanio):
    anio_actual = datetime.datetime.today().month
    return HttpResponse(f"{anio_actual}")


def probandoTemple(self):

    miHtml = open("C:/Users/David/Desktop/escritorio/projectos Django/Pro1 Django/mi_repositorio/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
