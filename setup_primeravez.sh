#!/bin/bash
echo "========================================="
echo "Iniciando servidor Unidas..."
echo "========================================="

echo "1. Instalando dependencias"
pip install -r requirements.txt

echo "Importando datos..."
python unidx/manage.py makemigrations
python unidx/manage.py migrate

echo "========================================="
echo "Listo ahora corre iniciar_servidor.sh"
echo "========================================="
