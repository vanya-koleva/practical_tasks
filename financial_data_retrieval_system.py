import requests


class FinancialDataRetrievalSystem:
    def __init__(self, currency_api_key, share_api_key):
        # Initialize attributes
        self.currency_api_key = currency_api_key
        self.share_api_key = share_api_key

    def get_currency_exchange_rate(self, base_currency, target_currency):
        # Retrieve the current exchange rate between two currencies using the currency API
        url = f"https://v6.exchangerate-api.com/v6/{currency_api_key}/pair/{base_currency}/{target_currency}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()["conversion_rate"]
        print(f"Current exchange rate: {data}")

    def get_company_share_price(self, company_symbol):
        # Retrieve the current price of shares for a given company using the share API
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' \
              f'{company_symbol}&apikey={share_api_key}'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()['Global Quote']['05. price']
        print(f"{company_symbol} share price: {data}")

    def get_currency_conversion(self, amount, base_currency, target_currency):
        # Convert the given amount from one currency to another
        url = f"https://v6.exchangerate-api.com/v6/{currency_api_key}/pair/{base_currency}/{target_currency}/{amount}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()["conversion_result"]
        print(f"{amount}{base_currency} = {data}{target_currency}")

    def get_company_info(self, company_symbol):
        # Retrieve additional information about a company (e.g., name, sector) using the share API
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={company_symbol}&apikey={share_api_key}'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()
        for key, value in data.items():
            print(f"{key}: {value}")

    def get_top_gainers(self):
        # Retrieve the top gaining companies from the share API
        url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={share_api_key}'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()["top_gainers"]
        print("Top gainers:")
        for item in data:
            print(item["ticker"])

    def get_top_losers(self):
        # Retrieve the top losing companies from the share API
        url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={share_api_key}'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        data = response.json()["top_losers"]
        print("Top losers:")
        for item in data:
            print(item["ticker"])


# Example usage of the Financial Data Retrieval System
if __name__ == "__main__":
    # Configure API keys
    # Get your "CURRENCY_API_KEY" from https://www.exchangerate-api.com/
    # Get your "SHARE_API_KEY" from https://www.alphavantage.co/
    currency_api_key = 'YOUR_CURRENCY_API_KEY'
    share_api_key = 'YOUR_SHARE_API_KEY'

    # Initialize the FinancialDataRetrievalSystem object
    financial_system = FinancialDataRetrievalSystem(currency_api_key, share_api_key)

    # Call methods of the FinancialDataRetrievalSystem object as needed...
    # Examples:
    financial_system.get_currency_exchange_rate("USD", "EUR")
    financial_system.get_currency_conversion(100, "EUR", "USD")
    financial_system.get_company_share_price("AAPL")
    financial_system.get_company_info("AAPL")
    financial_system.get_top_gainers()
    financial_system.get_top_losers()
