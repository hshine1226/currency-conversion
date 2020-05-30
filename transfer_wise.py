import requests
from bs4 import BeautifulSoup


def get_converted(source, target, amount):
    URL = f"https://transferwise.com/gb/currency-converter/{source}-to-{target}-rate?amount={amount}"
    r = requests.get(URL)
    html_doc = r.content
    soup = BeautifulSoup(html_doc, 'html.parser')

    try:
        target_amount = soup.find(id="cc-amount-to")['value']
    except:
        print("Doesn't exsist code in TransferWise")
        return False

    return target_amount
