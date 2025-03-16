import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_closing_prices(data, save_path="../results/closing_price_trends.png"):
    """Plots and saves the closing prices of different stocks over time."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    tickers = data['Ticker'].unique()
    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        subset = data[data['Ticker'] == ticker]
        plt.plot(subset['Date'], subset['Close'], label=ticker)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Closing Price Trends')
    plt.legend()
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Closing price trends saved to {save_path}")

def plot_correlation_matrix(data, save_path="../results/correlation_matrix.png"):
    """Plots and saves the correlation matrix heatmap of stock features."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    correlation_matrix = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Correlation matrix saved to {save_path}")

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("../data/cleaned_stocks.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    plot_closing_prices(df)
    plot_correlation_matrix(df)
