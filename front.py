import ccxt
import time

# Configure your exchange and API credentials
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Define trading parameters
symbol = 'ETH/USDT'
buy_threshold = 0.98  # Buy when the price drops by 2%
sell_threshold = 1.02  # Sell when the price increases by 2%
trade_amount = 0.01  # Amount of ETH to trade

# Function to get the current price of the symbol
def get_current_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# Main trading loop
while True:
    try:
        # Fetch current price
        current_price = get_current_price(symbol)
        print(f"Current price: {current_price}")

        # Check for buy condition
        if current_price <= last_price * buy_threshold:
            print("Buying ETH...")
            exchange.create_market_buy_order(symbol, trade_amount)
            last_price = current_price

        # Check for sell condition
        elif current_price >= last_price * sell_threshold:
            print("Selling ETH...")
            exchange.create_market_sell_order(symbol, trade_amount)
            last_price = current_price

        # Wait for a specified period before checking again
        time.sleep(60)  # Check every minute

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)  # Wait before retrying