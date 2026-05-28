#!/bin/bash

# ==========================================
# Definición de colores para la terminal
# ==========================================
C_CYAN='\033[1;36m'
C_VERDE='\033[1;32m'
C_AMARILLO='\033[1;33m'
C_MORADO='\033[1;35m'
C_BLANCO='\033[1;37m'
NC='\033[0m' # Sin color (reiniciar)

clear

# ==========================================
# Título Gigante
# ==========================================
echo -e "${C_MORADO}"
echo "██╗   ██╗███╗   ██╗██╗██████╗  █████╗ ███████╗"
echo "██║   ██║████╗  ██║██║██╔══██╗██╔══██╗██╔════╝"
echo "██║   ██║██╔██╗ ██║██║██║  ██║███████║███████╗"
echo "██║   ██║██║╚██╗██║██║██║  ██║██╔══██║╚════██║"
echo "╚██████╔╝██║ ╚████║██║██████╔╝██║  ██║███████║"
echo " ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝"
echo -e "${NC}"

echo -e "${C_CYAN}======================================================${NC}"
echo -e "${C_BLANCO}   Servicio de conteo de personas desaparecidas${NC}"
echo -e "${C_CYAN}======================================================${NC}"
echo ""

# ==========================================
# Integrantes del equipo (Extraídos del README)
# ==========================================
echo -e "${C_AMARILLO}👥 INTEGRANTES DEL EQUIPO:${NC}"
echo ""
echo -e "   ⭐ ${C_BLANCO}Líder:${NC} Indra Cortes"
echo -e "   🐛 ${C_BLANCO}Testing:${NC} Cristian Lopez"
echo -e "   💻 ${C_BLANCO}Ingeniero de Tecnología:${NC} Jorge Bolaños"
echo ""
echo -e "${C_CYAN}------------------------------------------------------${NC}"
echo ""

# ==========================================
# Preparación del Entorno
# ==========================================
echo -e "${C_AMARILLO}⚙️  Preparando el entorno del proyecto...${NC}"
echo ""

if [ ! -d "venv" ]; then
    echo -e "   ${C_BLANCO}[+] No se encontró el entorno virtual. Creándolo por primera vez...${NC}"
    python3 -m venv venv
    
    echo -e "   ${C_BLANCO}[+] Activando el entorno e instalando librerías...${NC}"
    source venv/bin/activate
    pip install -r requirements.txt
    echo ""
    echo -e "   ${C_VERDE}✔️  ¡Instalación completada exitosamente!${NC}"
else
    echo -e "   ${C_VERDE}✔️  Entorno virtual detectado y activado.${NC}"
    source venv/bin/activate
fi

echo ""
echo ""

# ==========================================
# Ejecución del Servidor
# ==========================================
echo -e "${C_CYAN}======================================================${NC}"
echo -e "${C_VERDE}🚀 INICIANDO SERVIDOR WEB EN DJANGO...${NC}"
echo -e "${C_CYAN}======================================================${NC}"
echo ""

python unidx/manage.py runserver
