def currency_converter(amount, from_currency, to_currency):
    # Conversion rates (example rates, not accurate)
    conversion_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.72, 'JPY': 110.5},
        'EUR': {'USD': 1.18, 'GBP': 0.84, 'JPY': 130.2},
        'GBP': {'USD': 1.39, 'EUR': 1.19, 'JPY': 155.8},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0064}
    }
    
    if from_currency == to_currency:
        return amount
    
    if from_currency in conversion_rates and to_currency in conversion_rates[from_currency]:
        conversion_rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Conversion not supported"

# Test the converter
amount_to_convert = float(input("Enter the amount: "))
from_currency = input("Enter the source currency (e.g., USD, EUR, GBP, JPY): ").upper()
to_currency = input("Enter the target currency (e.g., USD, EUR, GBP, JPY): ").upper()

converted_amount = currency_converter(amount_to_convert, from_currency, to_currency)
if type(converted_amount) == float:
    print(f"{amount_to_convert:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print(converted_amount)

    #// Open With python:)
