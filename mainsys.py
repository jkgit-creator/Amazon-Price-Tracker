from scrapper import check_price
from mail import send_mail
import time

#make sure to change URL, headers, and target_price to fit your needs
URL = 'https://www.amazon.com/Samsung-UN65RU7100FXZA-Flat-UHD-Smart/dp/B07NC96MBL/ref=sr_1_3?crid=H22V0N3BA0T3&keywords=samsung%2Btv%2B65&qid=1579368861&sprefix=samsung%2Btv%2Caps%2C194&sr=8-3&th=1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
target_price = 600

while(True):
    converted_price, title = check_price(URL, headers)
    if converted_price <= target_price:
        send_mail(URL, title)
    time.sleep(86400)






