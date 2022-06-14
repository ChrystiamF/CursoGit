import yfinance as yf

df=yf.download('AAPL',period='max',interval='1d')
print(df)