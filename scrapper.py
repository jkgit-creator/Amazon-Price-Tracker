import requests
from bs4 import BeautifulSoup

def check_price(URL, headers):
    """
    Checks the price of the desired product off of Amazon

    Parameters:
        URL: a url link
        headers: the user agent of the user's web browser

    Returns:
        converted_price(float): the current listed price of the product
        title(string): the title of the product
    """
    page = requests.get(URL, headers = headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(id="priceblock_ourprice").get_text()
    price = price.replace(',', '')
    converted_price = float(price[1:])
    return converted_price, title