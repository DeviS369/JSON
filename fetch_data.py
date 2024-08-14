import requests
class country_currency:
    def __init__(self, url):
        self.url = url
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code

    def fetch_headers(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return "ERROR : 404"
    def fetch_data(self):
        """Fetches the JSON data from the provided URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check for HTTP errors
            self.data = response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def display_all_countries_and_currencies(self):
        """Displays all countries, their currencies, and currency symbols."""
        if self.data:
            for country in self.data:
                country_name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    symbol = currency_info.get('symbol', 'N/A')
                    print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {symbol}")
        else:
            print("No data available. Please fetch the data first.")

    def display_countries_with_dollar(self):
        """Displays all countries that use DOLLAR as their currency."""
        if self.data:
            for country in self.data:
                country_name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    if 'dollar' in currency_name.lower():
                        symbol = currency_info.get('symbol', 'N/A')
                        print("Dollar Data :")
                        print("**************")
                        print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {symbol}")
        else:
            print("No data available. Please fetch the data first.")

    def display_countries_with_euro(self):
        """Displays all countries that use DOLLAR as their currency."""
        if self.data:
            for country in self.data:
                country_name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    if 'euro' in currency_name.lower():
                        symbol = currency_info.get('symbol', 'N/A')
                        print("Euro Data :")
                        print("______________")
                        print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {symbol}")
        else:
            print("No data available. Please fetch the data first.")            
if __name__ == '__main__':
    url = 'https://restcountries.com/v3.1/all'
    obj = country_currency(url)
    print("SERVER STATUS CODE : ", obj.api_status_code())
    print("Fetch_Data",obj.fetch_data())
    print("Headers",obj.fetch_headers())
    print("data " , obj.display_all_countries_and_currencies())
    print("Dollar Data", obj.display_countries_with_dollar())
    print("Euro Data",obj.display_countries_with_euro())
            
