import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def predict_stock_prices(model_path, data_path):
    """Loads trained model and makes predictions on new stock data."""
    # Load data
    data = pd.read_csv(data_path)
    features = ['Open', 'High', 'Low', 'Volume', '50_MA', '200_MA', 'Volatility']
    X = data[features]
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Load trained model
    model = joblib.load(model_path)
    
    # Make predictions
    predictions = model.predict(X_scaled)
    
    # Save predictions
    data['Predicted_Close'] = predictions
    data.to_csv("../results/predicted_stock_prices.csv", index=False)
    
    print("✅ Predictions saved to '../results/predicted_stock_prices.csv'")
    return data

# Example usage
if __name__ == "__main__":
    predict_stock_prices("../results/trained_model.pkl", "../data/feature_engineered_stocks.csv")
