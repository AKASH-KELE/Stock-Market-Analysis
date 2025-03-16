import pandas as pd

def load_data(filepath):
    """Loads a CSV file and returns a Pandas DataFrame."""
    try:
        data = pd.read_csv(filepath)
        print(f"✅ Successfully loaded data from {filepath}")
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    df = load_data("../data/cleaned_stocks.csv")
    print(df.head())
