from bs4 import BeautifulSoup
import requests
import smtplib
URL="https://www.amazon.com/Kate-Spade-New-York-Saffiano/dp/B09LGYYWSJ/ref=sr_1_8?keywords=kate%2Bspade%2Bbags%2Bfor%2Bwomen&qid=1675289067&sprefix=kate%2Bbags%2Caps%2C137&sr=8-8&th=1"
response = requests.get(URL,headers={'Accept-Language':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

soup = BeautifulSoup(response.text, 'html.parser')
price=soup.find(class_='a-offscreen')
title=soup.find(class_="a-size-large product-title-word-break")
price=float(price.getText().split('$')[1])
title=title.getText()

target_price=200
if price<=target_price:
    my_email="sameeranati@gmail.com"
    my_password="kedwoffjezzwsmug"
    connection=smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"{title} is selling at your target price {price}.Click on the link to get it: {URL}")
    connection.close()
