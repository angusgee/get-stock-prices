import yfinance as yf
import pandas as pd
import warnings
import time

warnings.filterwarnings('ignore', category=FutureWarning, module='yfinance.utils')

def get_ltp(symbol):
    symbol = symbol.replace('.', '-')    
    stock_data = yf.Ticker(symbol)
    # print(f"getting prices for {symbol}")
    price_data = stock_data.history(period='1d')
    if price_data.empty:
        return 0
    else:
        ltp = (round(price_data['Close'].iloc[-1], 2))
        # print(f"LTP for {symbol}: {ltp}")
        return ltp

def main():
    start_time = time.time()
    df = pd.read_csv('./tickers.csv', header=None, names=['Ticker'])
    df['Last traded price'] = df['Ticker'].apply(get_ltp)
    print(df.head)
    df.to_csv('tickers-with-prices.csv', index=False)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time: {duration} seconds")

if __name__ == '__main__':
    main()