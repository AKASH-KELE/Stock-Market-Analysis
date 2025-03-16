import pandas as pd

def clean_data(data):
    """Cleans the dataset by handling missing values and sorting it by date."""
    data.dropna(inplace=True)  # Remove missing values
    data['Date'] = pd.to_datetime(data['Date'])  # Convert Date column to datetime
    data = data.sort_values(by=['Ticker', 'Date'])  # Sort data
    return data

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("../data/stocks.csv")
    cleaned_df = clean_data(df)
    cleaned_df.to_csv("../data/cleaned_stocks.csv", index=False)
    print("✅ Data cleaning complete! Saved to '../data/cleaned_stocks.csv'")
