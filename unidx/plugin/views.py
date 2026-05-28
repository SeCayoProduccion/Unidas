from django.shortcuts import render
from django.conf import settings
from .models import Visitante
import pandas as pd
import os

def home(request):
    # Es la pagina de inicio... o sea, el index.html que Indra creo
    return render(request, 'plugin/index.html')

##### AQUI VAN LAS OTRAS PAGINAS
def negocio(request):
    return render(request, 'plugin/negocio.html')

##### HISTORIAL DE VISITANTES
def visitantes(request):
    # Ordenar por fecha
    historial = Visitante.objects.all().order_by('-fecha')
    return render(request, 'plugin/visitantes.html', {'historial': historial})

# búsqueda
def busqueda(request):
    # Si el usuario le dio al boton de 'Buscar' es un POST
    if request.method == 'POST':
        edad = request.POST.get('edad', '')
        estado = request.POST.get('estado', '').upper()
        genero = request.POST.get('genero', '')

        # Aquí se guarda lo que buscó pero sin el nombre
        Visitante.objects.create(
            sexo=genero,
            edad=edad,
            estado=estado
        )
        # Género
        sexo_csv = "MUJER" if genero == "femenino" else "HOMBRE"
        # Abrir el CSV
        ruta_csv = os.path.abspath(os.path.join(settings.BASE_DIR, 'RNPDNO-22-08-2023-limpio.csv'))
        df = pd.read_csv(ruta_csv, encoding="latin-1")

        # Filtrar por estado y genero
        filtro = df[(df["Entidad de desaparición"] == estado) & (df["Sexo"] == sexo_csv)]
        if edad: # Filtra x edad
            try:
                filtro = filtro[filtro["Edad"] == int(edad)]
            except:
                pass
        total_desapariciones = len(filtro)
        # Le pasa los resultados a la página
        return render(request, 'plugin/busqueda.html', {
            'total': total_desapariciones,
            'estado': estado,
            'busqueda_realizada': True
        })
    # Si el usuario no hizo una consulta y solo entró a ver el form
    return render(request, 'plugin/busqueda.html')
