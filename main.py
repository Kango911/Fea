import pandas as pd
import matplotlib.pyplot as plt

# Загружаем файл bitcoin.csv
df = pd.read_csv('bitcoin.csv')

# Вычисляем медианную цену
df['Median Price'] = (df['Open'] + df['High'] + df['Low']) / 3

# Строим график медианной цены и цены закрытия
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['Median Price'], label='Median Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Closing Price vs. Median Price')
plt.legend()
plt.grid(True)
plt.show()

# Выводим даты, когда максимальная цена была больше медианной на 4%
high_price_dates = df[df['High'] > 1.04 * df['Median Price']]['Date']
print("Dates when High price was greater than Median price by 4%:")
print(high_price_dates.to_string(index=False))
