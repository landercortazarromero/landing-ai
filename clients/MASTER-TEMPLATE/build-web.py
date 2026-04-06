#!/usr/bin/env python3
"""
BUILD-WEB.PY - Genera web de piloto desde plantilla maestra
Uso: python3 build-web.py
"""

import re
import os
import sys

# ============================================
# DATOS DEL PILOTO - RELLENAR ESTOS VALORES
# ============================================

DATOS = {
    # SECCIÓN 1: DATOS BÁSICOS
    "NOMBRE_COMPLETO": "",  # ej: "Ian Traba Arce"
    "NOMBRE": "",           # ej: "Ian"
    "APELLIDO": "",         # ej: "Traba"
    "DORSAL": "",           # ej: "62"
    "FECHA_NACIMIENTO": "", # ej: "11/02/2005"
    "NACIONALIDAD": "",     # ej: "Española"
    "CIUDAD": "",           # ej: "Bilbao"
    "CATEGORIA": "",        # ej: "GP3"
    "EQUIPO": "",           # ej: "Basque Riders"
    
    # SECCIÓN 2: HERO
    "FRASE_HERO": "",       # ej: "Esto no es un deporte, es mi estilo de vida"
    
    # SECCIÓN 3: STATS
    "STAT_TITULOS_NUM": "", # ej: "4"
    "STAT_ANOS_NUM": "",    # ej: "5"
    "STAT_PODIUMS_NUM": "", # ej: "18"
    "STAT_CARRERAS_NUM": "",# ej: "20+"
    "STAT_MEDALLAS_NUM": "",# ej: "10+"
    
    # SECCIÓN 4: HISTORIA
    "ORIGEN_TITULO": "",
    "ORIGEN_TEXTO": "",
    "PROBLEMA_TITULO": "",
    "PROBLEMA_TEXTO": "",
    "APOYO_TITULO": "",
    "APOYO_TEXTO": "",
    "SUPERACION_TITULO": "",
    "SUPERACION_TEXTO": "",
    "PROMESA_TITULO": "",
    "PROMESA_TEXTO": "",
    
    # SECCIÓN 5: PALMARÉS (formato: lista de dicts)
    # ej: [{"año": "2025", "títulos": ["🏆 Campeón del Mundo", "🥇 Campeón Europeo"]}]
    "PALMARES": [],
    
    # SECCIÓN 6: FOTOS (número de fotos por tipo)
    "NUM_PODIUMS": 0,       # ej: 9
    "NUM_GALERIA": 0,       # ej: 10
    
    # SECCIÓN 7: CONTACTO
    "EMAIL": "",
    "INSTAGRAM": "",
    "TELEFONO_WHATSAPP": "",
    "MENSAJE_WHATSAPP": "",
    
    # SECCIÓN 8: COLORES
    "COLOR_NEON": "#00d4ff",
}

# ============================================
# FUNCIÓN PRINCIPAL - NO EDITAR ABAJO
# ============================================

