import requests
from bs4 import BeautifulSoup
import datetime


def fetch_currency_values():
    # URL of the page where the currency data is published
    url = 'your_source_url_here'

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the currency data
    # This will vary depending on the structure of your source page
    # Here's a generic example that you'll need to customize:
    currency_elements = soup.find_all('div', class_='currency-class')

    currencies = {}
    for element in currency_elements:
        currency_name = element.find('span', class_='currency-name-class').text
        currency_value = element.find('span', class_='currency-value-class').text
        currencies[currency_name] = currency_value

    return currencies


if __name__ == '__main__':
    print("Fetching currency values for", datetime.date.today())
    currency_values = fetch_currency_values()
    for name, value in currency_values.items():
        print(f"{name}: {value}")
