from django.shortcuts import render
from django.conf import settings
from .models import Visitante
import pandas as pd
import os

def home(request):
    # Es la pagina de inicio... osea el index.html que Indra creo
    return render(request, 'plugin/index.html')

##### AQUI VAN LAS OTRAS PAGINAS

def negocio(request):
    return render(request, 'plugin/negocio.html')

##### HISTORIAL DE VISITANTES

def visitantes(request):
    # Ordenar por fecha
    historial = Visitante.objects.all().order_by('-fecha')
    

    return render(request, 'plugin/visitantes.html', {'historial': historial})

#####

def busqueda(request):
    # Si el usuario le dio al boton de Buscar (POST)
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        edad = request.POST.get('edad', '')
        estado = request.POST.get('estado', '').upper()
        genero = request.POST.get('genero', '')

        # Guardamos el nombre en el historial de visitantes de la base de datos
        if nombre:
            Visitante.objects.create(nombre=nombre)

        # Genero
        sexo_csv = "MUJER" if genero == "femenino" else "HOMBRE"

        # Abrir el CSV
        ruta_csv = os.path.abspath(os.path.join(settings.BASE_DIR, 'RNPDNO-22-08-2023-limpio.csv'))
        df = pd.read_csv(ruta_csv, encoding="latin-1")

        # Filtrar por estado y genero
        filtro = df[(df["Entidad de desaparición"] == estado) & (df["Sexo"] == sexo_csv)]

        # Si el usuario puso su edad, filtramos tambien por eso
        if edad:
            try:
                filtro = filtro[filtro["Edad"] == int(edad)]
            except:
                pass

        total_desapariciones = len(filtro)

        # Regresamos a la pagina pasandole los resultados
        return render(request, 'plugin/busqueda.html', {
            'total': total_desapariciones,
            'estado': estado,
            'nombre': nombre,
            'busqueda_realizada': True
        })

    # Si el usuario solo entro a la pagina a verla (GET)
    return render(request, 'plugin/busqueda.html')