def generar_html(datos):
    """Genera el HTML final替换 todos los campos"""
    
    # Leer HTML base
    html_path = "web/index.html"
    if not os.path.exists(html_path):
        print(f"❌ Error: No existe {html_path}")
        sys.exit(1)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. TÍTULO Y META
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>{datos["NOMBRE"]} {datos["APELLIDO"]} {datos["DORSAL"]} | Piloto Profesional Jetski</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{datos["NOMBRE"]} {datos["APELLIDO"]} #{datos["DORSAL"]} - Piloto profesional de Jetski {datos["CATEGORIA"]}">',
        html
    )
    
    # 2. HEADER
    html = re.sub(
        r'<span class="name">.*?</span><span class="number">.*?</span>',
        f'<span class="name" style="color: #ffffff;">{datos["NOMBRE"]} {datos["APELLIDO"]}</span><span class="number" style="color: var(--neon);">{datos["DORSAL"]}</span>',
        html
    )
    
    # 3. HERO
    html = re.sub(
        r'<div class="hero-name">.*?</div>\s*<div class="hero-surname">.*?</div>',
        f'<div class="hero-name">{datos["NOMBRE"]}</div>\n            <div class="hero-surname">{datos["APELLIDO"].upper()}</div>',
        html
    )
    html = re.sub(
        r'<div class="hero-subtitle">.*?</div>',
        f'<div class="hero-subtitle">{datos["CATEGORIA"]} - {datos["EQUIPO"]}</div>',
        html
    )
    html = re.sub(
        r'<div class="hero-quote">.*?</div>',
        f'<div class="hero-quote">"{datos["FRASE_HERO"]}"</div>',
        html
    )
    
    # 4. STATS
    stats_map = [
        ("7", datos["STAT_TITULOS_NUM"]),  # Títulos
        ("6", datos["STAT_ANOS_NUM"]),     # Años
        ("20+", datos["STAT_PODIUMS_NUM"]), # Podiums
        ("10+", datos["STAT_CARRERAS_NUM"]),# Carreras
        ("2", datos["STAT_MEDALLAS_NUM"]),  # Medallas
    ]
    for old, new in stats_map:
        html = html.replace(f'<span class="stat-number">{old}</span>', f'<span class="stat-number">{new}</span>')
    
    # 5. INFO PERSONAL
    html = html.replace('<div class="info-value">11/12/1991</div>', f'<div class="info-value">{datos["FECHA_NACIMIENTO"]}</div>')
    html = html.replace('<div class="info-value">España</div>', f'<div class="info-value">{datos["NACIONALIDAD"]}</div>')
    html = html.replace('<div class="info-value">Durango, Bizkaia</div>', f'<div class="info-value">{datos["CIUDAD"]}</div>')
    html = html.replace('<div class="info-value">Runabout GP2</div>', f'<div class="info-value">{datos["CATEGORIA"]}</div>')
    html = html.replace('<div class="info-value">Basque Riders</div>', f'<div class="info-value">{datos["EQUIPO"]}</div>')
    html = re.sub(r'alt="Lander Cortázar"', f'alt="{datos["NOMBRE_COMPLETO"]}"', html)
    
    # 6. HISTORIA
    historia = f'''
                    <div class="story-section">
                        <h4 style="color: var(--neon); font-family: 'Orbitron', sans-serif; font-size: 1.3rem; margin: 30px 0 15px 0;">{datos["ORIGEN_TITULO"]}</h4>
                        <p>{datos["ORIGEN_TEXTO"]}</p>
                    </div>
                    
                    <div class="story-section">
                        <h4 style="color: var(--neon); font-family: 'Orbitron', sans-serif; font-size: 1.3rem; margin: 30px 0 15px 0;">{datos["PROBLEMA_TITULO"]}</h4>
                        <p>{datos["PROBLEMA_TEXTO"]}</p>
                    </div>
                    
                    <div class="story-section">
                        <h4 style="color: var(--neon); font-family: 'Orbitron', sans-serif; font-size: 1.3rem; margin: 30px 0 15px 0;">{datos["APOYO_TITULO"]}</h4>
                        <p>{datos["APOYO_TEXTO"]}</p>
                    </div>
                    
                    <div class="story-section">
                        <h4 style="color: var(--neon); font-family: 'Orbitron', sans-serif; font-size: 1.3rem; margin: 30px 0 15px 0;">{datos["SUPERACION_TITULO"]}</h4>
                        <p>{datos["SUPERACION_TEXTO"]}</p>
                    </div>
                    
                    <div class="story-section" style="background: rgba(0, 212, 255, 0.05); border-left: 3px solid var(--neon); padding: 25px; margin: 30px 0; border-radius: 0 15px 15px 0;">
                        <h4 style="color: var(--neon); font-family: 'Orbitron', sans-serif; font-size: 1.4rem; margin-bottom: 15px;">{datos["PROMESA_TITULO"]}</h4>
                        <p>{datos["PROMESA_TEXTO"]}</p>
                    </div>'''
    
    html = re.sub(
        r'<div class="about-text">.*?</div>\s*</div>\s*</div>',
        f'<div class="about-text">\n                        {historia}\n                    </div>\n                </div>\n            </div>',
        html,
        flags=re.DOTALL
    )
    
    # 7. PALMARÉS
    palmares_html = ""
    for item in datos["PALMARES"]:
        titulos_html = ""
        for titulo in item["títulos"]:
            titulos_html += f'''
                    <div class="timeline-content">
                        <div class="timeline-title">{titulo}</div>
                        <div class="timeline-competition">{datos["CATEGORIA"]}</div>
                    </div>'''
        
        palmares_html += f'''
                <div class="timeline-item">
                    <div class="timeline-year">{item["año"]}</div>
                    {titulos_html}
                </div>'''
    
    html = re.sub(
        r'<div class="palmares-timeline">.*?</div>\s*</div>\s*</section>',
        f'<div class="palmares-timeline">\n                {palmares_html}\n            </div>\n        </div>\n    </section>',
        html,
        flags=re.DOTALL
    )
    
    # 8. PODIUMS
    podiums_html = ""
    for i in range(1, datos["NUM_PODIUMS"] + 1):
        podiums_html += f'\n                <div class="gallery-item"><img src="images/podium{i}.jpg" alt="Podium {i}"></div>'
    
    html = re.sub(
        r'<div class="gallery-grid">.*?</div>\s*</div>\s*</section>',
        f'<div class="gallery-grid">\n                {podiums_html}\n            </div>\n        </div>\n    </section>',
        html,
        flags=re.DOTALL
    )
    
    # 9. GALERÍA
    galeria_html = ""
    for i in range(1, datos["NUM_GALERIA"] + 1):
        galeria_html += f'\n                <div class="gallery-item"><img src="images/galeria{i}.jpg" alt="Galería {i}"></div>'
    
    html = re.sub(
        r'(id="galeria".*?<div class="gallery-grid">).*?(</div>\s*</div>\s*</section>)',
        rf'\1\n                {galeria_html}\n            </div>\n        </div>\n    </section>',
        html,
        flags=re.DOTALL
    )
    
    # 10. CONTACTO
    html = html.replace('landercortazarromero@gmail.com', datos["EMAIL"])
    html = html.replace('@cortazar_59', datos["INSTAGRAM"])
    html = re.sub(r'tel:34686087467', f'tel:{datos["TELEFONO_WHATSAPP"]}', html)
    html = re.sub(r'https://wa\.me/34686087467.*?"', f'https://wa.me/{datos["TELEFONO_WHATSAPP"]}?text={datos["MENSAJE_WHATSAPP"]}"', html)
    html = html.replace('Durango, Bizkaia', datos["CIUDAD"])
    
    # 11. FOOTER
    html = re.sub(r'CORTAZAR <span>.*?</span>', f'{datos["NOMBRE"]} {datos["APELLIDO"]} <span style="color: var(--neon);">#{datos["DORSAL"]}</span>', html)
    html = re.sub(r'© 2025 Lander Cortázar Romero', f'© 2025 {datos["NOMBRE_COMPLETO"]}', html)
    
    # 12. COLORES
    color = datos["COLOR_NEON"]
    color_dark = adjust_color(color, -30)
    color_light = adjust_color(color, 30)
    html = html.replace('#e5ff00', color)
    html = html.replace('#b8cc00', color_dark)
    html = html.replace('#f0ff66', color_light)
    html = html.replace('rgba(229, 255, 0, ', f'rgba{tuple([int(color[i:i+2], 16) for i in [1, 3, 5]] + [0.05])}'.replace('(', '(').replace(')', ''))
    
    return html

