import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Create the results folder if it doesn't exist
import os
os.makedirs("../results", exist_ok=True)

# Load the processed dataset
data = pd.read_csv('../data/cleaned_stocks.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Get unique stock tickers
tickers = data['Ticker'].unique()

# 📊 1. Plot Closing Price Trends and Save
plt.figure(figsize=(12, 6))
for ticker in tickers:
    subset = data[data['Ticker'] == ticker]
    plt.plot(subset['Date'], subset['Close'], label=ticker)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Closing Price Trends')
plt.legend()
plt.savefig('../results/closing_price_trends.png')  # Save the plot
plt.close()

# 🔥 2. Correlation Matrix Heatmap
correlation_matrix = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.savefig('../results/correlation_matrix.png')  # Save the plot
plt.close()

# 🏆 3. Train a Linear Regression Model and Plot Actual vs. Predicted
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

X = data[features]
y = data[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Save predictions
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv('../results/predicted_stock_prices.csv', index=False)

# 📈 Plot Actual vs Predicted Closing Prices
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Closing Price")
plt.ylabel("Predicted Closing Price")
plt.title("Actual vs Predicted Closing Prices")
plt.savefig('../results/actual_vs_predicted.png')  # Save the plot
plt.close()

print("✅ Graphs and predictions saved in the 'results/' folder!")
