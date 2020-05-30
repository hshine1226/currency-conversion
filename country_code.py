import requests
from bs4 import BeautifulSoup

COUNTRY_CODE = "https://www.iban.com/currency-codes"


def get_country_code():
    r = requests.get(COUNTRY_CODE)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    trs = soup.find_all('tr')[1:]

    country_code = []

    for tr in trs:
        country = tr.contents[1].string.capitalize()
        currency = tr.contents[3].string
        code = tr.contents[5].string
        # number = tr.contents[7].string
        if not currency == 'No universal currency':
            dictionary = {
                'country': country,
                'code': code
            }
            country_code.append(dictionary)
    return country_code
