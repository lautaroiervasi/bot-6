"""
main.py - template starter for Binance Testnet + Telegram on Render (Python 3.10)

IMPORTANT:
- Replace values in config.json with your TESTNET keys before deploying.
- This file is intentionally minimal. Integrá aquí tu lógica de estrategia (EMA/RSI/MACD/ATR, etc.)
"""

import json
import time
import os
from pathlib import Path

try:
    from telegram import Bot
except Exception as e:
    print("Error importing telegram library:", e)
    raise

try:
    from binance.client import Client
except Exception as e:
    print("Error importing binance client:", e)
    raise

CONFIG_PATH = Path(__file__).parent / "config.json"

def load_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError("config.json not found. Copiá config.json.example y completá las claves.")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def setup_binance_client(cfg):
    api_key = cfg.get("BINANCE_TESTNET_API_KEY")
    api_secret = cfg.get("BINANCE_TESTNET_API_SECRET")
    client = Client(api_key, api_secret, testnet=cfg.get("USE_TESTNET", True))
    # If using python-binance older/new versions, set the base_url for testnet:
    try:
        client.API_URL = "https://testnet.binance.vision/api"
    except Exception:
        pass
    return client

def send_telegram(bot_token, chat_id, text):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=text)

def main():
    cfg = load_config()
    # Basic checks
    for k in ["BINANCE_TESTNET_API_KEY", "BINANCE_TESTNET_API_SECRET", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]:
        if not cfg.get(k) or cfg.get(k).startswith("PUT_YOUR"):
            print(f"AVISO: Editá config.json y completá la clave `{k}` antes de desplegar.")
    print("Iniciando bot (modo Testnet):", cfg.get("USE_TESTNET", True))
    # Setup clients
    try:
        binance = setup_binance_client(cfg)
    except Exception as e:
        print("No se pudo conectar con Binance:", e)
        return
    try:
        # quick call to test connectivity
        status = binance.get_account_api_trading_status()
        print("Conexión Binance OK. Trading status:", status)
    except Exception as e:
        print("Advertencia: no se pudo leer account status (en Testnet puede fallar):", e)
    # Telegram notify
    try:
        send_telegram(cfg.get("TELEGRAM_BOT_TOKEN"), cfg.get("TELEGRAM_CHAT_ID"), "Bot arrancado en Render (Testnet). ✅")
        print("Mensaje Telegram enviado.")
    except Exception as e:
        print("No se pudo enviar Telegram (revisá token/chat_id):", e)
    # Aquí va el loop principal de tu bot. Mantenélo simple para Render.
    try:
        while True:
            # Placeholder: en tu bot real, llamá a la lógica de señales/ordenes aquí
            print("Loop heartbeat - bot vivo. Timestamp:", time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(60)
    except KeyboardInterrupt:
        print("Terminando por KeyboardInterrupt.")
    except Exception as e:
        print("Error en loop principal:", e)

if __name__ == "__main__":
    main()
