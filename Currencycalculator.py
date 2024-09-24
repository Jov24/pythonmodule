from bs4 import BeautifulSoup
import requests


def get_rate(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    request = requests.get(url).content
    soup = BeautifulSoup(request, "html.parser").find("span", class_="ccOutputRslt").get_text()
    rate = float(soup[:-4])
    return rate

def main():
    in_currency = input("Enter from Currency Code: ")
    out_currency = input("Enter to Currency Code: ")
    return get_rate(in_currency, out_currency)

print(main()) 