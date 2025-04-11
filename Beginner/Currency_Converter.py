def curr_conv(from_curr, to_curr, amount):
    rates = {
        'USD': 1.0,
        'EUR': 0.91,
        'INR': 83.2,
        'GBP': 0.78,
        'JPY': 151.6
    }

    usd_amount = amount / rates[from_curr]
    converted_amount = usd_amount * rates[to_curr]
    return round(converted_amount, 2)

from_curr = input("From currency (USD, EUR, INR, GBP, JPY): ")
to_curr = input("To currency (USD, EUR, INR, GBP, JPY): ")
amount = float(input("Amount: "))

result = curr_conv(from_curr, to_curr, amount)
print(f"{amount} {from_curr.upper()} = {result} {to_curr.upper()}")