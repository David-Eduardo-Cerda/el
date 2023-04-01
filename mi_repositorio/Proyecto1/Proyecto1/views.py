from django.http import HttpResponse
import datetime
#from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo")


def dia_de_hoy(request):

    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es el dia : <br> {dia}"

    return HttpResponse(documentoDeTexto)

def anionac(request,tuanio):
    anio_actual = datetime.datetime.today().month
    return HttpResponse(f"{anio_actual}")


