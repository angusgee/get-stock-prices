import yfinance as yf
import pandas as pd
import warnings
import time

warnings.filterwarnings('ignore', category=FutureWarning, module='yfinance.utils')

def add_exchange_to_ticker(symbol, exchange):
    if exchange == 'XETRA':
        return symbol + '.DE'
    else:
        return symbol

def get_ltp(ticker):
    ticker = ticker.replace('.', '-')    
    stock_data = yf.Ticker(ticker)
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
    df = pd.read_csv('./eu-tickers.csv', header=None)
    df.columns = ['Ticker', 'Exchange']
    df['Full ticker'] = df.apply(lambda row: add_exchange_to_ticker(row['Ticker'], row['Exchange']), axis=1)
    
    # df['Last traded price'] = df['Ticker'].apply(get_ltp)
    print(df.head)
    df.to_csv('eu-tickers-with-prices.csv', index=False)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time: {duration} seconds")

if __name__ == '__main__':
    main()