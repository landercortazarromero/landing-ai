#!/usr/bin/env python3
"""
SCRIPT DE CLONACIÓN - ELITE JSR
Crea una web de piloto desde la plantilla maestra

Uso:
    python3 clone-pilot.py [NOMBRE-DORSAL]

Ejemplo:
    python3 clone-pilot.py IAN-TRABA-62
"""

import os
import sys
import shutil
from datetime import datetime

# Datos del piloto (RELLENAR antes de ejecutar)
PILOT_DATA = {
    # === DATOS BÁSICOS ===
    "nombre": "NOMBRE DEL PILOTO",
    "apellidos": "APELLIDOS",
    "dorsal": "00",
    "categoria": "Runabout GP3",
    "equipo": "EQUIPO",
    "ciudad": "CIUDAD",
    "nacionalidad": "Española",
    
    # === FRASE HERO ===
    "frase": "TU FRASE AQUÍ",
    
    # === STATS ===
    "titulos": "0",
    "anios_exp": "0",
    "carreras_nac": "0",
    "carreras_eur": "0",
    "carreras_mund": "0",
    "podios": "0",
    
    # === HISTORIA (5 secciones) ===
    "historia_origen": "TU HISTORIA AQUÍ",
    "historia_problema": "TU HISTORIA AQUÍ",
    "historia_apoyo": "TU HISTORIA AQUÍ",
    "historia_superacion": "TU HISTORIA AQUÍ",
    "historia_promesa": "TU HISTORIA AQUÍ",
    
    # === PALMARÉS ===
    "palmares_2025": [
        {"titulo": "Campeón 2025", "competicion": "Campeonato"}
    ],
    "palmares_2024": [
        {"titulo": "Campeón 2024", "competicion": "Campeonato"}
    ],
    "palmares_2023": [
        {"titulo": "Campeón 2023", "competicion": "Campeonato"}
    ],
    
    # === CONTACTO ===
    "email": "email@ejemplo.com",
    "whatsapp": "34600000000",
    "instagram": "@usuario",
    
    # === COLORES (neón por defecto) ===
    "color_neon": "#e5ff00",  # Amarillo neón
    "color_neon_dark": "#b8cc00",
    "color_neon_light": "#f0ff66",
}

