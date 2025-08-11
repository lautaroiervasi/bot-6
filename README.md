# Trading Bot - Render (Testnet) - Template

**Objetivo:** plantilla lista para desplegar en Render usando Python 3.10 y Binance **Testnet**.

## Contenido
- `main.py` - script de arranque (conectividad básica a Testnet y Telegram).
- `requirements.txt` - dependencias.
- `render.yml` - configuración para Render (Python 3.10).
- `Procfile` - opcional (compatibilidad con Railway/Heroku).
- `config.json` - archivo de configuración con **placeholders** (método simple).
- `README.md` - este archivo.

## Pasos para usar
1. **Subí el ZIP** a Render como nuevo repo / proyecto.
2. En `config.json` reemplazá los placeholders por tus claves **Testnet** (NO uses claves Spot reales en esta carpeta).
3. Desplegá. Render instalará dependencias y ejecutará `python main.py`.
4. Si querés mover a Spot real, cambia el endpoint y las claves en `config.json` (y revisá el código antes de ejecutar con dinero real).

**ATENCIÓN:** Este template no incluye tu código completo de estrategia. Integra tu `bot.py` real reemplazando la lógica dentro de `main.py` o añadiendo tus módulos.
