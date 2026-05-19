from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyUserForm
import pandas as pd
import os
from django.conf import settings

# Aqui estamos creamdo la funcion principal.... es el cerebro o el corazon del formulario.... aqui es donde le pregunta al usuario
def MyUserView(request):
    # ¿El usuario hizo clic en el botón "Enviar"? (POST)
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            # 1. Sacamos los datos del formulario
            datos_usuario = form.cleaned_data
            entidad_buscada = datos_usuario['entidad'].upper() # Lo pasamos a mayúsculas como en el CSV
            
            # 2. Abrimos el CSV para buscar la estadística
            # Esta es la lógica que tenías en Consulta.py
            ruta_csv = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'RNPDNO-22-08-2023-limpio.csv'))
            df = pd.read_csv(ruta_csv, encoding="latin-1")
            
            # Filtramos por el estado que el usuario escribió
            filtro = df[df["Entidad de desaparición"] == entidad_buscada]
            total_desapariciones = len(filtro)

            # 3. Le respondemos al usuario con el resultado
            return HttpResponse(f"Hola {datos_usuario['nombre']}, en {entidad_buscada} hay un registro de {total_desapariciones} desapariciones. Estamos calculando tu nivel de riesgo...")
            
    else:
        # Si el usuario solo entró a la página, le mostramos el formulario vacío
        form = MyUserForm()
    
    # Enviamos el formulario al archivo HTML
    return render(request, 'plugin/api.html', {'form': form})
