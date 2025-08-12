import pandas as pd
import requests
from bs4 import BeautifulSoup
book_names=[]
prices=[]
stocks=[]

for i in range (1,26):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    data_main = requests.get(url).text
    soup = BeautifulSoup(data_main ,"lxml")
    
    for h3 in soup.find_all("h3"):
        a_tag = h3.find("a")
        if a_tag:
            book_name = a_tag.getText(strip=True)
            book_names.append(book_name)
    for price_tag in soup.find_all("p",class_ = "price_color"):
        price = price_tag.get_text(strip=True)
        prices.append(price)
    for stock1 in soup.find_all("p", class_ ="instock availability"):
        stock = stock1.get_text(strip=True)
        stocks.append(stock)

dataframe1  = pd.DataFrame({"BOOK_NAMES" :book_names,
                            "STOCKS" :stocks,
                            "PRICES" :prices})
print(dataframe1)
scrapped_data =dataframe1.to_csv("extracted_data_all_pages.csv")
scrapped_data =dataframe1.to_excel("extracted_data2.xlsx", engine="openpyxl")