def adjust_color(hex_color, amount):
    """Ajusta el brillo de un color hex"""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    new_rgb = tuple(max(0, min(255, c + amount)) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*new_rgb)

def main():
    print("🎯 GENERANDO WEB DEL PILOTO...")
    print()
    
    # Verificar que tenemos todos los datos mínimos
    required = ["NOMBRE", "APELLIDO", "DORSAL", "EMAIL"]
    missing = [k for k in required if not DATOS[k]]
    if missing:
        print(f"❌ Faltan datos obligatorios: {missing}")
        print("❌ Edita build-web.py y rellena los campos DATOS")
        sys.exit(1)
    
    # Generar HTML
    html = generar_html(DATOS)
    
    # Guardar
    output_path = "web/index.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Web generada: {output_path}")
    print()
    print(f"📋 Resumen:")
    print(f"   - Piloto: {DATOS['NOMBRE']} {DATOS['APELLIDO']} #{DATOS['DORSAL']}")
    print(f"   - Categoría: {DATOS['CATEGORIA']}")
    print(f"   - Palmarés: {len(DATOS['PALMARES'])} años")
    print(f"   - Fotos: {DATOS['NUM_PODIUMS']} podiums, {DATOS['NUM_GALERIA']} galería")

if __name__ == "__main__":
    main()
