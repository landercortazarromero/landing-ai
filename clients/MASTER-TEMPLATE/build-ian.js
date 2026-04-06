#!/usr/bin/env node
/**
 * BUILD-IAN.JS - Genera web de Ian Traba desde plantilla maestra LIMPIA
 * SIN COPIAR NADA DE OTRAS WEBS
 */

const fs = require('fs');
const path = require('path');

// DATOS DE IAN - SOLO ESTOS DATOS
const IAN = {
    NOMBRE: 'Ian',
    APELLIDO: 'Traba',
    NOMBRE_COMPLETO: 'Ian Traba Arce',
    DORSAL: '62',
    FECHA_NACIMIENTO: '11/02/2005',
    NACIONALIDAD: 'Española',
    CIUDAD: 'Bilbao',
    CATEGORIA: 'GP3',
    EQUIPO: 'Basque Riders',
    FRASE_HERO: 'Esto no es un deporte, es mi estilo de vida',
    
    STAT_TITULOS: '4',
    STAT_ANOS: '5',
    STAT_PODIUMS: '18',
    STAT_CARRERAS: '20+',
    STAT_MEDALLAS: '10+',
    
    ORIGEN_TITULO: 'EL ORIGEN',
    ORIGEN_TEXTO: 'Empecé en 2020 cuando me animó mi padre a comenzar en este deporte. Lo llevo viviendo desde pequeño con mi padre que siempre ha tenido motos de agua, y fue él quien me animó.',
    
    PROBLEMA_TITULO: 'EL PROBLEMA',
    PROBLEMA_TEXTO: 'La lesión en la que sigo aunque ya estoy en la recta final. Han sido meses complicados en los que te desmoralizas, pero siempre hay que tirar para adelante.',
    
    APOYO_TITULO: 'EL APOYO',
    APOYO_TEXTO: 'Mi padre siempre, el que más me anima y más me ayuda en ese sentido para que no me venga abajo nunca.',
    
    SUPERACION_TITULO: 'LA SUPERACIÓN',
    SUPERACION_TEXTO: 'Estoy en ello, pero sé que volveré más fuerte y entrenaré mucho para estar al máximo nivel.',
    
    PROMESA_TITULO: 'MI PROMESA',
    PROMESA_TEXTO: 'Porque veo que se me da bien y me gusta, es lo que me hace feliz.',
    
    EMAIL: 'trabaian62@gmail.com',
    INSTAGRAM: '@iantraba_62',
    TELEFONO_WHATSAPP: '34647325346',
    MENSAJE_WHATSAPP: 'Hola%20Ian%2C%20vi%20tu%20pagina%20deportiva%20y%20quiero%20apoyarte',
    
    COLOR_NEON: '#00d4ff',
    COLOR_NEON_DARK: '#0099cc',
    COLOR_NEON_LIGHT: '#66e0ff',
    
    PALMARES: [
        { año: '2025', titulos: ['🏆 Campeón del Mundo', '🥇 Campeón España Rallyjet y Offshore', '🥇 Campeón Euskadi'] },
        { año: '2024', titulos: ['🥇 Campeón España', '🥇 Campeón Euskadi'] },
        { año: '2023', titulos: ['🥇 Campeón España', '🥇 Campeón Europeo'] }
    ],
    
    NUM_PODIUMS: 8,
    NUM_GALERIA: 10
};

// Plantilla paths
const TEMPLATE_DIR = path.join(__dirname);
const OUTPUT_FILE = path.join(TEMPLATE_DIR, 'web', 'index.html');
const IMAGES_DIR = path.join(TEMPLATE_DIR, 'web', 'images');

console.log('🎯 Generando web de Ian Traba #62...');
console.log('');

// Leer plantilla
let html = fs.readFileSync(OUTPUT_FILE, 'utf8');

