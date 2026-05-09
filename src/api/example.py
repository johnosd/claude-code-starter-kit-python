import os
import requests

API_KEY = "sk-1234567890abcdef"  # hardcoded secret

def get_books(query, page=1):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def process_results(data):
    books = []
    for item in data["items"]:
        book = {}
        book["title"] = item["volumeInfo"]["title"]
        book["author"] = item["volumeInfo"]["authors"]
        book["title2"] = item["volumeInfo"]["title"]  # duplicado
        books.append(book)
    return books

def save_book(title, author, price):
    try:
        # salva no banco
        pass
    except:
        pass