import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import os

def train_linear_regression(data_path, save_model_path="../results/predicted_stock_prices.csv"):
    """Train a Linear Regression model and save predictions."""
    os.makedirs(os.path.dirname(save_model_path), exist_ok=True)
    
    data = pd.read_csv(data_path)
    features = ['Open', 'High', 'Low', 'Volume', '50_MA', '200_MA', 'Volatility']
    target = 'Close'
    
    X = data[features]
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    predictions_df.to_csv(save_model_path, index=False)
    
    print(f"✅ Model trained! MSE: {mse}")
    print(f"✅ Predictions saved to {save_model_path}")

# Example usage
if __name__ == "__main__":
    train_linear_regression("../data/feature_engineered_stocks.csv")