// Reemplazar TODOS los placeholders
const replacements = {
    '[NOMBRE]': IAN.NOMBRE,
    '[APELLIDO]': IAN.APELLIDO,
    '[NOMBRE_COMPLETO]': IAN.NOMBRE_COMPLETO,
    '[DORSAL]': IAN.DORSAL,
    '[FECHA_NACIMIENTO]': IAN.FECHA_NACIMIENTO,
    '[NACIONALIDAD]': IAN.NACIONALIDAD,
    '[CIUDAD]': IAN.CIUDAD,
    '[CATEGORIA]': IAN.CATEGORIA,
    '[EQUIPO]': IAN.EQUIPO,
    '[FRASE_HERO]': IAN.FRASE_HERO,
    '[STAT_TITULOS]': IAN.STAT_TITULOS,
    '[STAT_ANOS]': IAN.STAT_ANOS,
    '[STAT_PODIUMS]': IAN.STAT_PODIUMS,
    '[STAT_CARRERAS]': IAN.STAT_CARRERAS,
    '[STAT_MEDALLAS]': IAN.STAT_MEDALLAS,
    '[ORIGEN_TITULO]': IAN.ORIGEN_TITULO,
    '[ORIGEN_TEXTO]': IAN.ORIGEN_TEXTO,
    '[PROBLEMA_TITULO]': IAN.PROBLEMA_TITULO,
    '[PROBLEMA_TEXTO]': IAN.PROBLEMA_TEXTO,
    '[APOYO_TITULO]': IAN.APOYO_TITULO,
    '[APOYO_TEXTO]': IAN.APOYO_TEXTO,
    '[SUPERACION_TITULO]': IAN.SUPERACION_TITULO,
    '[SUPERACION_TEXTO]': IAN.SUPERACION_TEXTO,
    '[PROMESA_TITULO]': IAN.PROMESA_TITULO,
    '[PROMESA_TEXTO]': IAN.PROMESA_TEXTO,
    '[EMAIL]': IAN.EMAIL,
    '[INSTAGRAM]': IAN.INSTAGRAM,
    '[TELEFONO_WHATSAPP]': IAN.TELEFONO_WHATSAPP,
    '[MENSAJE_WHATSAPP]': IAN.MENSAJE_WHATSAPP,
    '[COLOR_NEON]': IAN.COLOR_NEON,
    '[COLOR_NEON_DARK]': IAN.COLOR_NEON_DARK,
    '[COLOR_NEON_LIGHT]': IAN.COLOR_NEON_LIGHT
};

// Aplicar reemplazos simples
for (const [placeholder, value] of Object.entries(replacements)) {
    html = html.split(placeholder).join(value);
}

// Generar Palmares
let palmaresHtml = '';
for (const item of IAN.PALMARES) {
    let titulosHtml = '';
    for (const titulo of item.titulos) {
        titulosHtml += `
                    <div class="timeline-content">
                        <div class="timeline-title">${titulo}</div>
                        <div class="timeline-competition">${IAN.CATEGORIA}</div>
                    </div>`;
    }
    palmaresHtml += `
                <div class="timeline-item">
                    <div class="timeline-year">${item.año}</div>
                    ${titulosHtml}
                </div>`;
}

html = html.replace('<!-- Palmares items will be dynamically generated -->', palmaresHtml);

// Generar Podiums
let podiumsHtml = '';
for (let i = 1; i <= IAN.NUM_PODIUMS; i++) {
    podiumsHtml += `
                <div class="gallery-item">
                    <img src="images/podium${i}.jpg" alt="Podium ${i}">
                </div>`;
}

html = html.replace('<!-- Podium images will be dynamically generated -->', podiumsHtml);

// Generar Galería
let galeriaHtml = '';
for (let i = 1; i <= IAN.NUM_GALERIA; i++) {
    galeriaHtml += `
                <div class="gallery-item">
                    <img src="images/galeria${i}.jpg" alt="Galería ${i}">
                </div>`;
}

html = html.replace('<!-- Gallery images will be dynamically generated -->', galeriaHtml);

// Guardar
fs.writeFileSync(OUTPUT_FILE, html, 'utf8');

console.log('✅ Web generada!');
console.log('');
console.log('📋 Datos aplicados:');
console.log(`   - Nombre: ${IAN.NOMBRE} ${IAN.APELLIDO} #${IAN.DORSAL}`);
console.log(`   - Categoría: ${IAN.CATEGORIA} - ${IAN.EQUIPO}`);
console.log(`   - Ciudad: ${IAN.CIUDAD}`);
console.log(`   - Palmarés: ${IAN.PALMARES.length} años`);
console.log(`   - Podiums: ${IAN.NUM_PODIUMS} fotos`);
console.log(`   - Galería: ${IAN.NUM_GALERIA} fotos`);
console.log('');
console.log('⚠️  IMPORTANTE: Copiar las fotos a web/images/ antes de desplegar!');
