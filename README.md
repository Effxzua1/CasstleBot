# Casstle Bot · Web

Página oficial de Casstle Bot: comandos, centro de ayuda, tickets, planes Premium y estadísticas en vivo.
HTML, CSS y JavaScript puros, sin dependencias ni paso de compilación.

## Estructura

```
index.html
casstle_web.py        servidor opcional para el bot (aiohttp)
assets/
  css/style.css
  js/config.js        enlaces, comandos, planes, servidores y FAQ
  js/app.js           lógica de la página
  img/                logo, banner, iconos y capturas
```

## Probar en local

```bash
python -m http.server 8000
```

Abre http://localhost:8000

## Publicar en GitHub Pages

1. Sube el contenido de esta carpeta a un repositorio.
2. En **Settings → Pages** elige la rama `main` y la carpeta `/ (root)`.
3. En Pages no hay bot detrás: las cifras se muestran con los valores de `fallback` de `config.js`.

## Estadísticas en vivo

Si ejecutas el bot, llama a `start_web(bot)` de `casstle_web.py`. Sirve la web y `/api/stats` con servidores, usuarios, comandos y ping.
Para usar la API desde Pages, pon su URL completa en `CONFIG.api` (el servidor ya permite CORS).

## Personalizar

Edita solo `assets/js/config.js`: enlaces de invitación y soporte, servidores, planes y preguntas frecuentes.
