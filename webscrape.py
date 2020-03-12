import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = "https://www.newegg.com/global/uk-en/Desktop-Graphics-Cards/SubCategory/ID-48?nm_mc=KNC-GoogleukAdwords&cm_mmc=KNC-GoogleukAdwords-_-Sitelink-UK-_-VGA-Cards-_-Global&gclid=CjwKCAjwmKLzBRBeEiwACCVihksnmGH9wBH824qQO35sFJRu3rxlW5dd9VrS-Jn5pubXMEHWxTFM5BoCpV0QAvD_BwE"
uClient = uReq(url)
page_html = uClient.read()
# close the file
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
filename = "products.csv"
f = open(filename,"w")
headers = "brand, product_name, price\n"
f.write(headers)
for container in containers:
    title = container.a.img["title"]
    brand = container.findAll("a",{"class":"item-brand"})[0].img["alt"]
    try:
        price = "£" + container.findAll("li",{"class":"price-current"})[0].strong.text
    except:
        price = "0"
    
    f.write(brand + "," + title.replace(",","|") + "," + price + "\n")

f.close()
