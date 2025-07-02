import requests
import pandas as pd
url ="https://api.exchangerate-api.com/v4/latest/USD"
response=requests.get(url)
data=response.json()
last_update=data["date"]
exrate=data["rates"]
#print(last_update)
df = pd.DataFrame.from_dict(exrate, orient='index', columns=['Rate'])


own_currency = input("Enter the currency you have (e.g., USD, EUR, JPY): ").upper()
target_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, JPY): ").upper()
amount = float(input("Enter the amount you want to exchange: "))

amount_in_usd = amount / df.loc[own_currency, "Rate"]
converted_amount = amount_in_usd * df.loc[target_currency, "Rate"]
print(f"{amount} {own_currency} = {converted_amount:.2f} {target_currency}")



