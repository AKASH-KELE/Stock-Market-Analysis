<!-- @format -->

# Stock Market Analysis Project

## 📌 Project Overview

This project aims to analyze stock prices of **Apple (AAPL), Microsoft (MSFT), Netflix (NFLX), and Google (GOOG)** using **data science and machine learning techniques**. It includes **data preprocessing, exploratory data analysis (EDA), feature engineering, and predictive modeling**.

## 📂 Project Structure

```
Stock-Market-Analysis/
│── data/                 # Contains raw & cleaned datasets
│   ├── stocks.csv
│   ├── cleaned_stocks.csv
│   ├── feature_engineered_stocks.csv
│   ├── data_description.txt
│
│── notebooks/            # Jupyter Notebooks for each phase
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Stock_Price_Prediction.ipynb
│
│── src/                  # Reusable Python scripts
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── visualization.py
│   ├── train_model.py
│   ├── predict.py
│
│── results/               # Outputs & reports
│   ├── closing_price_trends.png
│   ├── correlation_matrix.png
│   ├── actual_vs_predicted.png
│   ├── eda_summary.txt
│   ├── model_evaluation.txt
│   ├── predicted_stock_prices.csv
│
│── README.md
│── .gitignore
```

## 🚀 Steps to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

### 2️⃣ Run Data Processing & EDA

```bash
python src/data_loader.py
python src/preprocessing.py
python src/visualization.py
```

### 3️⃣ Train the Model

```bash
python src/train_model.py
```

### 4️⃣ Make Predictions

```bash
python src/predict.py
```

## 📊 Results

- **Stock Price Trends:** `results/closing_price_trends.png`
- **Feature Correlation Matrix:** `results/correlation_matrix.png`
- **Actual vs Predicted Prices:** `results/actual_vs_predicted.png`
- **Predicted Prices CSV:** `results/predicted_stock_prices.csv`

## 📌 Future Enhancements

- Implement **LSTM models** for time-series forecasting.
- Add **technical indicators** like RSI and MACD.
- Improve accuracy with **Random Forest & XGBoost models**.

✅ **Project Completed!** 🚀