def get_pilot_dir():
    """Obtiene el directorio del piloto desde CLI o usa por defecto"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return input("Nombre del cliente (ej: IAN-TRABA-62): ").strip()

def clone_template(pilot_id):
    """Clona la plantilla maestra para un nuevo piloto"""
    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_template = os.path.join(template_dir, "MASTER-TEMPLATE")
    clients_dir = os.path.join(template_dir, "clients")
    new_pilot_dir = os.path.join(clients_dir, pilot_id.upper())
    
    if not os.path.exists(master_template):
        print(f"❌ ERROR: No existe MASTER-TEMPLATE en {master_template}")
        return False
    
    if os.path.exists(new_pilot_dir):
        response = input(f"⚠️  {pilot_id} ya existe. ¿Sobrescribir? (s/n): ")
        if response.lower() != 's':
            print("Cancelado.")
            return False
        shutil.rmtree(new_pilot_dir)
    
    print(f"📦 Clonando plantilla para {pilot_id}...")
    shutil.copytree(master_template, new_pilot_dir)
    
    # Crear estructura de carpetas
    web_dir = os.path.join(new_pilot_dir, "web")
    if not os.path.exists(web_dir):
        os.makedirs(web_dir)
    
    # Copiar index.html
    master_index = os.path.join(master_template, "index.html")
    if os.path.exists(master_index):
        shutil.copy(master_index, web_dir)
    
    # Crear carpetas de imágenes
    for folder in ["hero", "profile", "moto", "podiums", "galeria"]:
        os.makedirs(os.path.join(web_dir, "assets", "images", folder), exist_ok=True)
    
    print(f"✅ Plantilla clonada en: {new_pilot_dir}")
    return True

def apply_pilot_data(pilot_id):
    """Aplica los datos del piloto al index.html"""
    clients_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_dir = os.path.join(clients_dir, pilot_id.upper(), "web", "index.html")
    
    if not os.path.exists(web_dir):
        print(f"❌ ERROR: No existe {web_dir}")
        return False
    
    with open(web_dir, 'r') as f:
        content = f.read()
    
    d = PILOT_DATA
    
    # === APLICAR DATOS ===
    
    # Título y meta
    content = content.replace("CORTAZAR 59 | Lander Cortázar - Piloto Profesional Jetski", 
                            f"{d['nombre'].upper()} {d['dorsal']} | {d['nombre']} {d['apellidos']} - Piloto Profesional Jetski")
    
    # Logo y nombre
    content = content.replace('<span class="name">CORTAZAR</span><span class="number">59</span>', 
                              f'<span class="name">{d["nombre"].upper()}</span><span class="number">{d["dorsal"]}</span>')
    
    # Hero
    content = content.replace('<div class="hero-name">LANDER</div>', f'<div class="hero-name">{d["nombre"].upper()}</div>')
    content = content.replace('<div class="hero-surname">CORTÁZAR</div>', f'<div class="hero-surname">{d["apellidos"].upper()}</div>')
    content = content.replace('<div class="hero-number">59</div>', f'<div class="hero-number">{d["dorsal"]}</div>')
    content = content.replace('"Toda victoria primero se cosecha en la mente..."', f'"{d["frase"]}"')
    content = content.replace('Piloto Profesional - Basque Riders', f'{d["categoria"]} - {d["equipo"]}')
    
    # Stats
    content = content.replace('<span class="stat-number">7</span>', f'<span class="stat-number">{d["titulos"]}</span>')
    content = content.replace('<span class="stat-number">6</span>', f'<span class="stat-number">{d["anios_exp"]}</span>')
    content = content.replace('<span class="stat-number">20+</span>', f'<span class="stat-number">{d["carreras_nac"]}+</span>')
    content = content.replace('<span class="stat-number">10+</span>', f'<span class="stat-number">{d["carreras_eur"]}+</span>')
    content = content.replace('<span class="stat-number">2</span>', f'<span class="stat-number">{d["carreras_mund"]}</span>')
    
    # Historia
    content = content.replace(
        'Lo llevo viviendo desde pequeño con mi padre que siempre ha tenido motos de agua, y fue el quien me animo a empezar a hacerlo yo mismo y afrontar este desafío.',
        d["historia_origen"]
    )
    
    # Contacto
    content = content.replace('cortazar59web@gmail.com', d["email"])
    content = content.replace('@cortazar_59', d["instagram"])
    content = content.replace('34686087467', d["whatsapp"])
    
    # Footer
    content = content.replace('CORTAZAR 59', f'{d["nombre"].upper()} {d["dorsal"]}')
    
    with open(web_dir, 'w') as f:
        f.write(content)
    
    print(f"✅ Datos aplicados a {web_dir}")
    return True

def main():
    print("=" * 50)
    print("🚀 ELITE JSR - CLONADOR DE PLANTILLAS")
    print("=" * 50)
    
    pilot_id = get_pilot_dir()
    
    if not pilot_id:
        print("❌ Nombre de cliente requerido")
        sys.exit(1)
    
    # Clonar
    if clone_template(pilot_id):
        # Aplicar datos
        apply_pilot_data(pilot_id)
        
        print("\n" + "=" * 50)
        print("✅ ¡LISTO!")
        print(f"📁 Proyecto: clients/{pilot_id.upper()}/web/")
        print(f"📝 Edita los datos en PILOT_DATA en este script")
        print(f"🖼️  Añade las fotos en assets/images/")
        print(f"🚀 Despliega con: vercel --prod")
        print("=" * 50)

if __name__ == "__main__":
    main()
