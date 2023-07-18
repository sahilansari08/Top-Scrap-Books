from bs4 import BeautifulSoup
import requests, json

html_content = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html").content

soup = BeautifulSoup(html_content, "html.parser")

# List all books type...
def get_all_books_type():
    ul = soup.find_all("ul")[-1]
    li_list  = ul.find_all("li")
    books = []
    for li in li_list:
        books.append(li.text.strip())
    return books

# Fetch all books by link.
def fetch_books():
    books=[]
    ol = soup.find("ol")
    li_list = ol.find_all("li")
    for li in li_list:
        book_name = li.find("h3").text
        book_price = li.find("p", class_="price_color").text
        book_image = li.find("img", class_="thumbnail").get("src")
        book_image = "https://books.toscrape.com"+book_image[11:]
        book_link  = li.find("h3").find("a").get("href")
        book_link  = "https://books.toscrape.com/catalogue"+book_link[8:]
        # print(book_name,book_price,book_image,book_link)
        books.append({
            "name": book_name,
            "price": book_price,
            "image": book_image,
            "link": book_link
        })
    f=open("books.json","w")
    json.dump(books,f,indent=4)
    return books