# stock_analysis.py
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def plot_stock_data(stock_data, symbol):
    stock_data['Close'].plot(figsize=(10, 5), label=symbol)
    plt.title(f'{symbol} 주가 분석')
    plt.xlabel('날짜')
    plt.ylabel('종가')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # 예제로 'AAPL' (애플 주식) 데이터를 가져와서 분석합니다.
    symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'

    data = get_stock_data(symbol, start_date, end_date)
    plot_stock_data(data, symbol)
