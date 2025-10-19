
import os
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from decimal import Decimal, getcontext

# --- Configuration ---
app = Flask(__name__, template_folder='../templates')
CORS(app)
getcontext().prec = 10  # Set precision for Decimal calculations

# --- API and Constants ---
FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY', 'YOUR_FINNHUB_KEY_HERE') # Use environment variables
BOT_PUBLIC_KEY = 'YOUR_BOT_PUBLIC_KEY_HERE'
DISCLAIMER = "⚠️ This is not financial advice. All data is informational only and may be delayed. Always DYOR."

# --- Helper Functions ---
def show_error(message):
    print(f"ERROR: {message}")
    return {"error": message}

# --- API Fetching Functions ---
def fetch_crypto_data(coin_id='bitcoin'):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return show_error(f"Crypto fetch failed: {e}")

def fetch_stock_data(symbol='AAPL'):
    if FINNHUB_API_KEY == 'YOUR_FINNHUB_KEY_HERE':
        return show_error("Finnhub API key is not set.")
    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return show_error(f"Stock fetch failed: {e}")

def fetch_deso_data():
    try:
        global_response = requests.get('https://node.deso.org/api/v0/get-global-state')
        global_response.raise_for_status()
        global_data = global_response.json()
        
        crypto_data = fetch_crypto_data('deso')
        if 'error' in crypto_data:
            return crypto_data

        return {"global": global_data, "crypto": crypto_data}
    except requests.exceptions.RequestException as e:
        return show_error(f"DeSo fetch failed: {e}")

# --- Math and Logic Functions ---
def calculate_roi(initial, current):
    if initial == 0: return Decimal(0)
    return ((Decimal(current) - Decimal(initial)) / Decimal(initial) * 100).quantize(Decimal('0.01'))

# --- Bot Response Logic ---
def get_bot_response(query):
    lower_query = query.lower()

    # DeSo Stats
    if 'deso' in lower_query and any(k in lower_query for k in ['price', 'block', 'supply']):
        data = fetch_deso_data()
        if 'error' in data:
            return f"{DISCLAIMER} {data['error']}"
        
        deso_price = data.get('crypto', {}).get('deso', {}).get('usd', 'N/A')
        change_24h = data.get('crypto', {}).get('deso', {}).get('usd_24h_change', 0)
        block_height = data.get('global', {}).get('LatestBlockHeight', 'N/A')
        supply_nanos = data.get('global', {}).get('Mempool', {}).get('TotalDESOInCirculationNanos', 0)
        token_supply = (Decimal(supply_nanos) / Decimal(1e9)).quantize(Decimal('0.01'))
        
        return f"{DISCLAIMER} DeSo Stats: Price: ${deso_price} (24h: {change_24h:+.2f}%). Block: {block_height}. Supply: {token_supply} DESO."

    # Generic Crypto
    if 'crypto' in lower_query or 'coin' in lower_query or any(c in lower_query for c in ['btc', 'eth', 'sol']):
        coin_id = 'bitcoin'
        if 'eth' in lower_query: coin_id = 'ethereum'
        elif 'sol' in lower_query: coin_id = 'solana'
        
        data = fetch_crypto_data(coin_id)
        if 'error' in data or not data.get(coin_id):
            return f"{DISCLAIMER} Could not fetch data for {coin_id}."
            
        price = data[coin_id].get('usd', 'N/A')
        change_24h = data[coin_id].get('usd_24h_change', 0)
        market_cap = data[coin_id].get('usd_market_cap', 0)
        trend = 'up' if change_24h > 0 else 'down' if change_24h < 0 else 'stable'
        
        return f"{DISCLAIMER} {coin_id.upper()}: ${price:,.2f} (24h: {change_24h:+.2f}%). Trend: {trend}. Cap: ${(market_cap / 1e9):.2f}B USD."

    # Stocks
    if 'stock' in lower_query or any(s in lower_query for s in ['aapl', 'tsla', 'goog']):
        symbol = 'AAPL'
        if 'tsla' in lower_query: symbol = 'TSLA'
        elif 'goog' in lower_query: symbol = 'GOOGL'
        
        data = fetch_stock_data(symbol)
        if 'error' in data:
            return f"{DISCLAIMER} {data['error']}"

        price = data.get('c', 'N/A')
        change = data.get('d', 0)
        change_percent = data.get('dp', 0)
        trend = 'up' if change > 0 else 'down' if change < 0 else 'stable'
        
        return f"{DISCLAIMER} {symbol}: ${price} (Daily: {change:+.2f} ({change_percent:.2f}%)). Trend: {trend}."

    # Fallback
    return 'Query not understood. Try "DESO price", "BTC price", or "AAPL stock".'

# --- Flask Routes ---
@app.route('/')
def index():
    """Render the chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided."}), 400
        
        bot_response = get_bot_response(user_message)
        return jsonify({"response": bot_response})
        
    except Exception as e:
        print(f"Chat endpoint error: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Note: For production, use a proper WSGI server like Gunicorn or Waitress
    # This server is for development only.
    app.run(host='0.0.0.0', port=8080, debug=True)
