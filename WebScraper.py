import urllib
import urllib.request
from bs4 import BeautifulSoup


def make_soup(url):
    the_page = urllib.request.urlopen(url)
    soup_data = BeautifulSoup(the_page, "html.parser")
    return soup_data


soup = make_soup("https://www.newegg.com/p/pl?d=gpu&Order=0")

containers = soup.findAll("div", {"class": "item-container"})

filename = "products.csv"

f = open(filename, "w")

headers = "Brand, Product Name, Price, Shipping\n"
f.write(headers)

for container in containers[4:]:
    brand = container.div.div.a.img["title"]
    print(brand)

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    print(product_name)

    price_container = container.findAll("li", {"class": "price-current"})
    product_price = price_container[0].text
    print(product_price.replace("–", " "))

    shipping_container = container.findAll("li", {"class": "price-ship"})
    product_shipping = shipping_container[0].text
    print(product_shipping)

    f.write(brand + "," + product_name.replace(",", "/") + "," + product_price.replace("–", "") + "," + product_shipping + "\n")

f.close()
