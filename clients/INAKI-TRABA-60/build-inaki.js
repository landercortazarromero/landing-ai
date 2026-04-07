const fs = require('fs');
const path = require('path');

const data = {
    nombre: 'IÑAKI TRABA',
    nombreDisplay: 'IÑAKI',
    dorsal: '60',
    frase: 'Con esfuerzo y sacrificio se logran resultados',
    color: '#00ff88',
    stats: [
        { num: '7', label: 'TÍTULOS' },
        { num: '15+', label: 'AÑOS' },
        { num: '20+', label: 'PODIUMS' },
        { num: '17', label: 'VICTORIAS' }
    ],
    historia: `Todo empezó con mi hermano mayor. Él siempre fue más rápido, más fuerte, más seguro. Yo lo seguía a todas partes, queriendo ser como él.

Un problema con la vista me apartó durante tres meses. Tres meses sin competir, sin entrenar, sin ser yo mismo. Pensé que mi carrera había terminado antes de empezar.

Fue mi hermano quien me tendió la mano. Me dejó su bicicleta para que pudiera salir con él, para que no perdiera el ritmo. Ese gesto lo cambió todo.

Me di cuenta de que si se quiere de verdad cualquier cosa se puede conseguir. Que las barreras no existen si el corazón está puesto.

Hoy compito porque compartir este hobby con mi hijo es lo más grande que he vivido. Cada metro recorrido es un regalo. Cada victoria, un homenaje a los que creyeron cuando yo mismo dejé de hacerlo.`,
    palmares: [
        { titulo: 'CAMPEÓN DE ESPAÑA RALLYJET GP2', anyo: '2010' },
        { titulo: 'CAMPEÓN DE ESPAÑA RALLYJET GP1 ATMOS', anyo: '2022' },
        { titulo: 'CAMPEÓN DE ESPAÑA RALLYJET GP3', anyo: '2023' },
        { titulo: 'CAMPEÓN DE ESPAÑA RALLYJET GP1 ATMOS', anyo: '2023' },
        { titulo: 'CAMPEÓN DE ESPAÑA OFFSHORE GP2', anyo: '2010' },
        { titulo: 'CAMPEÓN DE ESPAÑA OFFSHORE GP1 ATMOS', anyo: '2022' }
    ]
};

let html = fs.readFileSync(path.join(__dirname, 'web', 'index.html'), 'utf8');

html = html.replace(/COLOR_NEON/g, data.color);
html = html.replace(/NOMBRE_COMPLETO/g, data.nombre);
html = html.replace(/NOMBRE/g, data.nombreDisplay);
html = html.replace(/DORSAL/g, data.dorsal);
html = html.replace(/FRASE Hero/g, data.frase);
html = html.replace(/HISTORIA/g, data.historia);

// Stats
let statsHtml = '';
data.stats.forEach(s => {
    statsHtml += '<div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: ' + data.color + ';">' + s.num + '</div><div style="font-size: 0.9rem; color: var(--gray); letter-spacing: 2px;">' + s.label + '</div></div>';
});
html = html.replace(/<div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">4<\/div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">TÍTULOS<\/div><\/div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">5<\/div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">AÑOS<\/div><\/div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">18<\/div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">PODIUMS<\/div><\/div><div style="text-align: center;"><div style="font-family: Orbitron; font-size: 3rem; font-weight: 900; color: var\(--neon\);">20\+<\/div><div style="font-size: 0\.9rem; color: var\(--gray\); letter-spacing: 2px;">VICTORIAS<\/div><\/div>/', statsHtml);

// Palmares
let palmaresHtml = '';
data.palmares.forEach(function(p) {
    palmaresHtml += '<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba(0,255,136,0.2);"><span style="color: var(--light);">' + p.titulo + '</span><span style="color: ' + data.color + '; font-family: Orbitron; font-weight: 700;">' + p.anyo + '</span></div>';
});
html = html.replace(/<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA RALLYJET GP2<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2010<\/span><\/div><div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA RALLYJET GP1 ATMOS<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2022<\/span><\/div><div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA RALLYJET GP3<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2023<\/span><\/div><div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA RALLYJET GP1 ATMOS<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2023<\/span><\/div><div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA OFFSHORE GP2<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2010<\/span><\/div><div style="display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; border-bottom: 1px solid rgba\(0,212,255,0\.2\);"><span style="color: var\(--light\);">CAMPEÓN DE ESPAÑA OFFSHORE GP1 ATMOS<\/span><span style="color: var\(--neon\); font-family: Orbitron; font-weight: 700;">2022<\/span><\/div>/, palmaresHtml);

fs.writeFileSync(path.join(__dirname, 'web', 'index.html'), html);
console.log('✅ Iñaki web built');
