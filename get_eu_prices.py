import yfinance as yf
import pandas as pd
import warnings
import time
import re

warnings.filterwarnings('ignore', category=FutureWarning, module='yfinance.utils')

def add_exchange_to_ticker(symbol, exchange):
    if exchange == 'XETRA':
        return symbol + '.DE'
    if exchange == 'EURONEXT - EURONEXT BRUSSELS':
        return symbol + '.BR'
    if exchange == 'EURONEXT - EURONEXT AMSTERDAM':
        return symbol + '.AS'
    if exchange == 'BOLSA DE MADRID':
        return symbol + '.MC'
    if exchange == 'ATHENS EXCHANGE S.A. CASH MARKET':
        return symbol + '.AT'
    if exchange == 'BUDAPEST STOCK EXCHANGE':
        return symbol + '.BUD'
    if exchange == 'ELECTRONIC SHARE MARKET':
        return symbol
    if exchange == 'EURONEXT - EURONEXT PARIS':
        return symbol + '.PA'
    if exchange == 'EURONEXT GROWTH PARIS':
        return symbol + '.PA'
    if exchange == 'FIRST NORTH FINLAND - SME GROWTH MARKET':
        return symbol + '.HE'
    if exchange == 'FIRST NORTH SWEDEN - SME GROWTH MARKET':
        return symbol + '.ST'
    if exchange == 'HANSEATISCHE WERTPAPIERBOERSE HAMBURG':
        return symbol + '.HM'
    if exchange == 'IRISH STOCK EXCHANGE - ALL MARKET':
        return symbol + '.IR'
    if exchange == 'LJUBLJANA STOCK EXCHANGE (OFFICIAL MARKET)':
        return symbol + '.LJ'
    if exchange == 'MOSCOW EXCHANGE - ALL MARKETS':
        return symbol + '.ME'
    if exchange == 'NASDAQ COPENHAGEN A/S':
        return symbol + '.CO'
    if exchange == 'LONDON STOCK EXCHANGE':
        return symbol + '.L'
    if exchange == 'NASDAQ HELSINKI LTD':
        return symbol + '.HE'
    if exchange == 'NASDAQ ICELAND HF.':
        return symbol + '.IC'
    if exchange == 'NASDAQ STOCKHOLM AB':
        return symbol + '.ST'
    if exchange == 'OPERADOR DE MERCADO IBERICO DE ENERGIA - PORTUGAL':
        return symbol + '.LS'
    if exchange == 'OSLO BORS ASA':
        return symbol + '.OL'
    if exchange == 'PRAGUE STOCK EXCHANGE':
        return symbol + '.PR'
    if exchange == 'SIX SWISS EXCHANGE':
        return symbol + '.SW'
    if exchange == 'WARSAW STOCK EXCHANGE/EQUITIES/MAIN MARKET':
        return symbol + '.WA'
    else:
        return symbol

def get_ltp(ticker):
    stock_data = yf.Ticker(ticker)
    print(f"getting prices for {ticker}")
    price_data = stock_data.history(period='1d')
    if price_data.empty:
        return 0
    else:
        ltp = (round(price_data['Close'].iloc[-1], 2))
        print(f"LTP for {ticker}: {ltp}")
        return ltp

def main():
    start_time = time.time()
    df = pd.read_csv('./test.csv', header=None)
    df.columns = ['Ticker', 'Exchange']
    df['Ticker'] = df['Ticker'].str.replace(' ', '')
    df['Full ticker'] = df.apply(lambda row: add_exchange_to_ticker(row['Ticker'], row['Exchange']), axis=1)
    
    df['Last traded price'] = df['Full ticker'].apply(get_ltp)
    print(df.head)
    df.to_csv('eu-tickers-with-prices.csv', index=False)
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution time: {duration} seconds")

if __name__ == '__main__':
    main()