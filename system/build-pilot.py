#!/usr/bin/env python3
"""
HYBRID LABS - PILOT WEB BUILDER
================================
Builds a clean pilot web from template + data

Usage:
    python3 build-pilot.py [pilot-folder]
    
Example:
    python3 build-pilot.py IAN-TRABA-62
"""

import os
import sys
import json
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates', 'MASTER-TEMPLATE')
PILOT_PROFILES = os.path.join(BASE_DIR, 'pilot-profiles')

def load_pilot_data(pilot_name):
    """Load pilot data from JSON"""
    json_path = os.path.join(PILOT_PROFILES, f'{pilot_name}.json')
    if not os.path.exists(json_path):
        print(f"❌ No data found: {json_path}")
        sys.exit(1)
    
    with open(json_path, 'r') as f:
        return json.load(f)

def copy_template(pilot_name):
    """Copy clean template to pilot folder"""
    pilot_dir = os.path.join(BASE_DIR, '..', 'clients', pilot_name)
    
    # Clean if exists
    if os.path.exists(pilot_dir):
        shutil.rmtree(pilot_dir)
    
    # Copy fresh template
    shutil.copytree(TEMPLATE_DIR, pilot_dir)
    print(f"✅ Template copied to: {pilot_dir}")
    return pilot_dir

def build_html(pilot_dir, data):
    """Replace all placeholders with pilot data"""
    html_path = os.path.join(pilot_dir, 'web', 'index.html')
    
    with open(html_path, 'r') as f:
        html = f.read()
    
    # Replace core data
    replacements = {
        'COLOR_NEON': data['pilot']['colorNeon'],
        'NOMBRE_COMPLETO': data['pilot']['nombre'],
        'NOMBRE': data['pilot']['nombreCorto'],
        'DORSAL': str(data['pilot']['dorsal']),
        'FRASE_HERO': data['pilot']['frase'],
        'EMAIL': data['pilot'].get('email', ''),
        'INSTAGRAM': data['pilot'].get('instagram', ''),
        'WHATSAPP': data['pilot'].get('whatsapp', ''),
        'CIUDAD': data['pilot'].get('ciudad', ''),
    }
    
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    
    # Build stats
    stats_html = f'''
    <div style="text-align: center;">
        <div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: {data['pilot']['colorNeon']};">{data['stats']['titulos']}</div>
        <div style="font-size: 0.9rem; color: var(--gray); letter-spacing: 2px;">TÍTULOS</div>
    </div>
    <div style="text-align: center;">
        <div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: {data['pilot']['colorNeon']};">{data['stats']['anios']}</div>
        <div style="font-size: 0.9rem; color: var(--gray); letter-spacing: 2px;">AÑOS</div>
    </div>
    <div style="text-align: center;">
        <div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: {data['pilot']['colorNeon']};">{data['stats']['podiums']}</div>
        <div style="font-size: 0.9rem; color: var(--gray); letter-spacing: 2px;">PODIUMS</div>
    </div>
    <div style="text-align: center;">
        <div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: {data['pilot']['colorNeon']};">{data['stats']['victorias']}</div>
        <div style="font-size: 0.9rem; color: var(--gray); letter-spacing: 2px;">VICTORIAS</div>
    </div>
    '''
    
    # Find and replace stats block (rough pattern)
    import re
    stats_pattern = r'<div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">\d+</div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">TÍTULOS</div></div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">\d+</div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">AÑOS</div></div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">\d+</div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">PODIUMS</div></div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">\d+</div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">VICTORIAS</div></div>'
    html = re.sub(stats_pattern, stats_html.strip(), html)
    
    # Build historia
    historia = f"""
    {data['historia']['parrafo1']}
    
    {data['historia']['parrafo2']}
    
    {data['historia']['parrafo3']}
    
    {data['historia']['parrafo4']}
    
    {data['historia']['parrafo5']}
    """
    html = html.replace('HISTORIA', historia.strip())
    
    # Build palmares
    palmares_html = ''
    for entry in data['palmares']:
        palmares_html += f'''<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba{entry['titulo'], entry['anyo']})};">
            <span style="color: var(--light);">{entry['titulo']} - {entry['categoria']}</span>
            <span style="color: {data['pilot']['colorNeon']}; font-family: Orbitron; font-weight: 700;">{entry['anyo']}</span>
        </div>'''
    
    # Replace palmares block
    palmares_pattern = r'<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">[^<]+</span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">[^<]+</span></div>'
    html = re.sub(palmares_pattern, palmares_html.strip(), html)
    
    with open(html_path, 'w') as f:
        f.write(html)
    
    print(f"✅ HTML built with all data")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 build-pilot.py [pilot-folder]")
        print("Example: python3 build-pilot.py IAN-TRABA-62")
        sys.exit(1)
    
    pilot_name = sys.argv[1]
    
    print(f"🚀 Building web for: {pilot_name}")
    
    # Step 1: Load data
    print("📋 Loading pilot data...")
    data = load_pilot_data(pilot_name)
    
    # Step 2: Copy template
    print("📁 Copying clean template...")
    pilot_dir = copy_template(pilot_name)
    
    # Step 3: Copy photos
    print("📸 Copying photos...")
    photos_dir = os.path.join(pilot_dir, 'web', 'images')
    if os.path.exists(photos_dir):
        shutil.rmtree(photos_dir)
    shutil.copytree(os.path.join(PILOT_PROFILES, pilot_name, 'photos'), photos_dir)
    
    # Step 4: Build HTML
    print("🔨 Building HTML...")
    build_html(pilot_dir, data)
    
    print(f"✅ Build complete: {pilot_dir}")
    print(f"📝 Next: Deploy with 'vercel --prod --force --name {pilot_name.lower()}'")

if __name__ == '__main__':
    main()
